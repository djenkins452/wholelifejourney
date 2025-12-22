"""
AI Contracts for Whole Life Journey

This module defines strict interfaces for future AI integrations.
AI is DISABLED at this stage and this file must contain:
- No imports of AI libraries
- No network calls
- No side effects
"""

from dataclasses import dataclass
from typing import List, Optional, Protocol
from datetime import date


@dataclass(frozen=True)
class LifeEvent:
    """
    Immutable representation of a point on the life timeline.
    """
    occurred_on: date
    category: str
    summary: str


@dataclass(frozen=True)
class ReflectionResult:
    """
    Output returned by any AI reflection process.
    This is read-only and non-prescriptive.
    """
    title: str
    narrative: str
    patterns: List[str]
    cautions: Optional[List[str]] = None


class LifeReflectionEngine(Protocol):
    """
    Contract for any future AI reflection engine.

    Implementations MUST:
    - Be read-only
    - Produce reflective insight only
    - Avoid diagnosis, advice, or instruction
    """

    def summarize_period(
        self,
        events: List[LifeEvent],
        start_date: date,
        end_date: date,
    ) -> ReflectionResult:
        """
        Summarize a time period using provided life events.
        """
        ...
