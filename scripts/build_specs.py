#!/usr/bin/env python3
"""Write workflow specs, paste prompts, and blocked Astra jobs."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RULES = """
Rules:
- Send only between 08:00 and 20:00 in the contact's time zone. Hold other sends until 08:00 local.
- If the contact has tag opted-out, or replies STOP, UNSUBSCRIBE, CANCEL, QUIT, or END, stop this workflow and add tag opted-out.
- Pick agent_display_name, business_name, booking_url, reschedule_url, and kit_webhook_url from custom values. Do not type a name, phone number, or URL into the message.
- Do not mention a carrier, a policy price, an age, Medicare, or a promised result.
- Do not write the word iMessage.
- Do not publish. Leave the workflow in draft.
""".strip()

WORKFLOWS = [
    {
        "id": "W01",
        "slug": "w01-speed-to-lead",
        "name": "Speed-to-lead",
        "where": "snapshot",
        "trigger": "Contact created from the lead form, or from a Meta lead ad.",
        "goal": "Text and email within 60 seconds, a call task for today, and the opportunity in stage New.",
        "qa": "T01, created at 10:00 America/Chicago, has an SMS queued in under 60 seconds. T02 lands in the IUL pipeline at New with tag src-meta.",
        "channel": "SMS and email only. Do not use the client line.",
        "steps": """
1. Add tag src-form for a form submission, or src-meta for a Meta lead.
2. Create an opportunity. Pipeline is FEX, IUL, or Retirement from product_line. If product_line is empty, use FEX and add tag needs-product-line. Stage is New.
3. Send SMS: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. I got your note and I will call you today. If you want to pick a time instead, use {{custom_values.booking_url}}."
4. Send the same meaning by email, with the booking link as a button whose URL is the custom value.
5. Create a call task for the assigned user, due today, titled "Call new lead".
""".strip(),
    },
    {
        "id": "W02",
        "slug": "w02-appointment-reminders",
        "name": "Appointment reminders",
        "where": "snapshot",
        "trigger": "Appointment booked on the Protection Review calendar.",
        "goal": "Confirmation now, a reminder 24 hours before, and a reminder 1 hour before. Each includes the reschedule link.",
        "qa": "T03 booked 26 hours out gets the confirmation immediately and shows a wait until 24 hours before the start. A second appointment 70 minutes out sends the 1-hour reminder and not a second confirmation from a different workflow.",
        "channel": "SMS and email only. Do not use the client line. This workflow is the only reminder. Calendar notifications stay off.",
        "steps": """
1. Move the opportunity to Appointment Set.
2. Send confirmation SMS and email now. Include reschedule_url.
3. Wait until 24 hours before the appointment start.
4. If the appointment is cancelled, stop.
5. Send the 24-hour SMS and email with reschedule_url.
6. Wait until 1 hour before the appointment start.
7. If the appointment is cancelled, stop.
8. Send the 1-hour SMS and email with reschedule_url.
SMS shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. Your review is on {{appointment.start_time}}. Need a different time? {{custom_values.reschedule_url}}"
""".strip(),
    },
    {
        "id": "W03",
        "slug": "w03-no-show-recovery",
        "name": "No-show recovery",
        "where": "snapshot",
        "trigger": "Appointment status changes to no-show.",
        "goal": "Wait 15 minutes, text a rebook link, create a call task, follow up once at day 3, then move to Nurture if they still have no appointment.",
        "qa": "On T04, mark no-show and book a new appointment before the text. No rebook text sends, and the workflow stops.",
        "channel": "SMS and email only. Do not use the client line.",
        "steps": """
