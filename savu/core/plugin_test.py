import unittest
import voluptuous as vol

from . import parameters
from .plugin import (
    Plugin,
    NoSuchParameterError,
    DuplicateParameterNameError
)


class TestPlugin1(Plugin):

    def __init__(self):
        super(TestPlugin1, self).__init__("TestPlugin1", [
            parameters.Pattern(),
        ]);


class PluginTest(unittest.TestCase):

    def test_create_with_no_parameters(self):
        p = Plugin("test", [])
        self.assertEqual("test", p.name)
        self.assertEqual([], p.parameter_names)

    def test_create_with_duplicate_parameters(self):
        with self.assertRaises(DuplicateParameterNameError):
            p = Plugin("test", [
                    parameters.Pattern(),
                    parameters.Pattern(),
                ])

    def test_get_non_existent_parameter(self):
        p = Plugin("test", [])
        self.assertEqual("test", p.name)
        with self.assertRaises(NoSuchParameterError):
            p.parameter("nope")

    def test_create_test_plugin_1(self):
        p = TestPlugin1()
        self.assertEqual("TestPlugin1", p.name)
        self.assertEqual(["pattern"], p.parameter_names)
        self.assertEqual("pattern", p.parameter("pattern").name)

    def test_set_value_valid(self):
        p = TestPlugin1()
        self.assertEqual("PROJECTION", p.parameter_value("pattern"))
        p.set_parameter("pattern", "SINOGRAM")
        self.assertEqual("SINOGRAM", p.parameter_value("pattern"))

    def test_set_value_invalid(self):
        p = TestPlugin1()
        self.assertEqual("PROJECTION", p.parameter_value("pattern"))
        with self.assertRaises(vol.MultipleInvalid):
            p.set_parameter("pattern", "NOT A THING")
        self.assertEqual("PROJECTION", p.parameter_value("pattern"))
