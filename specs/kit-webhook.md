# Kit webhook

W06 sends one POST. The handler orders the mail. The workflow does not talk to thanks.io itself.

## When

Stage becomes First Payment Confirmed, and the contact does not have `kit-sent`.

## Request

`POST` to `{{custom_values.kit_webhook_url}}`

```json
{
  "contact_id": "{{contact.id}}",
  "location_id": "{{location.id}}",
  "product_line": "{{contact.product_line}}",
  "to_name": "{{contact.full_name}}",
  "street": "{{contact.mailing_street}}",
  "city": "{{contact.mailing_city}}",
  "state": "{{contact.mailing_state}}",
  "zip": "{{contact.mailing_zip}}",
  "agent_name": "{{custom_values.agent_display_name}}",
  "business_name": "{{custom_values.business_name}}"
}
```

Use the builder’s real tokens if these placeholders differ.

## Handler rules

- The recipient is the contact. That person is the member’s customer, not the member.
- Idempotency key is `location_id` plus `contact_id`. A second POST returns the first order and does not mail again.
- The workflow adds `kit-sent` only after this handler returns success. The handler also sets `kit-sent` and `kit_status` to `sent`, so a retried workflow stops.
- Order a 2-page windowless letter and one 6x9 MagnaCard. Page 1 is the welcome. Page 2 is the family sheet. Copy outline is `specs/care-package-copy.md`.
- On success, set `kit_order_id`, set `kit_status` to `sent`, and keep the tag `kit-sent`.
- On failure, set `kit_status` to `failed` and do not add a second tag. Alert the location user. Do not retry in a loop inside W06.
- Store the thanks.io cost on the order so the monthly invoice can charge 2×.

## QA

T07 produces one POST. T08 produces no second order. The test receiver never calls the live thanks.io account.