1. Move the opportunity to No-Show.
2. Wait 15 minutes.
3. If the contact has an appointment in the future, stop.
4. Send SMS and email with booking_url. SMS shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. We missed each other. Pick another time here: {{custom_values.booking_url}}"
5. Create a call task due today titled "No-show follow-up".
6. Wait 3 days.
7. If the contact has an appointment in the future, stop.
8. Send one follow-up SMS and email with booking_url.
9. If there is still no future appointment, move the opportunity to Nurture.
""".strip(),
    },
    {
        "id": "W04",
        "slug": "w04-long-term-nurture",
        "name": "Long-term nurture",
        "where": "snapshot",
        "trigger": "Opportunity has been in stage Nurture for 7 days.",
        "goal": "One useful SMS or email each month for 12 months. No send before day 7.",
        "qa": "T05 receives the first note on day 7 and does not receive one on day 6. A STOP reply ends the remaining months the same day.",
        "channel": "SMS and email only. Alternate channel by month if the builder requires one action per step, but never both on the same day. Do not use the client line.",
        "steps": """
1. Wait until the opportunity has been in Nurture for 7 days. If it leaves Nurture, stop.
2. Send one value note. No pitch, no carrier, no rate. Invite them to book with booking_url only if they want to talk.
3. Repeat every 30 days, 12 times total, while the opportunity is still in Nurture.
4. If stage changes away from Nurture, stop.
SMS shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. A short note from me is on the way by email. If you would rather talk, use {{custom_values.booking_url}}"
Use a plain monthly topic list the builder can rotate: what to keep with household papers, who to call first, how to update a phone number, when to schedule a review. Do not invent savings or prices.
""".strip(),
    },
    {
        "id": "W05",
        "slug": "w05-post-sale-welcome",
        "name": "Post-sale welcome",
        "where": "snapshot",
        "trigger": "Opportunity moves to Application Submitted.",
        "goal": "A 30-day sequence: thank-you, what happens next, a draft-date reminder, and a check-in call task. The sequence stops if the stage becomes Declined.",
        "qa": "T06 gets the day-0 thank-you. After the stage moves to Declined, no later step sends.",
        "channel": "Client line and email. SMS fallback is the vendor's. Do not say iMessage.",
        "steps": """
1. Day 0. Client-line message and email: thank them, and say {{custom_values.agent_display_name}} will be the person who follows up. No coverage claim.
2. Day 1. What happens next: the agent will confirm details and the next date to remember. If draft_date is empty, say the agent will confirm the date, and do not invent one.
3. If draft_date is set, wait until the day before draft_date and send a reminder of that date. If draft_date is empty, send one reminder on day 7 that the agent still needs to confirm the date.
4. Day 14. Create a call task titled "Application check-in".
5. Day 30. One check-in message offering booking_url.
6. Before every send, if the stage is Declined, stop.
""".strip(),
    },
    {
        "id": "W06",
        "slug": "w06-care-package",
        "name": "Care package",
        "where": "snapshot",
        "trigger": "Opportunity moves to First Payment Confirmed.",
        "goal": "One kit order, one billable kit, and one vault link. A second entry into this stage does nothing.",
        "qa": "T07 sends one POST and one vault message. T08, the same contact moved into the stage again, sends nothing.",
        "channel": "Client line and email for the vault link. The kit itself is mail, via the webhook, to the contact's mailing address.",
        "steps": """
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
""".strip(),
    },
    {
        "id": "W07",
        "slug": "w07-lapse-save",
        "name": "Lapse save",
        "where": "snapshot",
        "trigger": "Opportunity moves to Payment Missed.",
        "goal": "A same-day call task, a save text, then follow-ups at day 3 and day 7. Everything stops when the stage returns to Active.",
        "qa": "T09 gets the same-day text. After the stage returns to Active, the day-3 message does not send.",
        "channel": "Client line and email. Do not say iMessage. Do not threaten cancellation and do not quote a premium.",
        "steps": """
1. Create a call task due today titled "Payment missed".
2. Send a client-line message and email. Shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. I need to talk with you about your draft. You can reach me here or pick a time: {{custom_values.booking_url}}"
3. Wait 3 days. If stage is Active, stop.
4. Send one follow-up with booking_url.
5. Wait until day 7 from the trigger. If stage is Active, stop.
6. Send one last follow-up with booking_url.
7. Do not move the stage yourself. The agent moves it when the draft is resolved.
""".strip(),
    },
    {
        "id": "W08",
        "slug": "w08-anniversary-birthday",
        "name": "Anniversary and birthday",
        "where": "snapshot",
        "trigger": "Contact birthday is today, or policy_anniversary is today.",
        "goal": "One personal text on that date. Anniversaries also include the booking link for an annual review. The workflow does not send twice in the same year for the same reason.",
        "qa": "Set T07's birthday to today and run once. One message sends. A second run the same day does not. Set policy_anniversary to today on a different run and confirm the booking link is present.",
        "channel": "Client line. No email required. Do not say iMessage.",
        "steps": """
