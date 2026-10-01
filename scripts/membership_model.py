#!/usr/bin/env python3
"""Membership-only MRR model for the six-month plan.

First 20 seats sold are $97. Later seats are $147.
A seat keeps its original price while that member stays.
Planning churn, not a promise: 15% do not reach month 2, then 8% each month.
Month 0 is October 2026. Selling starts in November.
"""

from __future__ import annotations

MONTHS = ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
FOUNDER_PRICE = 97
STANDARD_PRICE = 147
FOUNDER_SEATS = 20
CHURN_FIRST = 0.15
CHURN_LATER = 0.08


def simulate(monthly_new: list[int]) -> list[dict]:
    cohorts: list[dict] = []
    seats_sold = 0
    rows: list[dict] = []
    for month, adds in enumerate(monthly_new):
        founders = 0.0
        standard = 0.0
        for cohort in cohorts:
            age = month - cohort["start"]
            if age <= 0:
                weight = cohort["n"]
            elif age == 1:
                weight = cohort["n"] * (1 - CHURN_FIRST)
            else:
                weight = cohort["n"] * (1 - CHURN_FIRST) * ((1 - CHURN_LATER) ** (age - 1))
            if cohort["price"] == FOUNDER_PRICE:
                founders += weight
            else:
                standard += weight
        add_founder = max(0, min(adds, FOUNDER_SEATS - seats_sold))
        add_standard = adds - add_founder
        if add_founder:
            cohorts.append({"start": month, "n": add_founder, "price": FOUNDER_PRICE})
            founders += add_founder
        if add_standard:
            cohorts.append({"start": month, "n": add_standard, "price": STANDARD_PRICE})
            standard += add_standard
        seats_sold += adds
        rows.append(
            {
                "month": MONTHS[month],
                "new": adds,
                "active": round(founders + standard, 1),
                "founders": round(founders, 1),
                "standard": round(standard, 1),
                "mrr": round(founders * FOUNDER_PRICE + standard * STANDARD_PRICE),
                "seats": seats_sold,
            }
        )
    return rows


def print_case(title: str, monthly_new: list[int]) -> None:
    print(f"\n{title}")
    print(f"{'Month':<6}{'New':>6}{'Active':>8}{'Founder':>9}{'Standard':>10}{'MRR':>8}{'Seats':>7}")
    for row in simulate(monthly_new):
        print(
            f"{row['month']:<6}{row['new']:>6}{row['active']:>8.1f}"
            f"{row['founders']:>9.1f}{row['standard']:>10.1f}{row['mrr']:>8}{row['seats']:>7}"
        )


def main() -> None:
    print("Target: 20 x $97 + 28 x $147 =", 20 * 97 + 28 * 147)
    print_case("Cap only. $2,000/mo Nov-Jan at $250 per member, then stop.", [0, 8, 8, 8, 0, 0])
    print_case("Kill line. $2,000/mo Nov-Jan at $1,000 per member, then stop.", [0, 2, 2, 2, 0, 0])
    print_case("January gate passes. 8, then 16 per month at $250.", [0, 8, 8, 8, 16, 16])
    print_case("Stay inside $2,000. Needs about $167 per member, 12 per month.", [0, 12, 12, 12, 12, 12])


if __name__ == "__main__":
    main()
