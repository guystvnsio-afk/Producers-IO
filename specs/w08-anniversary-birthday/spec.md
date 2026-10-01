# W08 Anniversary and birthday

Account: snapshot.

## Trigger

Contact birthday is today, or policy_anniversary is today.

## What it does

One personal text on that date. Anniversaries also include the booking link for an annual review. The workflow does not send twice in the same year for the same reason.

## Channel

Client line. No email required. Do not say iMessage.

## Steps

1. If the trigger is the birthday, and a birthday message was already sent in the last 360 days, stop. Otherwise send: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. Happy birthday."
2. If the trigger is policy_anniversary, and an anniversary message was already sent in the last 360 days, stop. Otherwise send: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. It has been a year since we set this up. If you want a review, use {{custom_values.booking_url}}"
3. Do not mention a carrier or a premium. Do not say the policy is still in force.

## QA must prove

Set T07's birthday to today and run once. One message sends. A second run the same day does not. Set policy_anniversary to today on a different run and confirm the booking link is present.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
