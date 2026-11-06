import { describe, expect, it } from "vitest";
import {
  clippedViewerImage,
  renderedImageRect,
  viewerImageInFrame,
} from "@/features/capture-viewer-motion";

describe("capture viewer image geometry", () => {
  it("retains the currently visible section of a scrolled tall screenshot", () => {
    const image = { left: 100, top: -500, width: 800, height: 4000 };
    const stage = { left: 100, top: 100, width: 800, height: 600 };
    const projection = clippedViewerImage(image, stage);
    expect(projection.frame).toEqual(stage);
    expect(projection.image).toEqual({
      left: 0,
      top: -600,
      width: 800,
      height: 4000,
    });
    // The first closing frame paints exactly the original document position.
    expect(projection.frame.top + projection.image.top).toBe(image.top);
    expect(projection.image.height).toBe(image.height);
  });

  it("preserves a centered contained icon inside the larger thumbnail frame", () => {
    const frame = { left: 50, top: 80, width: 300, height: 200 };
    const rendered = renderedImageRect(
      frame,
      { width: 64, height: 64 },
      "contain",
      "50% 50%",
    );
    const projection = viewerImageInFrame(rendered, frame);
    expect(projection.frame).toEqual(frame);
    expect(projection.image).toEqual({
      left: 50,
      top: 0,
      width: 200,
      height: 200,
    });
    expect(projection.frame.left + projection.image.left).toBe(100);
    // The icon stays square with its original side gutters.
    expect(projection.image.width).toBe(projection.image.height);
  });

  it("preserves centered cover cropping and non-default object positions", () => {
    const frame = { left: 10, top: 20, width: 200, height: 100 };
    const tall = renderedImageRect(
      frame,
      { width: 200, height: 400 },
      "cover",
      "50% 50%",
    );
    expect(viewerImageInFrame(tall, frame).image).toEqual({
      left: 0,
      top: -150,
      width: 200,
      height: 400,
    });
    expect(
      renderedImageRect(
        frame,
        { width: 64, height: 64 },
        "contain",
        "right bottom",
      ),
    ).toEqual({
      left: 110,
      top: 20,
      width: 100,
      height: 100,
    });
  });
});
