# Software testing

Nothing is published because a workflow was built. It is published after two clean passes. A pass names the contact, the step, and the time. A fail names the step that broke.

## Gates

| Gate | Who | Pass |
| --- | --- | --- |
| 1. Specs | You | You have read the spec and the prompt for that batch |
| 2. Workflow QA | QA agent | Two passes in a row on test contacts, plus STOP and quiet hours |
| 3. Publish | You | You have seen the QA log and the canvas screenshot, then you publish |
| 4. Snapshot | You | A fresh test location has the fields, pipelines, calendar, and workflows |
| 5. Launch | You | Test-mode purchase, upsell, signup, and snapshot load all finish |

Use Stripe test mode. Do not run a live card. Do not enroll a real customer until gate 5.

## Test contacts

Create these only inside `Producers IO Master`. Details are in `specs/data-model.md`.

| Contact | Proves |
| --- | --- |
| T01 Form lead, created at 10:00 local | W01 text queued in under 60 seconds |
| T02 Meta lead | W01 also catches the Meta source and files the lead in New |
| T03 Appointment 26 hours out | W02 confirmation now, and the 24-hour step is scheduled |
| T03b Appointment 70 minutes out | W02 one-hour reminder |
| T04 No-show, then a new booking before the text | W03 stops |
| T05 Stage Nurture for 7 days | W04 sends the first monthly note and not a day-6 note |
| T06 Application Submitted, then Declined | W05 sends day 0 and sends nothing after the stage change |
| T07 First Payment Confirmed | W06 sends one webhook and one vault link |
| T08 Same contact moved into First Payment Confirmed again | W06 does not send a second kit |
| T09 Payment Missed, then Active before day 3 | W07 sends the same-day text and not the day-3 text |
| T10 Replies STOP to W01 | Tag `opted-out`, and no later message |

T03b is a second appointment on T03, not an eleventh person. Birthday and anniversary use T07 with those date fields set to today, then the workflow is triggered once. A second trigger the same day must not send again. W09 uses T07 at day 30, and a copy of T07 left in Payment Missed, which must get nothing.

## Quiet hours

Create a lead at 21:00 in the contact’s time zone. No SMS and no email leave before 08:00 local. The under-60-second proof is T01 at 10:00, not this one.

## Checkout

One Stripe test purchase of Chargeback Shield Kit at $37, with the $17 bump on, then the $97 membership. The thank-you page shows the download. No thanks.io request is created. Repeat once with the bump off. Repeat once declining the membership, and confirm P02 is running and then stops when the membership is bought.

P04: fail a renewal in test mode. Messages on day 0, day 2, day 5, and day 7. The location is still active on day 7. It pauses on day 8. A recovered payment on day 3 cancels the rest.

## Snapshot

Load the snapshot into a new test location. Read back fields, tags, three pipelines, the calendar, and W01–W09. Then archive that location. Do not reuse it as a member account.

## Kit and vault

Point the kit webhook at a test receiver. T07 produces one POST. T08 produces zero. The POST body matches `specs/kit-webhook.md`. The vault link in the message is the link for that contact, and it opens a page that shows the member’s name and the customer’s first name. No carrier, no premium.

## Records

QA writes `qa.md` in the workflow folder:

```
Pass 1: PASS — T01 — text queued in 22s
Pass 2: PASS — T01 — text queued in 18s
```

or

```
Pass 1: FAIL — T07 — second webhook fired on T08
```

Two fails in a row stop the batch. Fix that workflow only, then retest it twice. Do not republish the others.
