# System Architecture — Whole Life Journey

This document defines **ownership, boundaries, and lifecycle rules**
for the Whole Life Journey platform.

These rules are binding once approved.

---

## Core Architectural Principle

Each module must be:
- Independently understandable
- Independently testable
- Independently evolvable

No module may assume internal details of another module.

---

## Layer Ownership

### Presentation Layer
**Location**
- `core/templates/`
- `core/static/`

**Responsibilities**
- HTML rendering
- Styling and layout
- User interaction

**Must NOT**
- Contain business logic
- Contain data mutation rules
- Import AI or analytics logic

---

### Application Layer
**Location**
- `core/views.py`
- `core/forms.py`
- `core/urls.py`

**Responsibilities**
- Request handling
- Permission enforcement
- Orchestration of domain logic

**Must NOT**
- Contain long-term business rules
- Contain AI logic
- Mutate data implicitly

---

### Domain Layer
**Location**
- `core/models.py`
- future: `core/domain/`

**Responsibilities**
- Data models
- Data integrity rules
- Lifecycle transitions (create, soft delete, restore)

**Must NOT**
- Render UI
- Call external services
- Contain AI behavior

---

### AI Boundary Layer (Future)
**Location**
- `core/ai/`

**Current State**
- Contracts only
- AI disabled

**Responsibilities (future only)**
- Read-only reflection
- Pattern summarization

**Must NOT**
- Mutate data
- Run autonomously
- Bypass domain rules

---

## Module Ownership Rules

Each module owns:
- Its models
- Its views
- Its templates
- Its migrations

Cross-module access must:
- Go through explicit interfaces
- Never rely on internal fields

---

## Data Lifecycle Rules

### Creation
- Explicit user action only
- Always user-scoped

### Modification
- Explicit user intent
- No background mutation

### Deletion
- Soft delete first
- Reversible where possible
- Permanent delete requires confirmation

---

## Cross-Cutting Concerns

### Authentication
- Enforced at view level
- Never assumed implicitly

### Authorization
- Role-based
- Explicit checks only

### Logging
- Informational
- No sensitive data

---

## Enforcement

If any change:
- Breaks these boundaries
- Blurs ownership
- Introduces hidden coupling

Work must stop and architecture must be revisited.

This document exists to protect long-term clarity.
