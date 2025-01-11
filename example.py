from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)
import io

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    fasta = FastaParser(filename="data/test.fa")
    # Create instance of FastqParser
    fastq = FastqParser("data/test.fq")
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    for record in fasta:
        print(record[0])
        print(transcribe(record[1], reverse=False))
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    for record in fastq:
        print(record[0])
        print(transcribe(record[1],reverse=False))

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    for record in fasta:
        print(record[0])
        print(transcribe(record[1], reverse=True))

    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    for record in fastq:
        print(record[0])
        print(transcribe(record[1],reverse=True))


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
