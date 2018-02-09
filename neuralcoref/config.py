NO_COREF_LIST = ["i", "me", "my", "you", "your"]

MENTION_TYPE = {"PRONOMINAL": 0, "NOMINAL": 1, "PROPER": 2, "LIST": 3}
# MENTION_LABEL = {0: "PRONOMINAL", 1: "NOMINAL", 2: "PROPER", 3: "LIST"}

PROPERS_TAGS = ["NN", "NNS", "NNP", "NNPS"]

ACCEPTED_ENTS = ["PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART", "LAW", "LANGUAGE"]
WHITESPACE_PATTERN = r"\s+|_+"
UNKNOWN_WORD = "*UNK*"
NORMALIZE_DICT = {"/.": ".", "/?": "?", "-LRB-": "(", "-RRB-": ")",
                  "-LCB-": "{", "-RCB-": "}", "-LSB-": "[", "-RSB-": "]"}
DISTANCE_BINS = list(range(5)) + [5]*3 + [6]*8 + [7]*16 +[8]*32