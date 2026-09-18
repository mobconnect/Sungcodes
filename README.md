# Sungcodes

Sungcodes is a static, installable web application for discovering music-code collections and creating original lyric drafts.

## Features

- Live artist and code discovery from the repository
- Search by artist or file name
- Browser-only original lyrics studio
- Copy and download lyric drafts
- Local draft recovery with `localStorage`
- Installable Progressive Web App (PWA)
- Offline app shell after the first visit
- Responsive mobile and desktop interface
- Visible copyright disclosure, contribution rules and disclaimer

## Run locally

Serve the repository root with a static server. Service workers and install prompts require HTTPS or localhost.

```bash
python3 -m http.server 8000
```

Open <http://localhost:8000>.

## Publish

The `.github/workflows/deploy-pages.yml` workflow publishes the repository through GitHub Pages. In repository settings, select **Pages → GitHub Actions**. The expected URL is:

<https://mobconnect.github.io/Sungcodes/>

## Content and rights

Sungcodes may reference third-party songs, artists and lyrics. Only publish material you created or are authorised to share. The app does not host audio or provide a lyrics licence. Read [`TERMS.md`](TERMS.md) before contributing.

## Business details

- Business name: Jessica Bright
- ABN: 59 726 146 692
- Website: https://justbeyou.com.au
- Domain: justbeyou.com.au
