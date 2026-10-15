import pytest


def test_w1_1_summary(load):
    g = load("w1", "grades")

    assert g.summary([8.5, 9.5, 7.0, 6.0]) == {
        "min": 6.0,
        "max": 9.5,
        "mean": 7.75,
        "median": 7.75,
    }
    assert g.summary([9.0])["median"] == 9.0
    assert g.summary([7.5, 7.5, 7.5]) == {
        "min": 7.5,
        "max": 7.5,
        "mean": 7.5,
        "median": 7.5,
    }
    assert g.summary([12, 24, 36, 48]) == {
        "min": 12,
        "max": 48,
        "mean": 30.0,
        "median": 30.0,
    }

    with pytest.raises(ValueError):
        g.summary([])


def test_w1_2_word_count(load):
    t = load("w1", "text_tools")

    assert t.word_count("Python is clear. Python is powerful!") == {
        "python": 2,
        "is": 2,
        "clear": 1,
        "powerful": 1,
    }
    assert t.top_k("Python is clear. Python is powerful!", 2) == [
        ("python", 2),
        ("is", 2),
    ]
    assert t.word_count("   ??? *** ### ") == {}
    assert t.top_k("   ??? *** ### ", 3) == []
    assert t.top_k("data science", 4) == [("data", 1), ("science", 1)]
    assert t.word_count("{Code}, <clean>! Code?") == {"code": 2, "clean": 1}


def test_w1_3_thesis(load):
    r = load("w1", "rules")

    assert r.can_register_thesis(125, 2.5)
    assert not r.can_register_thesis(115, 3.2)
    assert r.missing(115, 3.2) == ["need 5 more credits"]
    assert r.missing(125, 2.5) == []
    assert len(r.missing(105, 1.2)) == 2
    assert r.can_register_thesis(135, 3.6)
    assert r.missing(145, 3.9) == []
    assert r.missing(120, 1.7) == ["need 0.3 more gpa"]


def test_w1_4_translate(load):
    tr = load("w1", "translate")

    assert tr.transpose([[10, 20, 30], [40, 50, 60]]) == [
        [10, 40],
        [20, 50],
        [30, 60],
    ]
    assert tr.transpose([]) == []
    assert tr.transpose([[2, 4, 6], [8, 10, 12], [14, 16, 18]]) == [
        [2, 8, 14],
        [4, 10, 16],
        [6, 12, 18],
    ]
    assert tr.transpose([[5, 15, 25]]) == [[5], [15], [25]]
    assert tr.__doc__ or any(
        getattr(tr, n).__doc__ for n in dir(tr) if callable(getattr(tr, n))
    )


def test_w1_5_by_day(load):
    tt = load("w1", "timetable")

    got = tt.by_day([("INT10001", "Wed"), ("MTH00005", "Thu"), ("INT10002", "Wed")])
    assert got == {"Wed": ["INT10001", "INT10002"], "Thu": ["MTH00005"]}
    assert tt.by_day([]) == {}
    input_timetable = [("Gamma", "Sat"), ("Delta", "Sat"), ("Epsilon", "Tue")]
    assert tt.by_day(input_timetable) == {
        "Tue": ["Epsilon"],
        "Sat": ["Delta", "Gamma"],
    }