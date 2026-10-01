Build a new workflow named "W02 Appointment reminders". Start fresh. Do not edit a workflow that is already on the canvas.

Account: Producers IO Master.

Trigger: Appointment booked on the Protection Review calendar.

1. Move the opportunity to Appointment Set.
2. Send confirmation SMS and email now. Include reschedule_url.
3. Wait until 24 hours before the appointment start.
4. If the appointment is cancelled, stop.
5. Send the 24-hour SMS and email with reschedule_url.
6. Wait until 1 hour before the appointment start.
7. If the appointment is cancelled, stop.
8. Send the 1-hour SMS and email with reschedule_url.
SMS shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. Your review is on {{appointment.start_time}}. Need a different time? {{custom_values.reschedule_url}}"

Channel: SMS and email only. Do not use the client line. This workflow is the only reminder. Calendar notifications stay off.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
