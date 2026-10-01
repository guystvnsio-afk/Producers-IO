# P02 Founder upsell follow-up

Account: agency.

## Trigger

Tag front-end-buyer is added, and tag member is absent.

## What it does

A 7-day sequence to the single membership checkout. It stops the moment membership is purchased.

## Channel

SMS and email. Agency account only.

## Steps

1. If tag member or tag founder is present, stop.
2. Day 0, day 2, day 5, and day 7: one SMS and one email pointing at membership_checkout_url. Say setup is waived because they already bought. Do not quote a second price in the text. The checkout page shows $97 while founder seats remain and $147 after.
3. Before each send, if tag member is present, stop.
4. Do not mention income, and do not promise a number of clients.

## QA must prove

A buyer who does not take the one-time offer gets day-0 and day-2 messages. Adding tag member on day 3 stops day 5 and day 7.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
