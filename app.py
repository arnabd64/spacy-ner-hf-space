import gradio as gr
from tokenizer import tokenizer
from parts_of_speech import parts_of_speech
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

iface_list = [tokenizer, parts_of_speech]
tab_names = ["Tokenizer", "Parts of Speech"]

assert len(iface_list) == len(tab_names)

app = gr.TabbedInterface(
    interface_list = iface_list,
    tab_names = tab_names,
    title = "Spacy Token Classifer"
)

if __name__ == "__main__":
    app.launch(
        server_port=7860,
        server_name = "0.0.0.0"
    )