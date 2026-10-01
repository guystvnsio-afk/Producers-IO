Build a new workflow named "P03 New member onboarding". Start fresh. Do not edit a workflow that is already on the canvas.

Account: the Producers IO agency account, not a client sub-account.

Trigger: SaaS subscription becomes active for a new location.

1. Add tag member. If the checkout already added tag founder, leave it. Do not try to count the 20 founder seats inside this workflow. The checkout owns that count.
2. Day 0 welcome with community_url.
3. Day 0 A2P checklist: what they submit, and that sending waits on approval. Do not promise an approval time.
4. Day 1 nudge: finish the business name and booking link in custom values.
5. Day 3 nudge: confirm the client line is connected and that lead workflows are still SMS and email only.
6. Day 7 nudge: send one internal test lead to their own form.
7. If the subscription is paused or payment-failed, stop later nudges.

Channel: Email and SMS to the member. Agency account only.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
