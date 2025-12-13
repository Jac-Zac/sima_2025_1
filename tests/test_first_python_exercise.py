import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


def test_python_exercise_sum():
    from tools.weird_maths import robust_sum
    assert robust_sum([1, 2, 3, 4, 5]) == 15

def test_python_exercise_sum_empty():
    from tools.weird_maths import robust_sum
    assert robust_sum([]) == 0

def test_python_exercise_sum_negative():
    from tools.weird_maths import robust_sum
    assert robust_sum([-1, -2, -3, -4, -5]) == -15

def test_weird_sum():
    from tools.weird_maths import robust_sum
    assert robust_sum([1, 2.123 ,"pippo", 3]) == 6.123