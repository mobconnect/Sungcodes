# Deployment recommendations

## Recommended hosting

Sungcodes is a static GitHub Pages site. Keep the frontend on **GitHub Pages** with the existing Pages Actions workflow.

If server-side Gemini generation is added, host that API separately on **Google Cloud Run** (recommended), **Render**, **Railway**, **Fly.io**, or a managed serverless function. Keep `GEMINI_API_KEY` only in the backend environment; never expose it in this static site.

## Checks

```bash
# Static site: deploy the repository root with path: .
# Verify Pages source is GitHub Actions and enforce HTTPS.
```

Do not run an Express server inside GitHub Pages.
