from Conjugator import Conjugator
import re

def print_conjugation(list):
    print("============================================================")
    conjugation = str(list)[1:-1].replace(", ", "\n").replace("\'", "")
    print(conjugation)
    print("============================================================")
    return


def main():
    verb = Conjugator("vivir")
    print(verb.infinitive)
    print(verb.stem)
    print(verb.ending)

    print(verb.present_participle())
    print("Present Simple >> {}".format(verb.infinitive))
    print_conjugation(verb.present_simple())
    print("Past Simple >> {}".format(verb.infinitive))
    print_conjugation(verb.past_simple())
    print("Imperfect >> {}".format(verb.infinitive))
    print_conjugation(verb.imperfect())
    print("Subjunctive >> {}".format(verb.infinitive))
    print_conjugation(verb.subjunctive())
    print("Future >> {}".format(verb.infinitive))
    print_conjugation(verb.future())
    print("Present Progressive >> {}".format(verb.infinitive))
    print_conjugation(verb.present_progressive())
    print("Present Perfect >> {}".format(verb.infinitive))
    print_conjugation(verb.present_perfect())
    print("Past Perfect >> {}".format(verb.infinitive))
    print_conjugation(verb.past_perfect())
    print("Future Perfect >> {}".format(verb.infinitive))
    print_conjugation(verb.future_perfect())

main()