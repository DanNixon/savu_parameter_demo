import voluptuous as vol

from savu.core.parameters import Parameter, validation


class Pattern(Parameter):

    def __init__(self):
        super(Pattern, self).__init__(
            name="pattern",
            description="Data slice pattern",
            default="PROJECTION",
            schema=validation.enum([
                "PROJECTION",
                "SINOGRAM",
            ])
        )
