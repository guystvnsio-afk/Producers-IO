Build a new workflow named "P02 Founder upsell follow-up". Start fresh. Do not edit a workflow that is already on the canvas.

Account: the Producers IO agency account, not a client sub-account.

Trigger: Tag front-end-buyer is added, and tag member is absent.

1. If tag member or tag founder is present, stop.
2. Day 0, day 2, day 5, and day 7: one SMS and one email pointing at membership_checkout_url. Say setup is waived because they already bought. Do not quote a second price in the text. The checkout page shows $97 while founder seats remain and $147 after.
3. Before each send, if tag member is present, stop.
4. Do not mention income, and do not promise a number of clients.

Channel: SMS and email. Agency account only.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
