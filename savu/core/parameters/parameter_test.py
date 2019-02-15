import unittest
import voluptuous as vol

from parameter import Parameter


class ParameterTest(unittest.TestCase):

    def test_meta(self):
        p = Parameter(
            name="test_param",
            description="this is a test parameter",
            default="hello",
        )
        self.assertEquals("test_param", p.name)
        self.assertEquals("this is a test parameter", p.description)
        self.assertEquals("hello", p.value)

    def test_set_value_no_schema(self):
        p = Parameter(
            name="test_param",
            description="this is a test parameter",
            default="hello",
        )
        self.assertEquals("hello", p.value)

        test_values = [
            None,
            "I'm a string",
            42,
            55.5,
        ]

        for v in test_values:
            p.set_value(v)
            self.assertEquals(v, p.value)

    def test_set_value_with_schema(self):
        p = Parameter(
            name="test_param",
            description="this is a test parameter",
            default=42,
            schema=vol.Schema(int),
        )
        self.assertEquals(42, p.value)

        with self.assertRaises(vol.MultipleInvalid):
            p.set_value("I'm a string")

        p.set_value(99)
        self.assertEquals(99, p.value)
