import logging
import logging.config
import os
import warnings
from typing import List, Optional, Literal

from pandas import DataFrame
import spacy
import spacy.tokens
import yaml

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

with open("src/log_config.yaml", "r") as log:
    logging.config.dictConfig(yaml.load(log, yaml.SafeLoader))
    logger = logging.getLogger("primary")
    logger.setLevel(logging.DEBUG)


ModelCatalogue = {"fast": "en_core_web_sm", "accurate": "en_core_web_trf"}
Entities = {'CARDINAL', 'GPE', 'DATE', 'PERSON', 'EVENT', 'ORG', 'OTHERS'}

def generateJobToken() -> str:
    return os.urandom(8).hex()


def validateText(text: Optional[str], _id: str):
    if len(text) < 10 or text is None:
        logger.warning(f"({_id}) invalid string passed as input")
        return False
    
    logger.debug(f"({_id}) input string is valid")
    return True


def load_model(model_name: str, _id: str):
    _model = ModelCatalogue[model_name]
    logger.debug(f"({_id}) Loading model: {_model}")
    return spacy.load(_model)


def tokenizer(text: Optional[str]):
    _id = generateJobToken()
    
    if not validateText(text, _id):
        return None
    
    model = load_model("fast", _id)
    
    tokens = [token.text for token in model(text)]
    logger.info(f"({_id}) Tokenization... Done. Found {len(tokens)} tokens")
    
    return tokens


def partsOfSpeech(text: Optional[str], model_name: str):
    _id = generateJobToken()
    
    if not validateText(text, _id):
        return None
    
    model = load_model(model_name, _id)
    
    tokens = [token.text for token in model(text)]
    pos = [token.pos_ for token in model(text)]
    
    logger.info(f"({_id}) Tokenization... Done. Found {len(tokens)} tokens")
    logger.info(f"({_id}) POS Tagging... Done. Found {len(set(tokens))} unique tags")
    
    return DataFrame({"Token": tokens, "Part of Speech": pos})
    
 
def namedEntityRecognition(text: Optional[str], model_name: Literal["fast", "accurate"],  filters: List[str]):
    _id = generateJobToken()
    
    if not validateText(text, _id):
        return None
    
    model = load_model(model_name, _id)
    
    tokens = [token.text for token in model(text)]
    ner = [
        "OTHER" if token.ent_type_ == "" else token.ent_type_
        for token in model(text)
        if token.ent_type_ not in filters 
    ]

    logger.info(f"({_id}) Tokenization... Done. Found {len(tokens)} tokens")
    logger.info(f"({_id}) Entities... Done. Found {len(ner)} tokens")
    return DataFrame({"Token": tokens, "Entity": ner})
