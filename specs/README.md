# Specs

W01–W09 ship inside the agent snapshot. P01–P04 run in the Producers IO agency account.

| Id | Folder | QA has to prove |
| --- | --- | --- |
| W01 | `w01-speed-to-lead` | Text in under 60 seconds |
| W02 | `w02-appointment-reminders` | Confirmation, 24-hour, and 1-hour messages |
| W03 | `w03-no-show-recovery` | Stops when they rebook |
| W04 | `w04-long-term-nurture` | Monthly for 12 months, STOP ends it |
| W05 | `w05-post-sale-welcome` | Stops when the stage becomes Declined |
| W06 | `w06-care-package` | Exactly one kit |
| W07 | `w07-lapse-save` | Stops when the stage returns to Active |
| W08 | `w08-anniversary-birthday` | Fires on the date, once a year |
| W09 | `w09-referral-ask` | Skips Payment Missed |
| P01 | `p01-front-end-fulfillment` | Download in under 2 minutes, no mail |
| P02 | `p02-founder-upsell` | Stops when membership is bought |
| P03 | `p03-new-member-onboarding` | Welcome plus day 1, 3, and 7 |
| P04 | `p04-failed-payment` | Pause on day 8, not before |

Shared stage names and fields are in `data-model.md`. Message rules are in `rules.md`.
