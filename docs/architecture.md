# Architecture

This page describes the live system SAATHI would need, and how the current static website maps to it. The website stores and sends nothing.

## Proposed stack

- Frontend: the existing static site, progressively enhanced. Mobile-first, works on low-end phones and slow data.
- API: a small service (for example Python or Node) behind HTTPS, with role-based access.
- Database: PostgreSQL, encrypted at rest.
- Object storage: encrypted, for any attachments, with short-lived access links.
- Queue and worker: for notifications and reminders.
- Messaging: WhatsApp Business API, SMS, and email, each with opt-in.
- Identity: email or phone sign-in with multi-factor authentication for professionals. No sign-in is needed for public pages.

## Data residency (India)

Personal data of people in India is hosted in India cloud regions. This supports compliance with the Digital Personal Data Protection Act 2023 and lets us name the legal basis plainly in the consent text. Backups stay in India. Any processor outside India needs legal review first.

## Messaging

SMS in India uses DLT-registered senders and templates under TRAI rules. Each template (reminder, OTP, follow-up) is registered before use. WhatsApp uses approved templates and requires opt-in. Messages never include a person's concern in the text. Example: "You have an appointment on 12/11/2026 at 4:30 pm IST." Nothing more.

## Data model (outline)

- `person`: pseudonymous ID, age band, state, district, preferred language, preferred channel.
- `consent`: person, version, timestamp (IST), purposes, guardian consent reference for under-18s, withdrawn_at.
- `referral`: case ID (SA-YYYY-NNNN), received_at, channel, short summary, priority (set by a human), status, assigned professional.
- `professional`: role, languages, organisation, verification record.
- `organisation` and `service`: verified partner record, last checked date, review owner.
- `appointment`, `follow_up`: linked to referral.
- `note`: author, time, referral. Access is logged.
- `safeguarding_flag`: type (for example POCSO mandatory report), raised by, time, outcome.
- `audit_event`: actor, action, object, time. Append only.

## API map (outline)

| Area | Endpoints |
| --- | --- |
| Public | `GET /resources`, `GET /pathways`, `GET /services` (verified only) |
| Requests | `POST /requests` (with consent), `GET /requests/{id}/status` (token) |
| Workspace | `GET /referrals`, `GET /referrals/{id}`, `PATCH /referrals/{id}` (priority, status, assignee), `POST /referrals/{id}/notes` |
| Scheduling | `POST /appointments`, `PATCH /follow-ups/{id}` |
| Safeguarding | `POST /referrals/{id}/flags` |
| Admin | `GET /audit`, `POST /services` and verification, `GET /reports` (aggregate counts only) |

## Security

- Encryption in transit (TLS) and at rest. Secrets in a managed vault.
- Least-privilege roles: reviewer, professional, safeguarding lead, administrator.
- Multi-factor authentication for every professional account.
- Append-only audit log of reads and writes of case data.
- Retention schedule with deletion on request, and on withdrawal of consent where the law allows.
- Penetration test and a data protection impact assessment before launch.
- Priority and escalation are always set by people. No automated triage or diagnosis.

## How the static website maps to this

| Prototype | Live system |
| --- | --- |
| Static pages on GitHub Pages | Same pages, served alongside the API |
| Connect form (preview, sends nothing) | `POST /requests` with consent record |
| `dashboard.html` with invented records in memory | Workspace backed by the database with sign-in |
| Audit log list in the demo | `audit_event` table |
| Directory with "No verified services yet" | `service` records with verification and review dates |
| Helplines in `tools/layout.py` | Same, plus a re-verification schedule (`docs/helplines.md`) |
