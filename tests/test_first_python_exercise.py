def test_python_exercise_sum():
    from src.tools.weird_maths import robust_sum
    assert robust_sum([1, 2, 3, 4, 5]) == 15

def test_python_exercise_sum_empty():
    from src.tools.weird_maths import robust_sum
    assert robust_sum([]) == 0

def test_python_exercise_sum_negative():
    from src.tools.weird_maths import robust_sum
    assert robust_sum([-1, -2, -3, -4, -5]) == -15

def test_weird_sum():
    from src.tools.weird_maths import robust_sum
    assert robust_sum([1, 2.123 ,"pippo", 3]) == 6.123