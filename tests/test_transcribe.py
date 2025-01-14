# write tests for transcribe functions
import pytest 

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    assert transcribe('ATGCCCATG') == 'UACGGGUAC'

    with pytest.raises(ValueError):
        assert transcribe('AUGCCCAUGX')


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    assert transcribe('ATGCCCATG', True) == 'CAUGGGCAU'
    assert reverse_transcribe('UACGGGUAC') == 'CAUGGGCAU'