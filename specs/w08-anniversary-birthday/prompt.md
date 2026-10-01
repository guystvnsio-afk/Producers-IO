Build a new workflow named "W08 Anniversary and birthday". Start fresh. Do not edit a workflow that is already on the canvas.

Account: Producers IO Master.

Trigger: Contact birthday is today, or policy_anniversary is today.

1. If the trigger is the birthday, and a birthday message was already sent in the last 360 days, stop. Otherwise send: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. Happy birthday."
2. If the trigger is policy_anniversary, and an anniversary message was already sent in the last 360 days, stop. Otherwise send: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. It has been a year since we set this up. If you want a review, use {{custom_values.booking_url}}"
3. Do not mention a carrier or a premium. Do not say the policy is still in force.

Channel: Client line. No email required. Do not say iMessage.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
