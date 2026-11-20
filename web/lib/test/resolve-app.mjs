// A module resolve hook for the node test runner, so a test can import an app
// route (app/api/**/route.ts) as Next would: "@/x" is web/x, and an import
// without an extension tries .ts, .tsx and /index.ts (.js for a package
// subpath such as next/server). Registered by the tests
// that need it with module.register(); the app itself never loads this.
const WEB = new URL("../../", import.meta.url);

export async function resolve(specifier, context, next) {
  const spec = specifier.startsWith("@/") ? new URL(specifier.slice(2), WEB).href : specifier;
  try {
    return await next(spec, context);
  } catch (e) {
    if (e?.code !== "ERR_MODULE_NOT_FOUND" && e?.code !== "ERR_UNSUPPORTED_DIR_IMPORT") throw e;
    // A package subpath with no exports map ("next/server") is a CommonJS file.
    const exts = !spec.startsWith(".") && !spec.startsWith("file:") && !spec.startsWith("/") ? [".js"] : [".ts", ".tsx", "/index.ts"];
    for (const ext of exts) {
      try {
        return await next(spec + ext, context);
      } catch {}
    }
    throw e;
  }
}
