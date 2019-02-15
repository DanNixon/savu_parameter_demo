import unittest
import voluptuous as vol

from . import validation as val


class NullableTest(unittest.TestCase):
 
    def setUp(self):
        self._invalid_things = [
            "I'm a string",
            99.9,
            ["a", "list"],
            {"a": "dict"},
        ]

    def test_schema_valid_value(self):
        val.nullable(vol.Schema(int))(42)

    def test_schema_valid_none(self):
        val.nullable(vol.Schema(int))(None)

    def test_schema_invalid(self):
        for v in self._invalid_things:
            with self.assertRaises(vol.MultipleInvalid):
                val.nullable(vol.Schema(int))(v)

    def test_type_valid_value(self):
        val.nullable(int)(42)

    def test_type_valid_none(self):
        val.nullable(int)(None)

    def test_type_invalid(self):
        for v in self._invalid_things:
            with self.assertRaises(vol.MultipleInvalid):
                val.nullable(int)(v)


class OfLengthTest(unittest.TestCase):

    def test_none_valid(self):
        for l in range(10):
            s = "a" * l
            self.assertEquals(l, len(s))
            val.of_length(val.string())(s)

    def test_min_valid(self):
        for l in range(5, 10):
            s = "a" * l
            self.assertEquals(l, len(s))
            val.of_length(val.string(), min_len=5)(s)

    def test_min_invalid(self):
        for l in range(5):
            s = "a" * l
            self.assertEquals(l, len(s))
            with self.assertRaises(vol.MultipleInvalid):
                val.of_length(val.string(), min_len=5)(s)

    def test_max_valid(self):
        for l in range(10):
            s = "a" * l
            self.assertEquals(l, len(s))
            val.of_length(val.string(), max_len=10)(s)

    def test_max_invalid(self):
        for l in range(11, 15):
            s = "a" * l
            self.assertEquals(l, len(s))
            with self.assertRaises(vol.MultipleInvalid):
                val.of_length(val.string(), max_len=10)(s)

    def test_both_valid(self):
        for l in range(5, 10):
            s = "a" * l
            self.assertEquals(l, len(s))
            val.of_length(val.string(), min_len=5, max_len=10)(s)

    def test_both_invalid(self):
        for l in [2, 3, 4, 11, 12]:
            s = "a" * l
            self.assertEquals(l, len(s))
            with self.assertRaises(vol.MultipleInvalid):
                val.of_length(val.string(), min_len=5, max_len=10)(s)


class StringTest(unittest.TestCase):
    
    def test_str(self):
        val.string()("this is string")

    def test_invalid(self):
        invalid_things = [
            None,
            42,
            99.9,
            ["a", "list"],
            {"a": "dict"},
        ]

        for v in invalid_things:
            with self.assertRaises(vol.MultipleInvalid):
                val.string()(v)
