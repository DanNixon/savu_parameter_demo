import copy


class NoSuchParameterError(RuntimeError):

    def __init__(self, name):
        super(RuntimeError, self).__init__(
            "No parameter found matching name \"{}\"".format(name)
        )


class DuplicateParameterNameError(RuntimeError):

    def __init__(self, names):
        super(RuntimeError, self).__init__(
            "One of more duplicate paremeter names were found ({})".format(
                ','.join(names))
        )


def check_unique_parameter_names(params):
    names_list = list([p.name for p in params])
    if len(names_list) != len(set(names_list)):
        raise DuplicateParameterNameError(names_list)


class Plugin(object):

    def __init__(self, name, parameters):
        self._name = name
        check_unique_parameter_names(parameters)
        self.parameters = copy.deepcopy(parameters)

    @property
    def name(self):
        return self._name

    @property
    def parameter_names(self):
        return [p.name for p in self.parameters]

    def parameter(self, name):
        p = [p for p in self.parameters if p.name == name]
        if not p:
            raise NoSuchParameterError(name)
        # List should be of length 1 as duplicate names have already been
        # tested for
        return p[0]

    def parameter_value(self, name):
        return self.parameter(name).value

    def set_parameter(self, name, value):
        self.parameter(name).set_value(value)
