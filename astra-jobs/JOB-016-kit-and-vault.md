# JOB-016 Kit webhook and vault page

Status: BLOCKED. Do not paste until W06 is published and the snapshot has loaded in a fresh test location.

This is the extended software build. It does not belong in a workflow-builder paste.

## Build

1. A receiver for the POST body in `specs/kit-webhook.md`.
2. Idempotency on `location_id` plus `contact_id`, so a second call does not mail a second kit.
3. A thanks.io test-mode or draft order for one 2-page windowless letter and one 6x9 MagnaCard, to the contact’s address. Do not place a live order unless Guy has funded thanks.io and said to.
4. A vault page that shows `business_name`, the customer’s first name, and the agent phone from the location. No carrier, no premium, no Medicare.
5. Write that page’s URL back to `vault_url` on the contact.

Copy for the letter and magnet is the outline in `specs/care-package-copy.md`. Do not add a product pitch.

## Done

T07 against the test receiver: one order attempt, one vault URL. T08: no second order. Screenshot or log of both requests, and a line `PASS` or `FAIL`.

The recipient is the member’s customer. Do not mail Guy and do not mail the member.
