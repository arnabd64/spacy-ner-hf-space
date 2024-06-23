import logging
import logging.config
import secrets
import warnings
from typing import List, Optional

import spacy
import spacy.tokens
import yaml
from pandas import DataFrame

warnings.filterwarnings("ignore", category=UserWarning)

with open("log_config.yaml", "r") as log:
    logging.config.dictConfig(yaml.load(log, yaml.SafeLoader))
    logger = logging.getLogger("primary")    

class SpacyTask:

    def __init__(self, text: str, model_name: str):
        self.text = text
        self.model_name = model_name
        self._id = secrets.token_hex(4)

    def _log(self, message: str):
        return f"({self._id}) - {message}"

    @property
    def validate_text(self):
        if self.text == "" or self.text is None:
            logger.warning(self._log("empty string or None value passed as text input."))
            return False
        
        logger.debug(self._log('vaid string passed as text_input'))
        return True
    
    @property
    def model(self):
        if self.model_name == "fast":
            logger.info(self._log("loading en_core_web_sm"))
            return spacy.load("en_core_web_sm")
        
        elif self.model_name == "accurate":
            logger.info(self._log("loading en_core_web_trf"))
            return spacy.load("en_core_web_trf")
        
        else:
            logger.warning(self._log(f"model_name={self.model_name}. Loading default model: en_core_web_sm"))
            return spacy.load("en_core_web_sm")
        

    def tokenizer(self):
        """
        Tokenizes the input text and returns the list of tokens
        """
        if not self.validate_text:
            return []
        
        tokens = [token.text for token in self.model(self.text)]
        logger.info(self._log(f"Tokenizer found {len(tokens)} token(s)"))
        return tokens
    
    def parts_of_speech(self):
        """
        Tokenizes the text and assigns each token a POS tag
        """
        tokens = list()
        pos = list()

        if not self.validate_text:
            return None
        
        _doc = self.model(self.text)
        
        for token in _doc:
            tokens.append(token.text)
            pos.append(token.pos_)

        logger.info(self._log(f"Tokenizer found {len(tokens)} token(s)"))
        logger.info(self._log(f"POS Tagger found {len(set(pos))} unique tag(s)"))
        return {"tokens": tokens, "tags": pos}
    
    def named_entity_recognition(self, filters: List[Optional[str]] = []):
        """
        Tokenizes the text and assigns each token a NER tag.
        """
        tokens = list()
        ner = list()

        if not self.validate_text:
            return None
        
        _doc = self.model(self.text)
        
        for token in _doc:
            if token.ent_type_ not in filters:
                tokens.append(token.text)
                if token.ent_type_ == "":
                    ner.append("OTHER")
                else:
                    ner.append(token.ent_type_)

        logger.info(self._log(f"Tokenizer found {len(tokens)} token(s)"))
        logger.info(self._log(f"NER found {len(set(ner))} entity(s)"))
        return {"tokens": tokens, "entities": ner}


with open("config.yaml", "r") as fp:
    CONFIG = yaml.load(fp, yaml.SafeLoader)


def tokenizer(text: str):
    return SpacyTask(text, "fast").tokenizer()


def parts_of_speech(text: str, model_name: str):
    _output = SpacyTask(text, model_name).parts_of_speech()
    if _output is not None:
        return DataFrame.from_dict(_output)
    else:
        return None

def named_entity_recognition(text: str, model_name: str, filters: List[Optional[str]] = []):
    _output = SpacyTask(text, model_name).named_entity_recognition(filters)
    if _output is not None:
        return DataFrame.from_dict(_output)
    else:
        return None
