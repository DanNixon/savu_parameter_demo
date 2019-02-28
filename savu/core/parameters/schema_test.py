import unittest

from .schema import Schema, SchemaValidationError


class SchemaTest(unittest.TestCase):

    def test_validate_nullable(self):
        s = Schema(nullable=True)

        # Any non-None value is allowed
        s.validate('Not None')

        # None is allowed
        s.validate(None)

    def test_validate_not_nullable(self):
        s = Schema(nullable=False)

        # Any non-None value is allowed
        s.validate('Not None')

        # None is not allowed
        with self.assertRaises(SchemaValidationError):
            s.validate(None)

    def test_help_text_nullable(self):
        s = Schema(nullable=True)
        self.assertEquals(s.value_help_str(), 'Any value of any type, or None')

    def test_help_text_not_nullable(self):
        s = Schema(nullable=False)
        self.assertEquals(s.value_help_str(), 'Any non-None value of any type')
