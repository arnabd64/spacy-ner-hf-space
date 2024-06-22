# from typing import List, Optional
import spacy
from pandas import DataFrame

ALLOWED_MODELS = ["fast", "accurate"]
ACCURATE_MODEL = spacy.load("en_core_web_trf")
FAST_MODEL = spacy.load("en_core_web_sm")



def tokenizer(text: str):
    return [token.text for token in FAST_MODEL(text)]

def parts_of_speech(text: str, model_name: str):
    model = FAST_MODEL if model_name == "fast" else ACCURATE_MODEL
    doc = model(text)
    return DataFrame.from_dict({
        "token": [token.text for token in doc],
        "pos": [token.pos_ for token in doc]
    })

# def named_entity_recognition(text: str, model_name: str, filters: List[Optional[str]] = []):
#     model = load_model(model_name)
#     return [
#         token.ent_type_
#         for token in model(text)
#         if token.ent_type_ not in filters
#     ]
