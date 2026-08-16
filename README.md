# large-mixed-codebase

A generic web-app scaffold (health-check route, a couple of utility
modules, tests) — mostly boilerplate unrelated to AI. This repo exists
purely as a fixture for evaluating the JuriCode Compliance Gate: does it
correctly localize a real Annex III finding to one small buried component
without over-flagging unrelated boilerplate elsewhere in the diff?

See `PREDICTION.md` for the expected audit result of the PR that adds
`src/internal_tools/hr_screening/`.
