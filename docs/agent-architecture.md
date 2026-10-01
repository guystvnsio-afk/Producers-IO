# Agent architecture

You do not build HighLevel workflows by hand. Each agent has one job. A folder is the record. Chat is not.

## Roster

| # | Agent | Where it runs | Writes | Done when |
| --- | --- | --- | --- | --- |
| 1 | Architect | This repo | One spec and one paste prompt per workflow | Every workflow in `specs/` has both |
| 2 | Data model | Astra, after Master exists | Custom fields, custom values, tags, 10 test contacts | An API read-back matches `specs/data-model.md` |
| 3 | Builder | Astra, one job at a time | Pipelines, one calendar, then one workflow per job | Screenshot of the finished canvas, then QA passes |
| 4 | QA | Astra or a later code pass | Pass/fail log in the workflow folder | Two clean passes in a row, including STOP and quiet hours |
| 5 | Funnel | Astra, HighLevel Funnel AI | One checkout, one upsell, one thank-you page | A Stripe test purchase finishes. Waits on the lab file |
| 6 | Copy | This repo, then you | Page and kit copy that passes `docs/compliance.md` | Checklist marked line by line |
| 7 | Creative | Your video stack | Faceless ads from approved copy | You approve. No face, no fake testimonial |
| 8 | Vault and kits | Astra, extended build | Kit webhook and the policy vault page | A test customer gets one vault link and one test mail order |
| 9 | Ops | Research notes in `docs/open-items.md` | Sourced status for each open item | You close the rows that need a login |

You are the gate. You approve specs, publish each workflow batch, approve the snapshot, approve ads, and own every login.

## How a build moves

1. Architect spec is in the repo.
2. You approve that batch. Nothing is pasted before that.
3. You create `Producers IO Master`. Until you say it exists, Astra jobs stay blocked.
4. You paste one Astra job. Never the whole snapshot in one run.
5. Astra stops with a screenshot and a pass/fail line.
6. QA runs the test contacts twice.
7. You publish in the workflow builder.
8. After every agent-snapshot workflow passes, Astra makes the snapshot and you approve it.
9. SaaS signup is then wired to create a location and load that snapshot.

If a job pauses inside Astra, resume that one job. Do not combine the rest to save time.

## What is already written

Specs and prompts for W01–W09 and P01–P04 are in `specs/`. Pipeline instructions are in `astra-jobs/JOB-000-do-not-run-yet.md`. Do not paste that file yet.

Funnel page builds are not jobs yet. They wait until you drop the front-end lab. The five named offers are enough to describe the checkout. They are not enough to design 54 pages.

## Handoff folder

Each workflow folder holds:

- `spec.md` — trigger, steps, and the one thing QA must prove
- `prompt.md` — the text you paste into Workflow AI Builder
- `qa.md` — added later, with two pass/fail lines and the failing step if there is one
- the canvas screenshot — added by Astra, not by this repo

## Accounts

| Account | What lives there |
| --- | --- |
| Producers IO Master | The snapshot source. Pipelines, fields, W01–W09 |
| A fresh test location | Snapshot load test. Never a real member |
| Producers IO agency account | P01–P04, the front-end checkout, member dunning |

W01–W04 use SMS and email only. The Blooio client line starts at W05, and only for people who are already customers of your member.
