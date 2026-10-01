Build a new workflow named "P01 Front-end fulfillment". Start fresh. Do not edit a workflow that is already on the canvas.

Account: the Producers IO agency account, not a client sub-account.

Trigger: Successful payment for Chargeback Shield Kit ($37), 30 Rejection-Safe Ads ($47), Referral Porch ($27), Month-2 Script ($17), or Fridge Sheet ($27), in the Producers IO agency account.

1. Add tag front-end-buyer and tag setup-waived.
2. Send the download link that matches the product that was just bought. One product, one link. Do not send the other four.
3. Enroll the buyer in P02 if they do not have tag member.
4. Do not call the kit webhook. Do not create a thanks.io order.

Channel: SMS and email. This workflow is not in the agent snapshot.

Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.

When you finish, stop. Leave it unpublished. The human will publish after QA.
