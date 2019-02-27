from savu.core.parameters import Schema


class Parameter(object):

    def __init__(self, name, description, default, schema=Schema()):
        self._name = name
        self._description = description
        self._schema = schema

        # Validate and set default value
        self._schema.validate(default)
        self._default = default
        self._value = default

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def default(self):
        return self._default

    @property
    def value(self):
        return self._value

    def set_value(self, value):
        # Validate new value before setting it
        self._schema.validate(value)

        self._value = value
