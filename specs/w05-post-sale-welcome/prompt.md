Build a new workflow named "W05 Post-sale welcome". Start fresh. Do not edit a workflow that is already on the canvas.

Account: Producers IO Master.

Trigger: Opportunity moves to Application Submitted.

1. Day 0. Client-line message and email: thank them, and say {{custom_values.agent_display_name}} will be the person who follows up. No coverage claim.
2. Day 1. What happens next: the agent will confirm details and the next date to remember. If draft_date is empty, say the agent will confirm the date, and do not invent one.
3. If draft_date is set, wait until the day before draft_date and send a reminder of that date. If draft_date is empty, send one reminder on day 7 that the agent still needs to confirm the date.
4. Day 14. Create a call task titled "Application check-in".
5. Day 30. One check-in message offering booking_url.
6. Before every send, if the stage is Declined, stop.

Channel: Client line and email. SMS fallback is the vendor's. Do not say iMessage.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
