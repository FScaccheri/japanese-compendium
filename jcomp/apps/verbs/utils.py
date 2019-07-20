import romkan


class VerbConjugator:

    normal_roots = {
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

    nai_roots = {
        "う": "わ",
        "く": "か",
        "す": "さ",
        "つ": "た",
        "ぬ": "な",
        "ぶ": "ば",
        "む": "ま",
        "る": "ら",
        "ぐ": "が",
        "じゅ": "じゃ",
    }

    te_suffixes = {
        "い": "って",
        "き": "いて",
        "し": "して",
        "ち": "って",
        "に": "んで",
        "び": "んで",
        "み": "んで",
        "り": "って",
        "ぎ": "いで",
    }

    def __init__(self, verb):
        self.verb = verb

    def verb_root(self):
        hiragana = self.verb.hiragana[:-1]
        last_kana = self.verb.hiragana[-1]

        if self.verb.group == 1:
            last_kana = self.normal_roots[last_kana]
            return hiragana + last_kana
        if self.verb.group == 2:
            return hiragana
        if self.verb.group == 3:
            last_kana = self.normal_roots[hiragana[-1]]
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
        if self.verb.group == 0:
            return "-"
        
        if self.verb.group == 1:
            # Exception:
            if self.verb.hiragana == "いく":
                return "いって"
                
            hiragana = self.verb_root()[:-1]
            last_kana = self.verb_root()[-1]
            te_suffix = self.te_suffixes[last_kana]
            return hiragana + te_suffix
        
        return self.verb_root() + "て"

    def to_nai(self):
        # Informal negative
        if self.verb.group == 0:
            return "ではない"
        return self.verb_root() + "ない"

    def to_nakatta(self):
        # Informal negative past
        if self.verb.group == 0:
            return " - "
        return self.verb_root() + "なかった"
