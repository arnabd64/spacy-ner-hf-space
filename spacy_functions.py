from typing import List, Optional
import spacy
from pandas import DataFrame
import warnings
import yaml
import spacy.tokens
warnings.filterwarnings("ignore", category=UserWarning)

ACCURATE_MODEL = spacy.load("en_core_web_trf")
FAST_MODEL = spacy.load("en_core_web_sm")

with open("config.yaml", "r") as fp:
    CONFIG = yaml.load(fp, yaml.SafeLoader)

def tokenizer(text: str):
    return [token.text for token in FAST_MODEL(text)]

def parts_of_speech(text: str, model_name: str):
    model = FAST_MODEL if model_name == "fast" else ACCURATE_MODEL
    doc = model(text)
    return DataFrame.from_dict({
        "token": [token.text for token in doc],
        "pos": [token.pos_ for token in doc]
    })

def _ner(doc: spacy.tokens.Doc):
    return [
        (token.text, token.ent_type_)
        for token in doc
        if not token.ent_type_ == ""
    ]

def named_entity_recognition(text: str, model_name: str, filters: List[Optional[str]] = []):
    model = FAST_MODEL if model_name == "fast" else ACCURATE_MODEL
    doc = model(text)
    tokens = [token for token, ent in _ner(doc) if ent not in filters]
    ents = [ent for _, ent in _ner(doc) if ent not in filters]
    return DataFrame.from_dict({"tokens": tokens, "entities": ents})
