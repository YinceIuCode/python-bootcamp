
def test_w1_1(load):
	test = load("w1", "grades")
	assert test.summary([1.25, 5.25, 7.7, 4.6]) == {
		'min': 1.25,
		'max': 7.7,
		'mean': 4.7,
		'median': 4.92
	}
	assert test.summary([0, 10, 10, 10, 0, 10, 0, 0 ,10]) == {
		'min': 0,
		'max': 10,
		'mean': 5.56,
		'median': 10
	}

def test_w1_2(load):
	test = load("w1", "text_tools")
	assert test.word_count("foo bar boom foo quux boom baz bar") == {'foo': 2, 'bar': 2, 'boom': 2, 'quux': 1, 'baz': 1}
	assert test.top_k("Quia id ut omnis id ut distinctio nisi.", 2) == [('id', 2), ('ut', 2)]

def test_w1_3(load):
	test = load("w1", "rules")
	assert test.missing(120, 2) == []
	assert test.missing(110, 2) == ['need 10 more credits']
	assert test.missing(130, 1.5) == ['need 0.5 more gpa']
	assert len(test.missing(100, 1)) == 2
	assert len(test.missing(120, 2)) == 0
	assert test.can_register_thesis(120, 2) == True
	assert test.can_register_thesis(119, 2) == False

def test_w1_4(load):
	test = load("w1", "translate")
	assert test.fibonacci(20) == 6765
	assert test.fibonacci(40) == 102334155
	assert test.fibonacci(0) == 0
	assert test.fibonacci(2) == 1

def test_w1_5(load):
	test = load("w1", "timetable")
	assert test.by_day([("CSC100014", "Mon"), ("MTH100003", "Tue"), ("CSC100001", "Mon")]) == {'Mon': ['CSC100001', 'CSC100014'], 'Tue': ['MTH100003']}
	assert test.by_day([("CSC100001", "Sun"), ("CSC100003", "Sun"), ("CSC100002", "Sun"), ("CSC100005", "Wed"), ("CSC100004", "Sun")]) == {'Sun': ['CSC100001', 'CSC100002', 'CSC100003', 'CSC100004'], 'Wed': ['CSC100005']}
	assert test.by_day([("CSC100001", "Wed"), ("CSC100003", "Sun"), ("CSC100002", "Sun"), ("CSC100005", "Wed"), ("CSC100004", "Sun")]) == {'Wed': ['CSC100001', 'CSC100005'], 'Sun': ['CSC100002', 'CSC100003', 'CSC100004']}
	assert test.by_day([("CSC100001", "Sun"), ("CSC100003", "Wed"), ("CSC100002", "Sun"), ("CSC100005", "Wed"), ("CSC100004", "Sun")]) == {'Sun': ['CSC100001', 'CSC100002', 'CSC100004'], 'Wed': ['CSC100003', 'CSC100005']}
	assert test.by_day([("CSC100001", "Wed"), ("CSC100003", "Wed"), ("CSC100002", "Wed"), ("CSC100005", "Wed"), ("CSC100004", "Wed")]) == {'Wed': ['CSC100001', 'CSC100002', 'CSC100003', 'CSC100004', 'CSC100005']}
