import gradio as gr
from pages import interfaces
from spacy_functions import CONFIG


app = gr.TabbedInterface(interfaces, CONFIG['tab_names'], title="Spacy Token Classification")


if __name__ == "__main__":
    app.launch()