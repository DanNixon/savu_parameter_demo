import voluptuous as vol

from savu.core.parameters import Parameter


class Pattern(Parameter):

    def __init__(self):
        super(Pattern, self).__init__(
            name="pattern",
            description="Data slice pattern",
            default="PROJECTION",
            schema=vol.Schema(vol.In([
                "PROJECTION",
                "SINOGRAM",
            ]))
        )
