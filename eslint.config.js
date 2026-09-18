import js from "@eslint/js";

export default [
  js.configs.recommended,
  {
    files: ["app.js", "enhancements.js"],
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
      globals: {
        window: "readonly", document: "readonly", localStorage: "readonly",
        navigator: "readonly", speechSynthesis: "readonly",
        SpeechSynthesisUtterance: "readonly", URL: "readonly", Blob: "readonly",
        setTimeout: "readonly", clearTimeout: "readonly", fetch: "readonly"
      }
    },
    rules: { "no-unused-vars": "warn", "no-console": "warn" }
  }
];
