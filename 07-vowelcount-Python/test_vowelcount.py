import pytest
from vowelcount import vowelcount
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('x, check', [
    ("Likhitha", 3),
    ("Benarjee", 4),
    ("Lakshmi", 2),
    ("Taecyeon", 4),
    ("Virat", 2),
    ("Junhoo", 3),
    ("Nichkhun", 2),
    ("2pm", 0)

    
])
def test_vowelcount(x, check):
    assert vowelcount(x) == check