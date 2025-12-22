# AI Contracts — Whole Life Journey

This document defines the **technical and ethical contract** for any future AI
capability in the platform.

AI IS CURRENTLY DISABLED.

---

## Purpose

These contracts exist to ensure:
- Predictable AI behavior
- Clear boundaries
- Safe evolution over time

No AI implementation may bypass these contracts.

---

## Core Principles

Any AI capability must be:

- Read-only
- Deterministic where possible
- Reflective, not directive
- Non-medical
- Non-therapeutic

---

## Allowed Capabilities (Future Phase Only)

AI may:
- Summarize time periods
- Highlight recurring patterns
- Surface correlations across life domains
- Assist with reflection and planning

---

## Prohibited Capabilities

AI must never:
- Diagnose conditions
- Recommend treatment or medication
- Provide therapy or crisis counseling
- Perform autonomous actions
- Mutate user data
- Run background jobs without explicit invocation

---

## Enforcement

All AI implementations must:
- Implement the contracts in `core/ai/contracts.py`
- Be reviewed against `docs/decisions.md`
- Be explicitly enabled via configuration

Any violation requires an immediate stop and review.
