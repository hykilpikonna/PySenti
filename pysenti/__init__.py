from __future__ import annotations

from typing import NamedTuple, Iterable

import pkg_resources

__version__ = '1.0.0'


class SentiResult(NamedTuple):
    positive: int
    negative: int
    neutral: int

    def scale(self) -> int:
        return self.positive - self.negative

    def is_positive(self) -> bool:
        return self.scale() > 0


def _paths() -> tuple[str, str]:
    jar = pkg_resources.resource_filename(__name__, 'original/SentiStrength.jar')
    data = pkg_resources.resource_filename(__name__, 'original/data') + '/'
    return jar, data

