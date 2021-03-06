from services import fasta
from services import translate


def splc(file_name):
    """
    Prints a protein string resulting from transcribing and translating the
    exons of a base string.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    RNA Splicing

    After identifying the exons and introns of an RNA string, we only need to
    delete the introns and concatenate the exons to form a new string ready for
    translation.

    Given: A DNA string s (of length at most 1 kbp) and a collection of
    substrings of s acting as introns. All strings are given in FASTA format.

    Return: A protein string resulting from transcribing and translating the
    exons of s. (Note: Only one solution will exist for the dataset provided.)

    Sample Dataset

    >Rosalind_10
    ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCG
    AGCGTGTTTCAAAGTTTGCGCCTAG
    >Rosalind_12
    ATCGGTCGAA
    >Rosalind_15
    ATCGGTCGAGCGTGT

    Sample Output
    MVYIADKQHVASREAYGHMFKVCA
    """

    dataset = fasta.get(file_name)
    introns = []

    # Asign DNA string
    dna = dataset[1][0]

    # Asign introns
    for i in range(1, len(dataset[1])):
        introns.append(dataset[1][i])

    # Get the exons of the DNA string
    for intron in introns:
        dna = dna.replace(intron, "")

    # Translate DNA to mRNA, and to amino acids
    rna = translate.to_rna(dna)
    protein = translate.to_protein(rna)

    print(protein)
