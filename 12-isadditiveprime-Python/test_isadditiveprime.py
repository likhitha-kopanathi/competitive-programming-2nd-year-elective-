import pytest
from isadditiveprime import isadditiveprime
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('x, check', [
    (2, True),
    (3,  True),
    (11, True),
    (18,  False),
    (23, True),
    (101, True),
    (192, False),
    (360, False)

    
])
def test_additiveprime(x, check):
    assert isadditiveprime(x) == check