import unittest

from .parameter import Parameter


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
            "I'm a string",
            42,
            55.5,
        ]

        for v in test_values:
            p.set_value(v)
            self.assertEquals(v, p.value)
