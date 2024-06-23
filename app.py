import gradio as gr
from pages import Tokenizer, PartsOfSpeech, NamedEntityRecognition
from spacy_functions import CONFIG

ifaces = [Tokenizer, PartsOfSpeech, NamedEntityRecognition]

app = gr.TabbedInterface(ifaces, CONFIG['tab_names'], title="Spacy Token Classification")


if __name__ == "__main__":
    app.launch()