from savu.core.parameters import Schema, SchemaValidationError


class Enum(Schema):

    def __init__(self, values, nullable=False):
        super(Enum, self).__init__(nullable)
        self._enum_values = values

    def validate(self, value):
        super(Enum, self).validate(value)
        if value not in self._enum_values:
            raise SchemaValidationError('Value "{}" not in allowed enum items ({})'.format(value, self._enum_values))

    def value_help_str(self):
        text = 'One of {}'.format(','.join(self._enum_values))
        if self._nullable:
            text += ', or None'
        return text
