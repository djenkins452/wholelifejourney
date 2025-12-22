# Architecture & Product Decisions

This document records intentional, locked decisions for the Whole Life Journey platform.
Once a decision is approved and merged, it is considered binding unless explicitly revisited.

---

## AI FOUNDATION — PHASE 3

### Decision: AI is read-only and deferred

**Status:** Approved  
**Phase:** 3  

AI capabilities are explicitly deferred until later phases.

At this stage:
- No AI code may be written
- No AI services may be integrated
- No background jobs, agents, or API calls are permitted

This phase exists solely to establish guardrails.

---

### When AI is introduced (future phase only)

AI must comply with **all** of the following constraints:

- Read-only access to user data
- Summarization and pattern recognition only
- No diagnosis of medical or mental conditions
- No treatment recommendations
- No medication guidance
- No therapy or crisis counseling
- No autonomous actions
- No background data mutation

---

### AI Output Requirements

All AI output must be:

- Clearly labeled as reflective insight
- Non-prescriptive
- Conservative in tone
- Designed to support human judgment, not replace it

---

### Enforcement

If any future implementation violates these constraints:
- Work must stop immediately
- This decision must be explicitly reviewed and amended
- No silent expansion of AI scope is allowed

These guardrails exist to protect:
- User safety
- Product trust
- Long-term platform integrity

---

## Architecture Checkpoint — Phase 3

**Status:** Approved  
**Phase:** 3  

System boundaries, ownership rules, and data lifecycle constraints
are formally documented in `docs/architecture.md`.

All future work must comply with these constraints unless explicitly revised.
