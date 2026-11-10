# Privacy

## On the website today

- No form sends data. No cookies are set. No analytics or third-party trackers are used.
- The only values in the browser's `localStorage` are the language choice (`saathi.lang`) and the light-version choice (`saathi.lite`). Neither is personal.
- The demo workspace keeps invented records in memory and forgets them when the tab closes.
- Web fonts load from Google Fonts unless the light version is on. This shares the visitor's IP address with Google. Consider self-hosting fonts before launch.
- The quick-exit button leaves the site but cannot erase browser history. The site says so.

## For a live service

- Collect the least data needed, and say why at the point of asking.
- Consent is specific, in the person's language, recorded with version and time (IST), and withdrawable.
- Children under 18: verifiable parental consent under the DPDP Act 2023, with safeguards where the family is the concern. See `docs/safeguarding.md`.
- Host in India. Encrypt at rest and in transit. Log access.
- Do not tell anyone that a message is "completely confidential". Explain the limits, including mandatory reporting.
- Messages on shared phones: neutral sender names and wording, opt-in for each channel.
- Publish a short privacy notice in plain language in every supported language, and a grievance route.
- Retention and deletion schedules agreed before launch.
