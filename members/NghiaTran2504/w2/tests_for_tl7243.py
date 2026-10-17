import sys
from pathlib import Path

import pytest

curr_dir = Path(__file__).resolve().parents[3]
if str(curr_dir) not in sys.path:
    sys.path.insert(0, str(curr_dir))
    
from members.tl7243.w1.grades import summary
from members.tl7243.w1.rules import can_register_thesis, missing
from members.tl7243.w1.text_tools import top_k
from members.tl7243.w1.timetable import by_day
from members.tl7243.w1.translate import primes_up_to


def test_w1_1_summary_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        summary([])


def test_w1_2_top_k_punctuation_and_sorting():
    text = "Git is fun. Git is fast!"
    assert top_k(text, 2) == [("git", 2), ("is", 2)]


def test_w1_3_thesis_missing_reasons_edge_case():
    assert can_register_thesis(110, 1.8) is False
    reasons = missing(110, 1.8)
    assert isinstance(reasons, list) and len(reasons) >= 1


def test_w1_4_sieve_of_eratosthenes():
    assert primes_up_to(10) == [2, 3, 5, 7]
    assert primes_up_to(1) == []
    assert primes_up_to(-1) == []
    assert len(primes_up_to(100)) == 25
    assert primes_up_to(100)[-1] == 97



def test_w1_5_by_day_grouping_and_sorting():
    schedule = [("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]
    assert by_day(schedule) == {"Mon": ["CSC10001", "CSC10014"], "Tue": ["MTH00003"]}