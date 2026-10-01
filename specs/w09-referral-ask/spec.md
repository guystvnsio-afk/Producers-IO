# W09 Referral ask

Account: snapshot.

## Trigger

30 days after first_payment_date.

## What it does

One referral request with a simple share link. Skip anyone whose current stage is Payment Missed.

## Channel

Client line and email. Do not say iMessage.

## Steps

1. If the current stage is Payment Missed, stop.
2. If tag opted-out is present, stop.
3. Send one message. Shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. If someone you know wants the same kind of help, they can use this link: {{custom_values.booking_url}}"
4. Do not enroll this workflow a second time for the same contact.

## QA must prove

An Active T07 at day 30 gets one message. A copy of that contact left in Payment Missed gets none.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
