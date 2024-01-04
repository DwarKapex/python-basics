"""
create dataclass `Engine`
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Engine:
    volume: int = 0
    pistons: int = 0
