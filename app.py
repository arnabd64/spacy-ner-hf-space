import gradio as gr

from src.pages import Interfaces

app = gr.TabbedInterface(
    interface_list=list(Interfaces.values()),
    tab_names=list(Interfaces.keys()),
    title="Spacy Token Classification"
)


if __name__ == "__main__":
    app.launch()