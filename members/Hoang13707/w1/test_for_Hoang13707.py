import statistics

import pytest


def test_w1_1(load):
    loaded = load("w1", "grades")
    assert loaded.summary([1, 2, 3]) == {
        'min': min([1, 2, 3]), 
        'max' : max([1, 2, 3]), 
        'mean' : round(statistics.mean([1, 2, 3]), 2), 
        'median' : round(statistics.median([1, 2, 3]), 2)
    }

    assert loaded.summary([1]) == {
        'min': min([1]), 
        'max' : max([1]), 
        'mean' : round(statistics.mean([1]), 2), 
        'median' : round(statistics.median([1]), 2)
    }

    with pytest.raises(ValueError):
        loaded.summary([])
        
    assert loaded.summary([2, 3]) == {
        'min': min([2, 3]), 
        'max' : max([2, 3]), 
        'mean' : round(statistics.mean([2, 3]), 2), 
        'median' : round(statistics.median([2, 3]), 2)
    }
    
    assert loaded.summary([1, 2, 3, 4]) == {
        'min': min([1, 2, 3, 4]), 
        'max' : max([1, 2, 3, 4]), 
        'mean' : round(statistics.mean([1, 2, 3, 4]), 2), 
        'median' : round(statistics.median([1, 2, 3, 4]), 2)
    }
    
def test_w1_2(load):
    loaded = load("w1", "text_tools")
    assert loaded.top_k("Git is fast. Git is fun!", 2) == [('git', 2), ("is", 2)]
    assert len(loaded.top_k("Git is fast. Git is fun!", 1)) == 1
    assert len(loaded.word_count("This is a random test!")) == len({'a': 1, 'is': 1, 'random': 1, 'test': 1, 'this': 1})
    assert loaded.word_count("ABC ABC") == {'abc': 2}
    assert len(loaded.top_k("The quick brown fox jump over the lazy dog.", 2)) != 3
    assert len(loaded.top_k("", 1)) != 4
    
def test_w1_3(load):
    loaded = load("w1", "rules")
    assert loaded.missing(120, 2) == []
    assert loaded.missing(110, 2) == ['need 10 more credits']
    assert ('need 10 more credits' in loaded.missing(110, 1.9)) and (len(loaded.missing(110, 1.9)) == 2)
    assert len(loaded.missing(120, 1.9)) == 1
    assert len(loaded.missing(120, 2)) == 0
    assert loaded.can_register_thesis(120, 2) == True
    assert loaded.can_register_thesis(119, 2) == False
    assert loaded.can_register_thesis(120, 1) == False
    assert loaded.can_register_thesis(130, 3) == True
    assert loaded.can_register_thesis(125, 1) == False
    
def test_w1_5(load):
    loaded = load("w1", "timetable")
    assert loaded.by_day([("CSC100014", "Mon"), ("MTH100003", "Tue"), ("CSC100001", "Mon")]) == {'Mon': ['CSC100001', 'CSC100014'], 'Tue': ['MTH100003']}
    assert loaded.by_day([("CSC100024", "Mon"), ("MTH100053", "Tue"), ("CSC100067", "Mon"), ("CSC100019", "Fri")]) == {'Fri': ['CSC100019'], 'Mon': ['CSC100024', 'CSC100067'], 'Tue': ['MTH100053']}
    assert loaded.by_day([("CSC110014", "Mon"), ("MTH120003", "Mon"), ("CSC130001", "Mon")]) == {'Mon': ['CSC110014', 'CSC130001', 'MTH120003']}
    assert loaded.by_day([("CSC102014", "Mon"), ("MTH101003", "Tue"), ("CSC100301", "Mon"), ("MTH101003", "Sun")]) == {'Mon': ['CSC100301', 'CSC102014'], 'Tue': ['MTH101003'], 'Sun': ['MTH101003']}
    assert loaded.by_day([("CSC100727", "Mon"), ("MTH100333", "Tue"), ("CSC100067", "Mon"), ("MTH100069", "Tue"), ("MTH100069", "Tue")]) == {'Mon': ['CSC100067', 'CSC100727'], 'Tue': ['MTH100069', 'MTH100069', 'MTH100333']}
    
def test_w1_4(load):
    loaded = load("w1", "translate")
    assert loaded.reverse_sequence([1, 2, 3]) == [3, 2, 1]
    assert loaded.reverse_sequence('') == ''
    assert loaded.reverse_sequence('abc123') == '321cba'
    assert loaded.reverse_sequence([]) == []
    assert loaded.reverse_sequence(['']) == ['']
    assert (0 if loaded.reverse_in_place(['a', 'b', 'c']) == None else len(loaded.reverse_in_place(['a', 'b', 'c']))) != 4
    assert (0 if loaded.reverse_in_place(['1', '2', '3']) == None else len(loaded.reverse_in_place(['3', '2', '1']))) != 4
    assert (0 if loaded.reverse_in_place([' ', ' ', ' ']) == None else len(loaded.reverse_in_place([' ', ' ', ' ']))) != 4
    assert (0 if loaded.reverse_in_place(['  ']) == None else len(loaded.reverse_in_place(['  ']))) != 4
    assert (0 if loaded.reverse_in_place(['a']) == None else len(loaded.reverse_in_place(['a']))) != 4
