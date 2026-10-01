Build a new workflow named "W09 Referral ask". Start fresh. Do not edit a workflow that is already on the canvas.

Account: Producers IO Master.

Trigger: 30 days after first_payment_date.

1. If the current stage is Payment Missed, stop.
2. If tag opted-out is present, stop.
3. Send one message. Shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. If someone you know wants the same kind of help, they can use this link: {{custom_values.booking_url}}"
4. Do not enroll this workflow a second time for the same contact.

Channel: Client line and email. Do not say iMessage.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
