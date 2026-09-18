import test from "node:test";
import assert from "node:assert/strict";

const checks = [
  ["Search control exists", /id=["']search["']/],
  ["Creator lyrics control exists", /id=["']creatorLyrics["']/],
  ["PWA manifest is linked", /manifest\.webmanifest/],
  ["Canonical URL exists", /canonical/],
  ["Open Graph metadata exists", /og:title/]
];

test("Sungcodes smoke checks", async () => {
  const html = await (await fetch("file:///dev/null").catch(() => null)) || null;
  assert.ok(html === null || html);
  const fs = await import("node:fs/promises");
  const source = await fs.readFile("index.html", "utf8");
  for (const [name, pattern] of checks) assert.match(source, pattern, name);
});
