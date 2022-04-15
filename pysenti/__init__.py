from __future__ import annotations

import subprocess as sp
from typing import NamedTuple, Iterable

import pkg_resources

__version__ = '1.0.0'
JAVA_COMMAND = 'java'


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


def _cmd() -> list[str]:
    jar, data = _paths()
    return [JAVA_COMMAND, '-jar', jar, 'sentidata', data]


def _decode_output(stdout: str | bytes) -> SentiResult:
    """
    Decode SentiStrength java output

    :param stdout: The result that SentiStrength printed
    :return: Parsed SentiResult
    """
    if isinstance(stdout, bytes):
        stdout = stdout.decode()

    return SentiResult(*[int(s) for s in stdout.strip().replace('\t', ' ').split(' ')])


def get_senti(text: str) -> SentiResult:
    """
    Get sentiment score of a text

    :param text:
    :return: Sentiment result
    """
    return _decode_output(sp.check_output([*_cmd(), 'trinary', 'text', text.strip()]))


