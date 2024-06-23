import gradio as gr

from pages import CONFIG, interfaces

app = gr.TabbedInterface(interfaces, CONFIG['tab_names'], title="Spacy Token Classification")


if __name__ == "__main__":
    app.launch()