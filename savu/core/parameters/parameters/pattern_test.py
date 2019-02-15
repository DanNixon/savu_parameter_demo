import unittest

from pattern import Pattern


class PatternParameterTest(unittest.TestCase):

    def test_name(self):
        p = Pattern()
        self.assertEquals("pattern", p.name)

    def test_set_projection(self):
        p = Pattern()
        p.set_value("PROJECTION")
        self.assertEquals("PROJECTION", p.value)

    def test_set_sinogram(self):
        p = Pattern()
        p.set_value("SINOGRAM")
        self.assertEquals("SINOGRAM", p.value)
