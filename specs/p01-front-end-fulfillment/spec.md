# P01 Front-end fulfillment

Account: agency.

## Trigger

Successful payment for Chargeback Shield Kit ($37), 30 Rejection-Safe Ads ($47), Referral Porch ($27), Month-2 Script ($17), or Fridge Sheet ($27), in the Producers IO agency account.

## What it does

The download for that product arrives by email and SMS in under 2 minutes. The buyer is tagged. No physical mail is ordered.

## Channel

SMS and email. This workflow is not in the agent snapshot.

## Steps

1. Add tag front-end-buyer and tag setup-waived.
2. Send the download link that matches the product that was just bought. One product, one link. Do not send the other four.
3. Enroll the buyer in P02 if they do not have tag member.
4. Do not call the kit webhook. Do not create a thanks.io order.

## QA must prove

A Stripe test purchase of Chargeback Shield Kit puts the download link in the inbox in under 2 minutes, adds front-end-buyer, and produces zero calls to kit_webhook_url.

## Done

Draft only. Screenshot of the canvas. Two QA passes recorded in `qa.md`.
