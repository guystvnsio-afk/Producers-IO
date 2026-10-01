# P03 New member onboarding

Account: agency.

## Trigger

SaaS subscription becomes active for a new location.

## What it does

Welcome, an A2P checklist, a community invite, and setup nudges on day 1, day 3, and day 7.

## Channel

Email and SMS to the member. Agency account only.

## Steps

1. Add tag member. If the checkout already added tag founder, leave it. Do not try to count the 20 founder seats inside this workflow. The checkout owns that count.
2. Day 0 welcome with community_url.
3. Day 0 A2P checklist: what they submit, and that sending waits on approval. Do not promise an approval time.
4. Day 1 nudge: finish the business name and booking link in custom values.
5. Day 3 nudge: confirm the client line is connected and that lead workflows are still SMS and email only.
6. Day 7 nudge: send one internal test lead to their own form.
7. If the subscription is paused or payment-failed, stop later nudges.

## QA must prove

A test signup sends those touches. A separate snapshot test, not this workflow, proves the new location loaded the snapshot. This workflow must not be marked passed just because the emails sent.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
