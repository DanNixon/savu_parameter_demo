import unittest

from .. import SchemaValidationError
from .enum import Enum


class EnumTest(unittest.TestCase):

    def test_help_text_nullable(self):
        s = Enum(['a', 'b', 'c'], nullable=True)
        self.assertEquals(s.value_help_str, 'One of "a", "b", "c", or None')

    def test_help_text_not_nullable(self):
        s = Enum(['a', 'b', 'c'], nullable=False)
        self.assertEquals(s.value_help_str, 'One of "a", "b", "c"')

    def test_valid_values_nullable(self):
        s = Enum(['a', 'b', 'c'], nullable=True)
        self.assertEquals(['a', 'b', 'c', None], s.valid_values)

    def test_valid_values_not_nullable(self):
        s = Enum(['a', 'b', 'c'], nullable=False)
        self.assertEquals(['a', 'b', 'c'], s.valid_values)

    def test_validate_nullable(self):
        s = Enum(['a', 'b', 'c'], nullable=True)

        # All valid
        s.validate(None)
        s.validate('a')
        s.validate('b')
        s.validate('c')

        # Not valid
        with self.assertRaises(SchemaValidationError):
            s.validate('d')

    def test_validate_not_nullable(self):
        s = Enum(['a', 'b', 'c'], nullable=True)

        # All valid
        s.validate('a')
        s.validate('b')
        s.validate('c')

        # Not valid
        with self.assertRaises(SchemaValidationError):
            s.validate(None)
            s.validate('d')
