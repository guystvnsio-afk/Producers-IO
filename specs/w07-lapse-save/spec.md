# W07 Lapse save

Account: snapshot.

## Trigger

Opportunity moves to Payment Missed.

## What it does

A same-day call task, a save text, then follow-ups at day 3 and day 7. Everything stops when the stage returns to Active.

## Channel

Client line and email. Do not say iMessage. Do not threaten cancellation and do not quote a premium.

## Steps

1. Create a call task due today titled "Payment missed".
2. Send a client-line message and email. Shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. I need to talk with you about your draft. You can reach me here or pick a time: {{custom_values.booking_url}}"
3. Wait 3 days. If stage is Active, stop.
4. Send one follow-up with booking_url.
5. Wait until day 7 from the trigger. If stage is Active, stop.
6. Send one last follow-up with booking_url.
7. Do not move the stage yourself. The agent moves it when the draft is resolved.

## QA must prove

T09 gets the same-day text. After the stage returns to Active, the day-3 message does not send.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
