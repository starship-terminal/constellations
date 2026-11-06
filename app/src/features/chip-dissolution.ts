const DURATION = 500;
const MAX_ACTIVE = 6;
const MAX_PARTICLES = 700;
const active = new Set<() => void>();

interface Particle {
  x: number;
  y: number;
  dx: number;
  dy: number;
  size: number;
  color: string;
  delay: number;
}

/** A visual-only copy survives the immediate filter update for half a second. */
export function dissolveChip(chip: HTMLButtonElement): () => void {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches)
    return () => {};
  while (active.size >= MAX_ACTIVE) active.values().next().value?.();
  const rectangle = chip.getBoundingClientRect();
  if (!rectangle.width || !rectangle.height) return () => {};
  const padding = 48;
  const wrapper = document.createElement("div");
  wrapper.setAttribute("aria-hidden", "true");
  wrapper.inert = true;
  Object.assign(wrapper.style, {
    position: "fixed",
    left: `${rectangle.left}px`,
    top: `${rectangle.top}px`,
    width: `${rectangle.width}px`,
    height: `${rectangle.height}px`,
    pointerEvents: "none",
    zIndex: "110",
    overflow: "visible",
  });
  const clone = chip.cloneNode(true) as HTMLButtonElement;
  clone.removeAttribute("id");
  clone.removeAttribute("aria-label");
  clone.tabIndex = -1;
  clone.disabled = true;
  Object.assign(clone.style, {
    position: "absolute",
    inset: "0",
    width: `${rectangle.width}px`,
    height: `${rectangle.height}px`,
    margin: "0",
    transform: "none",
    maxWidth: "none",
    pointerEvents: "none",
    willChange: "filter, opacity",
    opacity: "1",
  });
  // A thresholded turbulence mask progressively removes the real chip pixels.
  // The separate dust layer then carries small fragments beyond its bounds.
  const namespace = "http://www.w3.org/2000/svg";
  const filterId = `chip-dust-${crypto.randomUUID()}`;
  const filterSvg = document.createElementNS(namespace, "svg");
  filterSvg.setAttribute("width", "0");
  filterSvg.setAttribute("height", "0");
  filterSvg.innerHTML = `<defs><filter id="${filterId}" x="-20%" y="-40%" width="140%" height="180%" color-interpolation-filters="sRGB"><feTurbulence type="fractalNoise" baseFrequency=".72" numOctaves="1" seed="7" result="noise"/><feColorMatrix in="noise" type="matrix" values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  1 0 0 0 0" result="grain"/><feComponentTransfer in="grain" result="threshold"><feFuncA type="linear" slope="12" intercept="1"/></feComponentTransfer><feComposite in="SourceGraphic" in2="threshold" operator="in" result="pieces"/><feDisplacementMap in="pieces" in2="noise" scale="0" xChannelSelector="R" yChannelSelector="G"/></filter></defs>`;
  const threshold = filterSvg.querySelector("feFuncA")!;
  const displacement = filterSvg.querySelector("feDisplacementMap")!;
  clone.style.filter = `url(#${filterId})`;
  const canvas = document.createElement("canvas");
  const width = Math.ceil(rectangle.width + padding * 2);
  const height = Math.ceil(rectangle.height + padding * 2);
  const ratio = Math.min(window.devicePixelRatio || 1, 2);
  canvas.width = width * ratio;
  canvas.height = height * ratio;
  Object.assign(canvas.style, {
    position: "absolute",
    left: `${-padding}px`,
    top: `${-padding}px`,
    width: `${width}px`,
    height: `${height}px`,
    pointerEvents: "none",
  });
  const context = canvas.getContext("2d");
  if (!context) return () => {};
  context.scale(ratio, ratio);
  const particles = chipParticles(chip, rectangle);
  wrapper.append(filterSvg, clone, canvas);
  document.body.append(wrapper);
  let frame = 0;
  let finished = false;
  const started = performance.now();
  function cleanUp() {
    if (finished) return;
    finished = true;
    cancelAnimationFrame(frame);
    wrapper.remove();
    active.delete(cleanUp);
  }
  active.add(cleanUp);
  function draw(now: number) {
    const progress = Math.min(1, (now - started) / DURATION);
    threshold.setAttribute("intercept", String(1 - progress * 10));
    displacement.setAttribute("scale", String(progress * 12));
    clone.style.opacity = String(
      Math.max(0, 1 - Math.max(0, progress - 0.25) / 0.6),
    );
    context!.clearRect(0, 0, width, height);
    for (const particle of particles) {
      const age = Math.max(
        0,
        (progress - particle.delay) / (1 - particle.delay),
      );
      if (!age || age >= 1) continue;
      const drift = 1 - (1 - age) ** 2;
      context!.globalAlpha =
        Math.sin(Math.PI * Math.min(1, age * 1.4)) * (1 - age);
      context!.fillStyle = particle.color;
      context!.fillRect(
        padding + particle.x + particle.dx * drift,
        padding +
          particle.y +
          particle.dy * drift -
          8 * Math.sin(age * Math.PI),
        particle.size * (1 - age * 0.65),
        particle.size * (1 - age * 0.65),
      );
    }
    context!.globalAlpha = 1;
    if (progress < 1) frame = requestAnimationFrame(draw);
    else cleanUp();
  }
  frame = requestAnimationFrame(draw);
  return cleanUp;
}

