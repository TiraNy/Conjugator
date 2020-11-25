present_simple_suffices = {"ar": ["o", "as", "a", "amos", "ais", "an"],
                           "er": ["o", "es", "e", "emos", "eis", "en"],
                           "ir": ["o", "es", "e", "imos", "is", "en"]}

past_simple_suffices = {"ar": ["e", "aste", "o", "amos", "asteis", "aron"],
                        "er": ["i", "iste", "io", "imos", "isteis", "ieron"],
                        "ir": ["i", "iste", "io", "imos", "isteis", "ieron"]}

imperfect_suffices = {"ar": ["aba", "abas", "aba", "abamos", "abais", "aban"],
                      "er": ["ia", "ias", "ia", "iamos", "iais", "ian"],
                      "ir": ["ia", "ias", "ia", "iamos", "iais", "ian"]}

subjunctive_suffices = {"ar": ["e", "es", "e", "emos", "eis", "en"],
                      "er": ["a", "as", "a", "amos", "ais", "an"],
                      "ir": ["a", "as", "a", "amos", "ais", "an"]}

future_suffices = {"ar": ["e", "as", "a", "emos", "eis", "as"],
                   "er": ["e", "as", "a", "emos", "eis", "as"],
                   "ir": ["e", "as", "a", "emos", "eis", "as"]}

personal_pronouns = ["yo", "tu", "el/ella/usted", "nosotros/as", "vosotros/as", "ellos/ellas/ustedes"]

estar_present = ["estoy", "estas", "esta", "estamos", "estais", "estan"]

haber_present = ["he", "has", "ha", "habemos", "habeis", "han"]

haber_imperfect = ["habia", "habias", "habia", "habiamos", "habiais", "habian"]

haber_future = ["habre", "habras", "habra", "habremos", "habreis", "habran"]

class Conjugator():
    def __init__(self, infinitive):
        self.__infinitive = infinitive

    @property
    def infinitive(self):
        return self.__infinitive

    @property
    def stem(self):
        return self.infinitive[:-2]

    @property
    def ending(self):
        return self.infinitive[-2:]

    def present_participle(self):
        stem = self.stem
        ending = self.ending
        if ending == "ar":
            output = stem + "ando"
        elif ending == "er":
            output = stem + "iendo"
        elif ending == "ir":
            output = stem + "iendo"
        return output

    def past_participle(self):
        stem = self.stem
        ending = self.ending
        if ending == "ar":
            output = stem + "ado/ada"
        elif ending == "er":
            output = stem + "ido/ida"
        elif ending == "ir":
            output = stem + "ido/ida"
        return output

    def present_simple(self):
        stem = self.stem
        ending = self.ending
        suffices = present_simple_suffices[ending]
        present_simple_verbs = []
        for item in suffices:
            verb = stem + item
            present_simple_verbs.append(verb)
        present_simple_output = []
        for pronoun, verb in zip(personal_pronouns, present_simple_verbs):
            present_simple_output.append("{} {}".format(pronoun, verb))
        return present_simple_output

    def present_progressive(self):
        participle = self.present_participle()
        present_progressive_output = []
        for pronoun, verb in zip(personal_pronouns, estar_present):
            present_progressive_output.append("{} {} {}".format(pronoun, verb, participle))
        return present_progressive_output


    def past_simple(self):
        stem = self.stem
        ending = self.ending
        suffices = past_simple_suffices[ending]
        past_simple_verbs = []
        for item in suffices:
            verb = stem + item
            past_simple_verbs.append(verb)
        past_simple_output = []
        for pronoun, verb in zip(personal_pronouns, past_simple_verbs):
            past_simple_output.append("{} {}". format(pronoun, verb))
        return past_simple_output

    def imperfect(self):
        stem = self.stem
        ending = self.ending
        suffices = imperfect_suffices[ending]
        imperfect_verbs = []
        for item in suffices:
            verb = stem + item
            imperfect_verbs.append(verb)
        imperfect_output = []
        for pronoun, verb in zip(personal_pronouns, imperfect_verbs):
            imperfect_output.append("{} {}".format(pronoun, verb))
        return imperfect_output

    def subjunctive(self):
        stem = self.stem
        ending = self.ending
        suffices = subjunctive_suffices[ending]
        subjunctive_verbs = []
        for item in suffices:
            verb = stem + item
            subjunctive_verbs.append(verb)
        subjunctive_output = []
        for pronoun, verb in zip(personal_pronouns, subjunctive_verbs):
            subjunctive_output.append("{} {}".format(pronoun, verb))
        return subjunctive_output

    def future(self):
        stem = self.stem
        ending = self.ending
        suffices = future_suffices[ending]
        future_verbs = []
        for item in suffices:
            verb = stem + item
            future_verbs.append(verb)
        future_output = []
        for pronoun, verb in zip(personal_pronouns, future_verbs):
            future_output.append("{} {}".format(pronoun, verb))
        return future_output

    def present_perfect(self):
        participle = self.past_participle()
        present_perfect_output = []
        for pronoun, verb in zip(personal_pronouns, haber_present):
            present_perfect_output.append("{} {} {}".format(pronoun, verb, participle))
        return present_perfect_output

    def past_perfect(self):
        participle = self.past_participle()
        past_perfect_output = []
        for pronoun, verb in zip(personal_pronouns, haber_imperfect):
            past_perfect_output.append("{} {} {}".format(pronoun, verb, participle))
        return past_perfect_output

    def future_perfect(self):
        participle = self.past_participle()
        future_perfect_output = []
        for pronoun, verb in zip(personal_pronouns, haber_future):
            future_perfect_output.append("{} {} {}". format(pronoun, verb, participle))
        return future_perfect_output

