Build a new workflow named "W04 Long-term nurture". Start fresh. Do not edit a workflow that is already on the canvas.

Account: Producers IO Master.

Trigger: Opportunity has been in stage Nurture for 7 days.

1. Wait until the opportunity has been in Nurture for 7 days. If it leaves Nurture, stop.
2. Send one value note. No pitch, no carrier, no rate. Invite them to book with booking_url only if they want to talk.
3. Repeat every 30 days, 12 times total, while the opportunity is still in Nurture.
4. If stage changes away from Nurture, stop.
SMS shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. A short note from me is on the way by email. If you would rather talk, use {{custom_values.booking_url}}"
Use a plain monthly topic list the builder can rotate: what to keep with household papers, who to call first, how to update a phone number, when to schedule a review. Do not invent savings or prices.

Channel: SMS and email only. Alternate channel by month if the builder requires one action per step, but never both on the same day. Do not use the client line.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
