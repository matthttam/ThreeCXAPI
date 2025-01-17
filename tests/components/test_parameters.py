from abc import ABC
from components.parameters import ListParameters


class TestParameters:

    def test_parameters_is_abc(self):
        assert issubclass(ListParameters, ABC)
