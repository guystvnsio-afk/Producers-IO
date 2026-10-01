Build a new workflow named "W03 No-show recovery". Start fresh. Do not edit a workflow that is already on the canvas.

Account: Producers IO Master.

Trigger: Appointment status changes to no-show.

1. Move the opportunity to No-Show.
2. Wait 15 minutes.
3. If the contact has an appointment in the future, stop.
4. Send SMS and email with booking_url. SMS shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. We missed each other. Pick another time here: {{custom_values.booking_url}}"
5. Create a call task due today titled "No-show follow-up".
6. Wait 3 days.
7. If the contact has an appointment in the future, stop.
8. Send one follow-up SMS and email with booking_url.
9. If there is still no future appointment, move the opportunity to Nurture.

Channel: SMS and email only. Do not use the client line.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
