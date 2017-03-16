import pytest
# above Python 3.3 (under 3.3, pip install mock)
from unittest.mock import Mock

# before import target module
import sys
sys.modules['disabled_package'] = Mock()
sys.modules['disabled_package.disabled_module'] = Mock()

# using 'disabled_package''disabled_package.disabled_module' in 'target' module
from mocking_module import Target

class Test_Target(object):
    def test_square(self):
        # Arrange
        sut = Target()
        # Act
        actual = sut.square(2)
        # Assert
        assert actual == 4
