import romkan


class VerbConjugator:

    endings_kanas = {
        "う": "い",
        "く": "き",
        "す": "し",
        "つ": "ち",
        "ぬ": "に",
        "ぶ": "び",
        "む": "み",
        "る": "り",
        "ぐ": "ぎ",
        "じゅ": "じ",

    }

    def __init__(self, verb):
        self.verb = verb

    def verb_root(self):
        hiragana = self.verb.hiragana[:-1]
        last_kana = self.verb.hiragana[-1]

        if self.verb.group == 1:
            last_kana = self.endings_kanas[last_kana]
            return hiragana + last_kana
        if self.verb.group == 2:
            return hiragana
        if self.verb.group == 3:
            last_kana = self.endings_kanas[hiragana[-1]]
            return hiragana[:-1] + last_kana

    def to_masu(self):
        # Present / Future
        if self.verb.group == 0:
            return "です"
        return self.verb_root() + "ます"

    def to_masen(self):
        # Negative present / negative future
        if self.verb.group == 0:
            return "では　ありません"
        return self.verb_root() + "ません"

    def to_mashita(self):
        # Past
        if self.verb.group == 0:
            return "でした"
        return self.verb_root() + "ました"

    def to_masen_deshita(self):
        # Negative past
        if self.verb.group == 0:
            return "では　ありません　でした"
        return self.verb_root() + "ません　でした"

    def to_te(self):
        # て　form
        return "-"