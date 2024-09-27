import gradio as gr

from pages import Interfaces

app = gr.TabbedInterface(list(Interfaces.values()), list(Interfaces.keys()), title="Spacy Token Classification")


if __name__ == "__main__":
    app.launch()