import gradio as gr
import pages
import pages.ner
import pages.parts_of_speech
import pages.tokenizer

tab_names = ["Tokenizer", "Parts of Speech", "Named Entity Recognition"]
ifaces = [
    pages.tokenizer.Tokenizer,
    pages.parts_of_speech.PartsOfSpeech,
    pages.ner.NamedEntityRecognition
]

assert len(ifaces) == len(tab_names)

app = gr.TabbedInterface(
    interface_list = ifaces,
    tab_names = tab_names,
    title = "Spacy Token Classifer"
)

if __name__ == "__main__":
    app.launch()
