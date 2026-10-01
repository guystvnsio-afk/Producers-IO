# W01 Speed-to-lead

Account: snapshot.

## Trigger

Contact created from the lead form, or from a Meta lead ad.

## What it does

Text and email within 60 seconds, a call task for today, and the opportunity in stage New.

## Channel

SMS and email only. Do not use the client line.

## Steps

1. Add tag src-form for a form submission, or src-meta for a Meta lead.
2. Create an opportunity. Pipeline is FEX, IUL, or Retirement from product_line. If product_line is empty, use FEX and add tag needs-product-line. Stage is New.
3. Send SMS: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. I got your note and I will call you today. If you want to pick a time instead, use {{custom_values.booking_url}}."
4. Send the same meaning by email, with the booking link as a button whose URL is the custom value.
5. Create a call task for the assigned user, due today, titled "Call new lead".

## QA must prove

T01, created at 10:00 America/Chicago, has an SMS queued in under 60 seconds. T02 lands in the IUL pipeline at New with tag src-meta.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
