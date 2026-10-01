Build a new workflow named "P04 Failed payment". Start fresh. Do not edit a workflow that is already on the canvas.

Account: the Producers IO agency account, not a client sub-account.

Trigger: Membership payment fails.

1. Add tag payment-failed.
2. Day 0, day 2, day 5, and day 7: ask them to update the card. Include the billing link from the SaaS settings, as a custom value, not a hardcoded URL.
3. Before each send, if the latest invoice is paid, remove payment-failed and stop.
4. On day 8, if it is still unpaid, pause the sub-account and add tag paused. Do not delete the location.
5. Do not pause on day 0, day 2, day 5, or day 7.

Channel: SMS and email to the member. Agency account only.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
