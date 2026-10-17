import pytest

# Import functions from doomsdaycome's w1 directory
from members.doomsdaycome.w1.grades import summary
from members.doomsdaycome.w1.rules import can_register_thesis, missing
from members.doomsdaycome.w1.text_tools import word_count
from members.doomsdaycome.w1.translate import insertion_sort


# 1. Normal test case for W1-1 (grades.py)
def test_summary_normal_scores():
    """Test min, max, mean, and median calculations with a standard dataset."""
    scores = [7.5, 9.0, 6.0, 8.0]
    result = summary(scores)

    assert result["min"] == 6.0
    assert result["max"] == 9.0
    assert result["mean"] == 7.62
    assert result["median"] == 7.75


# 2. EDGE CASE for W1-1 (grades.py)
def test_summary_empty_list_edge_case():
    """
    Edge case: Empty score list.
    The function should raise a ValueError when given an empty list.
    """
    with pytest.raises(ValueError):
        summary([])


# 3. Boundary test case for W1-3 (rules_4.py)
def test_thesis_boundary_conditions():
    """Check exact boundary conditions (120 credits, 2.0 GPA)."""
    # Exact required values -> True
    assert can_register_thesis(120, 2.0) is True
    assert missing(120, 2.0) == []

    # Missing exactly 1 credit -> False
    assert can_register_thesis(119, 2.0) is False
    assert "need 1 more credits" in missing(119, 2.0)

    # Missing exactly 0.1 GPA -> False
    assert can_register_thesis(120, 1.9) is False
    assert "need 0.1 more gpa" in missing(120, 1.9)


# 4. String processing test case for W1-2 (text_tools.py)
def test_word_count_punctuation_and_case():
    """Test punctuation removal and case-insensitive counting."""
    text = "Git! is fun, git IS fast."
    result = word_count(text)

    assert result.get("git") == 2
    assert result.get("is") == 2
    assert result.get("fun") == 1
    assert "Git" not in result  # Ensure everything is converted to lowercase


# 5. EDGE CASE for W1-4 (translate.py)
def test_insertion_sort_edge_cases():
    """
    Edge case: Empty array, single-element array, and array with identical elements.
    Ensures the sorting algorithm does not crash on extremely short or uniform arrays.
    """
    assert insertion_sort([]) == []
    assert insertion_sort([42]) == [42]
    assert insertion_sort([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert insertion_sort([3, -1, 0, 2]) == [-1, 0, 2, 3]
