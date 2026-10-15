import pytest

import members.YinceIuCode.w1.grades as g
import members.YinceIuCode.w1.rules as r
import members.YinceIuCode.w1.text_tools as t
import members.YinceIuCode.w1.timetable as tt
import members.YinceIuCode.w1.translate as tr


def test_w1_1_summary():
    assert g.summary([8.5, 9.5, 7.0, 6.0]) == {
        "min": 6.0,
        "max": 9.5,
        "mean": 7.75,
        "median": 7.75,
    }
    with pytest.raises(ValueError):
        g.summary([])


def test_w1_2_word_count():
    assert t.word_count("Python is clear. Python is powerful!") == {
        "python": 2,
        "is": 2,
        "clear": 1,
        "powerful": 1,
    }


def test_w1_3_thesis():
    assert r.can_register_thesis(125, 2.5)


def test_w1_4_translate():
    arr = [1, 3, 5, 7, 9, 11]
    assert tr.binary_search(arr, 7) == 3
    assert tr.binary_search(arr, 2) == -1


def test_w1_5_by_day():
    assert tt.by_day([("INT10001", "Wed")]) == {"Wed": ["INT10001"]}