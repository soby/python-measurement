from decimal import Decimal

from measurement.base import MeasureBase


__all__ = [
    'Current'
]


class Current(MeasureBase):
    STANDARD_UNIT = 'A'
    UNITS = {
        'A': Decimal('1.0'),
    }
    ALIAS = {
        'amp': 'A',
        'ampere': 'A',
    }
    SI_UNITS = ['A']
