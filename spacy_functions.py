# from typing import List, Optional
import spacy

ALLOWED_MODELS = ["fast", "accurate"]
ACCURATE_MODEL = spacy.load("en_core_web_trf")
FAST_MODEL = spacy.load("en_core_web_sm")



def tokenizer(text: str):
    return [token.text for token in FAST_MODEL(text)]

# def parts_of_speech(text: str, model_name: str):
#     model = load_model(model_name)
#     return [token.pos_ for token in model(text)]

# def named_entity_recognition(text: str, model_name: str, filters: List[Optional[str]] = []):
#     model = load_model(model_name)
#     return [
#         token.ent_type_
#         for token in model(text)
#         if token.ent_type_ not in filters
#     ]
