# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    if all(x in 'ATCG' for x in seq):
        # if reverse transcription, feed transcribed seq to reverse_transcribe()
        if reverse:
            return reverse_transcribe(''.join(map(lambda x: TRANSCRIPTION_MAPPING.get(x, x), seq)))
        # else, return mapping from DNA to RNA
        else:
            return ''.join(map(lambda x: TRANSCRIPTION_MAPPING.get(x, x), seq))
    else:
        raise ValueError('Sequence includes invalid nucelotides.')

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return seq[::-1]