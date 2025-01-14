# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser_goodFile():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    testFasta = FastaParser('data/test.fa')
    numSeq = 0
    for record in testFasta:
        numSeq+=1 # incriment counter for num seq test
        # Check that values are assigned to both record slots based on expected formating:
        assert record[0].startswith("seq") and record[1].startswith(tuple(["A","T","C","G"]))
    # Check that number of records is the same as expected
    assert numSeq==100

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # Check that fasta parser behaves as expected when used to read in fastq file
    fastq_fastaParse = FastaParser('data/test.fq')
    out = []
    for record in fastq_fastaParse:
        # extract records for easier checking
        out.append(record[0])
    assert len(out) != 100 # length will be longer than expected (100) if using fasta parsing rules for fastq format
    # check that first element is None as specified in test prompt
        ## not a generalized test because many of the first elements are actually not None, likely because 
        ## quality scores sometimes include the ">" character
    assert out[0] == None 

def test_FastqParser_goodFile():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    testFastq = FastqParser('data/test.fq')
    numSeq = 0
    for record in testFastq:
        numSeq+=1 # incriment counter for num seq test
        # Check that values are assigned to both record slots based on expected formating:
        assert record[0].startswith("seq") and record[1].startswith(tuple(["A","T","C","G"])) and record[2]!=None
    # Check that number of records is the same as expected
    assert numSeq==100

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # Check that fastq parser behaves as expected when used to read in fasta file
    fasta_fastqParse = FastqParser('data/test.fa')
    for record in fasta_fastqParse:
        # check that first element is None as specified in test prompt--generalizable in this case
        assert record[0] == None 