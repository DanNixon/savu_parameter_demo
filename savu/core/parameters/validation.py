import sys
import voluptuous as vol


def _get_thing(thing):
    return thing.schema if isinstance(thing, vol.Schema) else thing


def nullable(thing):
    return vol.Schema(vol.Any(None, _get_thing(thing)))


def of_length(thing, min_len=None, max_len=None):
    return vol.Schema(vol.All(vol.Length(min_len, max_len), _get_thing(thing)))


def string():
    return vol.Schema(vol.Any(str, unicode) if sys.version_info.major == 2 else str)


def enum(values):
    return vol.Schema(vol.In(values))
