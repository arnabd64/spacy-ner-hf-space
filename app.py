import gradio as gr
from tokenizer import tokenizer

app = gr.TabbedInterface(
    interface_list = [tokenizer],
    tab_names = ['Tokenizer'],
    title = "Spacy Token Classifer"
)

if __name__ == "__main__":
    app.launch(
        server_port=7860,
        server_name = "0.0.0.0"
    )