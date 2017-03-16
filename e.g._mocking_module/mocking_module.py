from disabled_package import disabled_module
from disabled_package.disabled_module import disabled_submodule

class Target(object):
    def square(self, value):
        # wish to replace when unittest
        disabled_module.call_function(disabled_submodule.CONST)

        return value ** 2
