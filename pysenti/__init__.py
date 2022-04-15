from __future__ import annotations

from typing import NamedTuple, Iterable
__version__ = '1.0.0'


class SentiResult(NamedTuple):
    positive: int
    negative: int
    neutral: int

    def scale(self) -> int:
        return self.positive - self.negative

    def is_positive(self) -> bool:
        return self.scale() > 0

