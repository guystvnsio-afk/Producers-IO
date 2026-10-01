Build a new workflow named "W07 Lapse save". Start fresh. Do not edit a workflow that is already on the canvas.

Account: Producers IO Master.

Trigger: Opportunity moves to Payment Missed.

1. Create a call task due today titled "Payment missed".
2. Send a client-line message and email. Shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. I need to talk with you about your draft. You can reach me here or pick a time: {{custom_values.booking_url}}"
3. Wait 3 days. If stage is Active, stop.
4. Send one follow-up with booking_url.
5. Wait until day 7 from the trigger. If stage is Active, stop.
6. Send one last follow-up with booking_url.
7. Do not move the stage yourself. The agent moves it when the draft is resolved.

Channel: Client line and email. Do not say iMessage. Do not threaten cancellation and do not quote a premium.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
