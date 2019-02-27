from savu.core.parameters import Parameter, schemas


class Pattern(Parameter):

    def __init__(self):
        super(Pattern, self).__init__(
            name="pattern",
            description="Data slice pattern",
            default="PROJECTION",
            schema=schemas.Enum([
                "PROJECTION",
                "SINOGRAM",
            ])
        )
