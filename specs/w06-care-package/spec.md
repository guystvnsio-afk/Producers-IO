# W06 Care package

Account: snapshot.

## Trigger

Opportunity moves to First Payment Confirmed.

## What it does

One kit order, one billable kit, and one vault link. A second entry into this stage does nothing.

## Channel

Client line and email for the vault link. The kit itself is mail, via the webhook, to the contact's mailing address.

## Steps

1. If tag kit-sent is present, or kit_status is sent, stop.
2. Set first_payment_date to today if it is empty.
3. Set kit_status to queued. Do not add kit-sent yet.
4. POST this JSON to kit_webhook_url:
   {"contact_id":"{{contact.id}}","location_id":"{{location.id}}","product_line":"{{contact.product_line}}","to_name":"{{contact.full_name}}","street":"{{contact.mailing_street}}","city":"{{contact.mailing_city}}","state":"{{contact.mailing_state}}","zip":"{{contact.mailing_zip}}","agent_name":"{{custom_values.agent_display_name}}","business_name":"{{custom_values.business_name}}"}
   The receiver treats location_id plus contact_id as the idempotency key and will not mail twice.
5. If the webhook returns success, add tag kit-sent and set kit_status to sent.
6. If the webhook fails, set kit_status to failed, create a task "Retry care package", and do not add kit-sent. Do not loop.
7. Send vault_url by client line and by email. If vault_url is empty, create a task "Vault link missing" instead of sending a blank link.
Message shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. Your household sheet is on its way, and your page is here: {{contact.vault_url}}"

## QA must prove

T07 sends one POST and one vault message. T08, the same contact moved into the stage again, sends nothing.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
