# Rules baked into every workflow prompt

- Send only from 08:00 to 20:00 in the contact’s time zone. Hold anything else until 08:00.
- STOP, UNSUBSCRIBE, CANCEL, QUIT, or END adds `opted-out` and ends every message in this workflow.
- A contact who already has `opted-out` never enters the send steps.
- Every person name, business name, and link is a custom value from `specs/data-model.md`.
- Do not type a phone number or a URL into the message text.
- Do not mention a carrier, a price of a policy, an age, Medicare, or a promised result.
- Do not say iMessage.
- Do not publish. Leave the workflow in draft.
- W01 through W04 use SMS and email only.
- W05 through W09 may use the client line, with the vendor’s SMS fallback. Copy stays the same either way.
