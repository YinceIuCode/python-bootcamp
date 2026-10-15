import pytest
import sys
from pathlib import Path

bootcamp_dir = Path(__file__).resolve().parents[3]
if str(bootcamp_dir) not in sys.path:
    sys.path.insert(0, str(bootcamp_dir))

from members.tl7243.w1.translate import primes_up_to

def test_sieve_basic_small():
    assert primes_up_to(10) == [2, 3, 5, 7]

def test_sieve_boundary_two():
    assert primes_up_to(2) == [2]

def test_sieve_edge_case_less_than_two():
    assert primes_up_to(1) == []
    assert primes_up_to(0) == []
    assert primes_up_to(-10) == []


def test_sieve_composite_limit():
    res = primes_up_to(25)
    assert 23 in res
    assert 25 not in res

def test_sieve_larger_n():
    res = primes_up_to(100)
    assert len(res) == 25 
    assert res[-1] == 97