function chipParticles(
  chip: HTMLButtonElement,
  rectangle: DOMRect,
): Particle[] {
  // Rasterise the already visible text and same-origin icon, never remote media.
  const source = document.createElement("canvas");
  source.width = Math.ceil(rectangle.width);
  source.height = Math.ceil(rectangle.height);
  const context = source.getContext("2d");
  if (!context) return [];
  const chipStyle = getComputedStyle(chip);
  for (const text of chip.querySelectorAll("small, strong")) {
    const bounds = text.getBoundingClientRect();
    const style = getComputedStyle(text);
    context.fillStyle = style.color;
    context.font = `${style.fontWeight} ${style.fontSize} ${style.fontFamily}`;
    context.textBaseline = "middle";
    context.fillText(
      text.textContent || "",
      bounds.left - rectangle.left,
      bounds.top - rectangle.top + bounds.height / 2,
      bounds.width,
    );
  }
  const image = chip.querySelector("img");
  if (
    image?.complete &&
    image.naturalWidth &&
    new URL(image.currentSrc || image.src, location.href).origin ===
      location.origin
  ) {
    const bounds = image.getBoundingClientRect();
    try {
      context.drawImage(
        image,
        bounds.left - rectangle.left,
        bounds.top - rectangle.top,
        bounds.width,
        bounds.height,
      );
    } catch {
      /* The noise-masked clone still retains the original icon. */
    }
  }
  let pixels: Uint8ClampedArray;
  try {
    pixels = context.getImageData(0, 0, source.width, source.height).data;
  } catch {
    return [];
  }
  const particles: Particle[] = [];
  const random = (index: number) => {
    const value = Math.sin(index * 127.1 + 311.7) * 43758.5453;
    return value - Math.floor(value);
  };
  for (let y = 0; y < source.height; y += 2) {
    for (let x = 0; x < source.width; x += 2) {
      const index = (y * source.width + x) * 4;
      if (pixels[index + 3] < 45) continue;
      const seed = y * source.width + x;
      particles.push({
        x,
        y,
        dx: (random(seed) - 0.4) * 70,
        dy: (random(seed + 1) - 0.5) * 50,
        size: 0.7 + random(seed + 2) * 1.2,
        color: `rgb(${pixels[index]} ${pixels[index + 1]} ${pixels[index + 2]})`,
        delay: 0.02 + random(seed + 3) * 0.24,
      });
    }
  }
  // A few quiet fill fragments preserve the silhouette for chips without icons.
  for (let index = 0; index < 70; index++)
    particles.push({
      x: random(index + 4) * rectangle.width,
      y: random(index + 8) * rectangle.height,
      dx: (random(index + 12) - 0.4) * 60,
      dy: (random(index + 16) - 0.5) * 45,
      size: 1 + random(index + 20),
      color: chipStyle.backgroundColor,
      delay: random(index + 24) * 0.2,
    });
  if (particles.length <= MAX_PARTICLES) return particles;
  return Array.from(
    { length: MAX_PARTICLES },
    (_, index) =>
      particles[Math.floor((index * particles.length) / MAX_PARTICLES)],
  );
}

/** Cancel transient visual copies on unmount or a reduced-motion preference change. */
export function cancelChipDissolutions() {
  for (const cleanUp of active) cleanUp();
}
