# W04 Long-term nurture

Account: snapshot.

## Trigger

Opportunity has been in stage Nurture for 7 days.

## What it does

One useful SMS or email each month for 12 months. No send before day 7.

## Channel

SMS and email only. Alternate channel by month if the builder requires one action per step, but never both on the same day. Do not use the client line.

## Steps

1. Wait until the opportunity has been in Nurture for 7 days. If it leaves Nurture, stop.
2. Send one value note. No pitch, no carrier, no rate. Invite them to book with booking_url only if they want to talk.
3. Repeat every 30 days, 12 times total, while the opportunity is still in Nurture.
4. If stage changes away from Nurture, stop.
SMS shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. A short note from me is on the way by email. If you would rather talk, use {{custom_values.booking_url}}"
Use a plain monthly topic list the builder can rotate: what to keep with household papers, who to call first, how to update a phone number, when to schedule a review. Do not invent savings or prices.

## QA must prove

T05 receives the first note on day 7 and does not receive one on day 6. A STOP reply ends the remaining months the same day.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
