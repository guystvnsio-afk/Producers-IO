# Data model

Build this in `Producers IO Master` only. Names below are the source of truth. If HighLevel already has a standard birthday field, use it and do not create a second one.

## Pipelines

Three pipelines, same stages, in this order:

1. FEX
2. IUL
3. Retirement

Stages:

1. New
2. Contacted
3. Appointment Set
4. No-Show
5. Nurture
6. Application Submitted
7. Declined
8. First Payment Confirmed
9. Active
10. Payment Missed

`product_line` picks the pipeline. If it is empty, use FEX and add the tag `needs-product-line`.

## Calendar

One calendar, named `Protection Review`.

- 30-minute slots
- 15-minute buffer
- Monday to Friday, 09:00–18:00 in the location time zone
- HighLevel’s own reminder texts and emails off. W02 is the only reminder sender

## Contact fields

| Field | Type | Use |
| --- | --- | --- |
| `product_line` | dropdown: FEX, IUL, Retirement | Which pipeline |
| `draft_date` | date | W05 reminder |
| `policy_anniversary` | date | W08 |
| `first_payment_date` | date | Set when the deal first hits First Payment Confirmed. W09 reads it |
| `kit_status` | dropdown: none, queued, sent, failed | Mail state |
| `kit_order_id` | text | thanks.io id, written by the webhook handler |
| `vault_url` | text | One link per customer |
| `mailing_street` | text | Kit address. Use standard address fields if they already exist |
| `mailing_city` | text | Kit address |
| `mailing_state` | text | Kit address |
| `mailing_zip` | text | Kit address |

Birthday uses the standard contact birthday field.

## Agency custom values

These live on the Producers IO agency account, not inside a member location.

| Value | Use |
| --- | --- |
| `founder_seats_remaining` | Starts at 20. The checkout decrements it when a founder seat is sold. Workflows do not do this math |
| `membership_checkout_url` | Same checkout for every front end |
| `community_url` | Invite used by P03 |

## Location custom values

| Value | Use |
| --- | --- |
| `agent_display_name` | How the agent signs texts |
| `business_name` | Letter and magnet |
| `booking_url` | Protection Review link |
| `reschedule_url` | Reschedule link |
| `kit_webhook_url` | Test receiver, then the live kit endpoint |

Phone numbers come from the location’s HighLevel number and the Blooio line selected on the conversation action. Do not store a raw number inside a message.

## Tags

`src-form`, `src-meta`, `needs-product-line`, `opted-out`, `kit-sent`, `front-end-buyer`, `founder`, `member`, `setup-waived`, `payment-failed`, `paused`.

## Test contacts

All of them use a phone and email you control. Time zone America/Chicago unless a test says otherwise.

| Id | Name | Product | Starting point |
| --- | --- | --- | --- |
| T01 | Test Form | FEX | Empty. Submit the lead form at 10:00 local |
| T02 | Test Meta | IUL | Empty. Submit the Meta test lead |
| T03 | Test Booked | FEX | Stage Contacted. Book Protection Review |
| T04 | Test Noshow | Retirement | Appointment marked no-show |
| T05 | Test Nurture | FEX | Stage Nurture, entered 7 days ago |
| T06 | Test App | IUL | Move to Application Submitted during the test |
| T07 | Test Paid | FEX | Has mailing address, birthday, and anniversary. Move to First Payment Confirmed |
| T08 | Test Paid | FEX | Same person as T07, second stage move |
| T09 | Test Lapse | Retirement | Move to Payment Missed, then back to Active |
| T10 | Test Stop | FEX | Lead form, then reply STOP |

T08 is not a new person.
