# W05 Post-sale welcome

Account: snapshot.

## Trigger

Opportunity moves to Application Submitted.

## What it does

A 30-day sequence: thank-you, what happens next, a draft-date reminder, and a check-in call task. The sequence stops if the stage becomes Declined.

## Channel

Client line and email. SMS fallback is the vendor's. Do not say iMessage.

## Steps

1. Day 0. Client-line message and email: thank them, and say {{custom_values.agent_display_name}} will be the person who follows up. No coverage claim.
2. Day 1. What happens next: the agent will confirm details and the next date to remember. If draft_date is empty, say the agent will confirm the date, and do not invent one.
3. If draft_date is set, wait until the day before draft_date and send a reminder of that date. If draft_date is empty, send one reminder on day 7 that the agent still needs to confirm the date.
4. Day 14. Create a call task titled "Application check-in".
5. Day 30. One check-in message offering booking_url.
6. Before every send, if the stage is Declined, stop.

## QA must prove

T06 gets the day-0 thank-you. After the stage moves to Declined, no later step sends.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
