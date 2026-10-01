# W02 Appointment reminders

Account: snapshot.

## Trigger

Appointment booked on the Protection Review calendar.

## What it does

Confirmation now, a reminder 24 hours before, and a reminder 1 hour before. Each includes the reschedule link.

## Channel

SMS and email only. Do not use the client line. This workflow is the only reminder. Calendar notifications stay off.

## Steps

1. Move the opportunity to Appointment Set.
2. Send confirmation SMS and email now. Include reschedule_url.
3. Wait until 24 hours before the appointment start.
4. If the appointment is cancelled, stop.
5. Send the 24-hour SMS and email with reschedule_url.
6. Wait until 1 hour before the appointment start.
7. If the appointment is cancelled, stop.
8. Send the 1-hour SMS and email with reschedule_url.
SMS shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. Your review is on {{appointment.start_time}}. Need a different time? {{custom_values.reschedule_url}}"

## QA must prove

T03 booked 26 hours out gets the confirmation immediately and shows a wait until 24 hours before the start. A second appointment 70 minutes out sends the 1-hour reminder and not a second confirmation from a different workflow.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
