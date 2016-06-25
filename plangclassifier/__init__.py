from .classifier import Classifier
from .samples import DATA

def classify_langs(code, languages=None):
    if languages is None:
        languages = []
    return Classifier.classify(DATA, code, languages=languages)
