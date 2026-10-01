Build a new workflow named "W01 Speed-to-lead". Start fresh. Do not edit a workflow that is already on the canvas.

Account: Producers IO Master.

Trigger: Contact created from the lead form, or from a Meta lead ad.

1. Add tag src-form for a form submission, or src-meta for a Meta lead.
2. Create an opportunity. Pipeline is FEX, IUL, or Retirement from product_line. If product_line is empty, use FEX and add tag needs-product-line. Stage is New.
3. Send SMS: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. I got your note and I will call you today. If you want to pick a time instead, use {{custom_values.booking_url}}."
4. Send the same meaning by email, with the booking link as a button whose URL is the custom value.
5. Create a call task for the assigned user, due today, titled "Call new lead".

Channel: SMS and email only. Do not use the client line.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
