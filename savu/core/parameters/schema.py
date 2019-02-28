class SchemaValidationError(ValueError):

    def __init__(self, error_message):
        super(SchemaValidationError, self).__init__(error_message)


class Schema(object):

    def __init__(self, nullable=False):
        self._nullable = nullable

    @property
    def nullable(self):
        return self._nullable

    def validate(self, value):
        """
        Checks if a value is valid.
        Throws SchemaValidationError on invalid value.
        Should be overridden by subclases.
        """
        if not self._nullable and value is None:
            raise SchemaValidationError('Value is None but parameter is not nullable')

    @property
    def value_help_str(self):
        """
        Gets a help text describing valid values for this schema.
        """
        return 'Any value of any type, or None' if self._nullable else 'Any non-None value of any type'

    @property
    def valid_values(self):
        """
        Return the set of valid values that satisfy this schema.
        If it is impossible to list values (e.g. free text, numerical range) then None should be returned.
        """
        return None
