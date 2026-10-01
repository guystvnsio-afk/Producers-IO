# Six-month plan

Window: 1 Oct 2026 through 31 Mar 2027. The number that matters is membership revenue. Kit margin and usage rebills are extra and do not count toward $6,000.

## Prices

| Offer | Price | Rule |
| --- | --- | --- |
| Founder membership | $97/mo | First 20 seats, locked while that member stays active |
| Standard membership | $147/mo | Seat 21 onward |
| Setup | $197 | Waived for anyone who bought a front end |
| Care package | 2× the thanks.io charge for that kit | Billed monthly to the member. Not part of the $6,000 |

Twenty founders and 28 standard members, all still active, is 20 × $97 + 28 × $147 = $6,056. Churn means you must sell more than 48 seats to have about 48 still paying.

## What $6,000 requires

The model is `scripts/membership_model.py`. Churn used for planning, not as a promise: 15% are gone before the second bill, then 8% each month. That is a little worse than the beta goal of 85% still paying in month 2.

Ads in November, December, and January stay at $2,000. A $250 cost per member buys 8 new members a month. A test sitting on the kill line ($100 to sell a front end, and under 10% of those buyers taking membership) costs about $1,000 per member and buys 2.

| Path | Nov–Jan | Feb–Mar | End of March |
| --- | --- | --- | --- |
| Cap, then stop. $250 per member | 8, 8, 8 | no ads | about $1,800 MRR, 17 members |
| Kill line, then stop | 2, 2, 2 | no ads | about $420 MRR, 4 members |
| January gate passes | 8, 8, 8 at $2,000 | 16 and 16 at $4,000 | about $6,200 MRR, 47 members |
| Stay at $2,000 all five selling months | 12 a month, which needs about $167 per member | same | about $6,400 MRR |

The $2,000 cap does not reach $6,000 by March unless members cost about $167 or less for the whole stretch. The working road is the gate, not a hope that the cap is enough.

## January 31 gate

Raise February and March to $4,000 only if both are true:

- Blended cost per new member is $250 or less.
- Front-end buyers take membership at 20% or better.

If either miss, leave spend at $2,000 or cut it. Do not buy $6,000 of MRR with $1,000 members. At $97, a $1,000 member takes more than 10 months of dues to repay the ads, before HighLevel.

## Month by month

### October — build, no ads

You register the domain, run the trademark search, start the 14-day Agency Pro trial, and create `Producers IO Master`. Specs in this repo are the build input. Astra stays unpasted until that sub-account exists and you approve the specs.

Cash: domain, then HighLevel at $497 when the trial ends. No Meta spend.

### November — launch and first tests

Target launch is the week of 10 Nov, six weeks from 1 Oct, only if the five gates in `docs/testing.md` pass. Spend $2,000 across 3 to 5 front ends, $300 to $500 each. Kill a front end when a sale costs more than $100 or fewer than 10% of buyers take membership.

### December — keep the winners

Put the next $2,000 into front ends that survived November. Do not restart a killed offer with a new headline and the same page.

### January — last month of the cap, then the gate

Spend the third $2,000. On 31 Jan, apply the gate above. Write the actual cost per member and take rate into this file before February spend starts.

### February and March — scale or hold

If the gate passes, $4,000 each month at the same cost per member is the path that lands near $6,200. If it fails, hold or cut spend. $6,000 moves past March instead of being forced.

## Cash, separate from MRR

| Item | Amount |
| --- | --- |
| HighLevel, six bills if the trial starts 1 Oct and converts | 6 × $497 = $2,982 |
| Ads if you stop after January | $6,000 |
| Ads if the January gate passes | $6,000 + $8,000 = $14,000 |
| Domain | about $20 |

Kit cost is recovered at 2× from the member, so it is not part of this table. Blooio’s price is not on the integration page. Add it when you buy the line.

$6,200 MRR is not profit. HighLevel at $497 is the fixed platform bill. Usage is rebilled to members with a small markup, in SaaS mode.

## Care package money

Recipients are only the customers of your members. A kit leaves when that customer’s deal hits First Payment Confirmed. One kit per customer.

| Plan | Kit cost | Invoice to the member | Your margin before the plan fee |
| --- | --- | --- | --- |
| No monthly plan | $4.84 | $9.68 | $4.84 |
| $49 Business plan | $2.98 | $5.96 | $2.98 |

Stay on pay as you go until a month actually ships 27 kits. Invoice 2× the thanks.io charge on that order, not a frozen $9.68, so a plan change does not make you sell below 2×.

The beta goal is at least two kits per member per month. At 47 members that is about 94 kits. That is past the 27-kit switch. Do not switch early to chase it.

## People and time

You are not on calls. Support is the community, the AI agent, and onboarding videos. The beta bar is under one hour of your time per member per month. At 47 members that is still about 47 hours, so the videos and the AI agent have to answer A2P, number trouble, and kit questions before those tickets reach you.

A weekend group call is allowed later only if, in a given month, more than 30% of active members open a ticket that is specifically about getting their own ads running. It is not part of v1.

## Beta bar, first 60 days after launch

- Under one hour of support per member per month.
- 85% of the first members still paying at month 2.
- At least two care packages per member per month.
- No workflow failure that reaches a real customer.

Twenty founder seats are the beta, not a reason to skip the kill rules.

## What is out of these six months

Multi-line dialer, a Pro tier, Google Business Profile setup, a roleplay coach, a recruiting kit, and a custom dashboard on the HighLevel API. They wait until the membership number is real.