1. If the trigger is the birthday, and a birthday message was already sent in the last 360 days, stop. Otherwise send: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. Happy birthday."
2. If the trigger is policy_anniversary, and an anniversary message was already sent in the last 360 days, stop. Otherwise send: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. It has been a year since we set this up. If you want a review, use {{custom_values.booking_url}}"
3. Do not mention a carrier or a premium. Do not say the policy is still in force.
""".strip(),
    },
    {
        "id": "W09",
        "slug": "w09-referral-ask",
        "name": "Referral ask",
        "where": "snapshot",
        "trigger": "30 days after first_payment_date.",
        "goal": "One referral request with a simple share link. Skip anyone whose current stage is Payment Missed.",
        "qa": "An Active T07 at day 30 gets one message. A copy of that contact left in Payment Missed gets none.",
        "channel": "Client line and email. Do not say iMessage.",
        "steps": """
1. If the current stage is Payment Missed, stop.
2. If tag opted-out is present, stop.
3. Send one message. Shape: "Hi {{contact.first_name}}, this is {{custom_values.agent_display_name}}. If someone you know wants the same kind of help, they can use this link: {{custom_values.booking_url}}"
4. Do not enroll this workflow a second time for the same contact.
""".strip(),
    },
    {
        "id": "P01",
        "slug": "p01-front-end-fulfillment",
        "name": "Front-end fulfillment",
        "where": "agency",
        "trigger": "Successful payment for Chargeback Shield Kit ($37), 30 Rejection-Safe Ads ($47), Referral Porch ($27), Month-2 Script ($17), or Fridge Sheet ($27), in the Producers IO agency account.",
        "goal": "The download for that product arrives by email and SMS in under 2 minutes. The buyer is tagged. No physical mail is ordered.",
        "qa": "A Stripe test purchase of Chargeback Shield Kit puts the download link in the inbox in under 2 minutes, adds front-end-buyer, and produces zero calls to kit_webhook_url.",
        "channel": "SMS and email. This workflow is not in the agent snapshot.",
        "steps": """
1. Add tag front-end-buyer and tag setup-waived.
2. Send the download link that matches the product that was just bought. One product, one link. Do not send the other four.
3. Enroll the buyer in P02 if they do not have tag member.
4. Do not call the kit webhook. Do not create a thanks.io order.
""".strip(),
    },
    {
        "id": "P02",
        "slug": "p02-founder-upsell",
        "name": "Founder upsell follow-up",
        "where": "agency",
        "trigger": "Tag front-end-buyer is added, and tag member is absent.",
        "goal": "A 7-day sequence to the single membership checkout. It stops the moment membership is purchased.",
        "qa": "A buyer who does not take the one-time offer gets day-0 and day-2 messages. Adding tag member on day 3 stops day 5 and day 7.",
        "channel": "SMS and email. Agency account only.",
        "steps": """
1. If tag member or tag founder is present, stop.
2. Day 0, day 2, day 5, and day 7: one SMS and one email pointing at membership_checkout_url. Say setup is waived because they already bought. Do not quote a second price in the text. The checkout page shows $97 while founder seats remain and $147 after.
3. Before each send, if tag member is present, stop.
4. Do not mention income, and do not promise a number of clients.
""".strip(),
    },
    {
        "id": "P03",
        "slug": "p03-new-member-onboarding",
        "name": "New member onboarding",
        "where": "agency",
        "trigger": "SaaS subscription becomes active for a new location.",
        "goal": "Welcome, an A2P checklist, a community invite, and setup nudges on day 1, day 3, and day 7.",
        "qa": "A test signup sends those touches. A separate snapshot test, not this workflow, proves the new location loaded the snapshot. This workflow must not be marked passed just because the emails sent.",
        "channel": "Email and SMS to the member. Agency account only.",
        "steps": """
