# W03 No-show recovery

Account: snapshot.

## Trigger

Appointment status changes to no-show.

## What it does

Wait 15 minutes, text a rebook link, create a call task, follow up once at day 3, then move to Nurture if they still have no appointment.

## Channel

SMS and email only. Do not use the client line.

## Steps

1. Move the opportunity to No-Show.
2. Wait 15 minutes.
3. If the contact has an appointment in the future, stop.
4. Send SMS and email with booking_url. SMS shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. We missed each other. Pick another time here: {{custom_values.booking_url}}"
5. Create a call task due today titled "No-show follow-up".
6. Wait 3 days.
7. If the contact has an appointment in the future, stop.
8. Send one follow-up SMS and email with booking_url.
9. If there is still no future appointment, move the opportunity to Nurture.

## QA must prove

On T04, mark no-show and book a new appointment before the text. No rebook text sends, and the workflow stops.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
