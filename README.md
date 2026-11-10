# SAATHI

A space to feel heard. A pathway to feel supported.

SAATHI is a psychosocial wellbeing and support platform for women, adolescent girls and children, built for use in India: Indian languages, Indian services and helplines, Indian law, and the realities of family, school, work and shared phones. This repository contains the public SAATHI website, built for use in India. It runs on GitHub Pages with no server.

Nothing on the site sends or stores personal information. No referral service is live yet.

## What works today

| Feature | Working now | Demo data only | Needs external configuration |
| --- | --- | --- | --- |
| Design system, navigation, quick exit, light version | Yes | | |
| Language switching (English, Hindi, Bengali, Maithili, Bhojpuri interface strings) | Yes (menus and buttons; full content in progress) | | |
| Age pathways, resource library, safety pages, FAQs | Yes (awaiting expert review) | | |
| Find support and helplines | Helplines work | | Local services need verified partners |
| Connect with a person | Form is a preview only | | Secure backend, WhatsApp and SMS channels, trained staff |
| Professional workspace (`dashboard.html`) | Runs in the browser | All records are invented | Sign-in, encrypted storage in India, audit trail |
| Contact email | | | Set `contact_email` in `tools/layout.py` |
| Custom domain | | | DNS and GitHub Pages settings |

## Quick start

Open `index.html` in a browser, or run `python3 -m http.server` in this folder and visit http://localhost:8000.

## Edit and rebuild

Pages are generated from Python so the header, footer and safety links stay identical everywhere.

1. Edit content in `tools/content_*.py`, page code in `tools/pages/*.py`, or interface translations in `locales/*.json`.
2. Run `python3 tools/build.py`.
3. Run `python3 tests/check_site.py` to check links, headings, labels and the quick-exit link.
4. Commit the generated `.html` files along with your changes.

## Publish on GitHub Pages

Option A: deploy from a branch.

1. Create a new repository on GitHub and upload the contents of this folder (keep the `.nojekyll` file).
2. Open Settings, then Pages.
3. Under "Build and deployment", choose "Deploy from a branch", select `main` and `/ (root)`, and save.
4. After a minute or two the site is live at `https://<your-username>.github.io/<repository-name>/`.

Option B: the included GitHub Actions workflow.

1. In Settings, then Pages, set "Source" to "GitHub Actions".
2. Push to `main`. `.github/workflows/pages.yml` builds the site, runs the checks and deploys it. You can also start it by hand from the Actions tab.

Custom domain: add it under Settings, then Pages, then create the DNS records GitHub describes. Turn on "Enforce HTTPS". Every link on the site is relative, so it works on a project path or a custom domain.

## Before going public

- Have a qualified professional review all content, and native speakers review every translation.
- Re-verify every helpline in `tools/layout.py` (`HELPLINES`) against official sources. See `docs/helplines.md`.
- Add real photography only with informed consent.
- Set a monitored contact email in `SITE` in `tools/layout.py`.
- Get legal review under the Digital Personal Data Protection Act 2023 and the POCSO Act 2012, and agree the open decisions in `docs/safeguarding.md`.

## Folder structure

```
index.html, *.html        Generated pages (do not edit by hand)
assets/css, js, img       Styles, scripts, icons
tools/build.py            Site generator
tools/layout.py           Header, footer, helplines, SITE settings
tools/content_*.py        Written content (pathways, resources)
tools/pages/*.py          One module per group of pages
locales/*.json            Interface translations
docs/                     Architecture, safeguarding, privacy, content, helplines
tests/check_site.py       Link, heading and accessibility checks
.github/workflows/        GitHub Pages deployment
```

## Licence

Code: MIT (see `LICENSE`). Written content is © the SAATHI team, all rights reserved, until a content licence is chosen.
