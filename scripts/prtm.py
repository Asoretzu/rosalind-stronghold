from services import fasta
from services.search import amino_mass


def prtm(file_name):
    """
    Prints the total weight of a given protein.

    Keyword arguments:
    file_name -- The path of the txt file to be parsed.


    Calculating Protein Mass

    In a weighted alphabet, every symbol is assigned a positive real number
    called a weight. A string formed from a weighted alphabet is called a
    weighted string, and its weight is equal to the sum of the weights of its
    symbols.

    The standard weight assigned to each member of the 20-symbol amino acid
    alphabet is the monoisotopic mass of the corresponding amino acid.

    Given: A protein string P of length at most 1000 aa.

    Return: The total weight of P.

    Sample Dataset
    SKADYEK

    Sample Output
    821.392

    A   71.03711
    C   103.00919
    D   115.02694
    E   129.04259
    F   147.06841
    G   57.02146
    H   137.05891
    I   113.08406
    K   128.09496
    L   113.08406
    M   131.04049
    N   114.04293
    P   97.05276
    Q   128.05858
    R   156.10111
    S   87.03203
    T   101.04768
    V   99.06841
    W   186.07931
    Y   163.06333
    """

    data = fasta.get(file_name)
    mass = 0
    for amino in data:
        mass = mass + amino_mass(amino)

    print(round(mass, 3))
