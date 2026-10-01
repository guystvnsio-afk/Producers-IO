# P04 Failed payment

Account: agency.

## Trigger

Membership payment fails.

## What it does

Dunning messages across 7 days. The account pauses on day 8, not before. A successful payment stops the sequence.

## Channel

SMS and email to the member. Agency account only.

## Steps

1. Add tag payment-failed.
2. Day 0, day 2, day 5, and day 7: ask them to update the card. Include the billing link from the SaaS settings, as a custom value, not a hardcoded URL.
3. Before each send, if the latest invoice is paid, remove payment-failed and stop.
4. On day 8, if it is still unpaid, pause the sub-account and add tag paused. Do not delete the location.
5. Do not pause on day 0, day 2, day 5, or day 7.

## QA must prove

A failed test renewal sends day 0. The location is still active at the end of day 7. It pauses on day 8. A recovered payment on day 3 sends nothing further and does not pause.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
