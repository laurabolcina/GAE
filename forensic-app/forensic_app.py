# coding=utf-8
__author__ = "Laura Bolčina"

def find_criminal(dna):
    """ Returns criminal's properties based on entered DNA. """
    criminal = []

    race_dna = ["AAAACCTCA", "CGACTACAG", "CGCGGGCCG"]
    race = ["white", "black", "Asian"]

    gender_dna = ["TGCAGGAACTTC", "TGAAGGACCTTC"]
    gender = ["male", "female"]

    hair_colour_dna = ["CCAGCAATCGC", "GCCAGTGCCG", "TTAGCTATCGC"]
    hair_colour = ["black", "brown", "ginger"]

    eye_colour_dna = ["TTGTGGTGGC", "GGGAGGTGGC", "AAGTAGTGAC"]
    eye_colour = ["blue", "green", "brown"]

    face_dna = ["GCCACGG", "ACCACAA", "AGGCCTCA"]
    face = ["square", "round", "oval"]

    race_base = zip(race_dna, race)
    gender_base = zip(gender_dna, gender)
    hair_base = zip(hair_colour_dna, hair_colour)
    eye_base = zip(eye_colour_dna, eye_colour)
    face_base = zip(face_dna, face)

    database = race_base + gender_base + hair_base + eye_base + face_base

    for i in database:
        if dna.find(i[0]) != -1:
           criminal.append(i[1])

    properties = ["race", "gender", "hair colour", "eye colour", "face shape"]
    criminal_profile = dict(zip(properties, criminal))
    return criminal_profile

if __name__ == "__main__":
    test = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
    print find_criminal(test)