1. Add tag member. If the checkout already added tag founder, leave it. Do not try to count the 20 founder seats inside this workflow. The checkout owns that count.
2. Day 0 welcome with community_url.
3. Day 0 A2P checklist: what they submit, and that sending waits on approval. Do not promise an approval time.
4. Day 1 nudge: finish the business name and booking link in custom values.
5. Day 3 nudge: confirm the client line is connected and that lead workflows are still SMS and email only.
6. Day 7 nudge: send one internal test lead to their own form.
7. If the subscription is paused or payment-failed, stop later nudges.
""".strip(),
    },
    {
        "id": "P04",
        "slug": "p04-failed-payment",
        "name": "Failed payment",
        "where": "agency",
        "trigger": "Membership payment fails.",
        "goal": "Dunning messages across 7 days. The account pauses on day 8, not before. A successful payment stops the sequence.",
        "qa": "A failed test renewal sends day 0. The location is still active at the end of day 7. It pauses on day 8. A recovered payment on day 3 sends nothing further and does not pause.",
        "channel": "SMS and email to the member. Agency account only.",
        "steps": """
1. Add tag payment-failed.
2. Day 0, day 2, day 5, and day 7: ask them to update the card. Include the billing link from the SaaS settings, as a custom value, not a hardcoded URL.
3. Before each send, if the latest invoice is paid, remove payment-failed and stop.
4. On day 8, if it is still unpaid, pause the sub-account and add tag paused. Do not delete the location.
5. Do not pause on day 0, day 2, day 5, or day 7.
""".strip(),
    },
]


def spec_md(item: dict) -> str:
    return f"""# {item['id']} {item['name']}

Account: {item['where']}.

## Trigger

{item['trigger']}

## What it does

{item['goal']}

## Channel

{item['channel']}

## Steps

{item['steps']}

## QA must prove

{item['qa']}

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
"""


def prompt_md(item: dict) -> str:
    return f"""Build a new workflow named "{item['id']} {item['name']}". Start fresh. Do not edit a workflow that is already on the canvas.

Account: {"Producers IO Master" if item['where'] == "snapshot" else "the Producers IO agency account, not a client sub-account"}.

Trigger: {item['trigger']}

{item['steps']}

Channel: {item['channel']}

{RULES}

When you finish, stop. Leave it unpublished. The human will publish after QA.
"""


def job_md(item: dict, number: int) -> str:
    status = "BLOCKED"
    return f"""# JOB-{number:03d} {item['id']} {item['name']}

Status: {status}. Do not paste this into Astra.

Unblock only after all of these are true:

- Guy has said the Producers IO Master sub-account exists.
- Guy has approved this spec (gate 1).
- JOB-000 and JOB-001 and JOB-002 have already been pasted and passed, for snapshot workflows. Agency workflows P01–P04 wait until the snapshot gate has passed and the agency checkout exists.

## Paste target

Workflow AI Builder. One workflow. Start fresh.

## Source

Paste `specs/{item['slug']}/prompt.md` in full.

## Done

A screenshot of the canvas saved next to this job, and a one-line PASS or FAIL. QA then runs the test in the spec twice. You do not publish.
"""


def main() -> None:
    jobs = ROOT / "astra-jobs"
    jobs.mkdir(exist_ok=True)
    for index, item in enumerate(WORKFLOWS, start=3):
        folder = ROOT / "specs" / item["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "spec.md").write_text(spec_md(item), encoding="utf-8")
        (folder / "prompt.md").write_text(prompt_md(item), encoding="utf-8")
        (jobs / f"JOB-{index:03d}-{item['slug']}.md").write_text(job_md(item, index), encoding="utf-8")
    print(f"wrote {len(WORKFLOWS)} workflows")


if __name__ == "__main__":
    main()
