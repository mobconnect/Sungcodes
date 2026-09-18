import { readFile } from "node:fs/promises";
import { access } from "node:fs/promises";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import test from "node:test";
import assert from "node:assert/strict";

const exec = promisify(execFile);
const required = ["index.html", "styles.css", "app.js", "enhancements.js", "sw.js", "manifest.webmanifest", "data/library.json", "404.html", "robots.txt", "sitemap.xml"];

test("required production files exist", async () => {
  for (const file of required) await access(file);
});

test("library is valid JSON", async () => {
  const data = JSON.parse(await readFile("data/library.json", "utf8"));
  assert.ok(Array.isArray(data));
  assert.ok(data.every(song => song.title && song.artist && song.rights));
});

test("HTML and service worker reference the application shell", async () => {
  const html = await readFile("index.html", "utf8");
  const worker = await readFile("sw.js", "utf8");
  assert.match(html, /app\.js/);
  assert.match(html, /enhancements\.js/);
  assert.match(worker, /enhancements\.js/);
  assert.match(worker, /data\/library\.json/);
});

test("JavaScript has valid syntax", async () => {
  for (const file of ["app.js", "enhancements.js", "sw.js"]) await exec(process.execPath, ["--check", file]);
});
