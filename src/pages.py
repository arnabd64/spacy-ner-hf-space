import sys

import gradio as gr
import gradio.components as gc
import spacy

import src.functions as f


ModelChooser = lambda: gc.Radio(list(f.ModelCatalogue.keys()), label="Choose You Model")
TextInput = lambda: gc.Textbox(label="Enter your Text:")


with gr.Blocks() as Tokenizer:
    with gr.Row():
        with gr.Column():
            with gr.Row():
                text_input = TextInput()
            
            with gr.Row():
                with gr.Column():
                    submit = gc.Button("Tokenize")

                with gr.Column():
                    gc.ClearButton([text_input])

        with gr.Column():
            tokens_list = gc.JSON(label="Tokens Found")

    submit.click(f.tokenizer, [text_input], tokens_list)

with gr.Blocks() as PartsOfSpeech:
    with gr.Row():
        with gr.Column():
            with gr.Row():
                text_input = TextInput()
            
            with gr.Row():
                model = ModelChooser()
            
            with gr.Row():
                with gr.Column():
                    submit = gr.Button("Tag Parts of Speech")

                with gr.Column():
                    gr.ClearButton([text_input])

        with gr.Column():
            tokens_list = gc.DataFrame(label="Tokens Found")

    submit.click(f.partsOfSpeech, [text_input, model], tokens_list)

with gr.Blocks() as NamedEntityRecognition:
    with gr.Row():
        with gr.Column():
            with gr.Row():
                text_input = TextInput()

            with gr.Row():
                model = ModelChooser()
                
            with gr.Row():
                filters = gr.CheckboxGroup(f.Entities, label="Entities to Hide:")

            with gr.Row():
                with gr.Column():
                    submit = gr.Button("Recognize Entities")

                with gr.Column():
                    gr.ClearButton([text_input, filters])

        with gr.Column():
            entity_list = gc.DataFrame(label="Entities Found")

    submit.click(f.namedEntityRecognition, [text_input, model, filters], entity_list)

with gr.Blocks() as About:
    gr.Markdown("## About")
    gr.Markdown("* Author: [arnabdhar](https://hf.co/arnabdhar)")
    gr.Markdown("* Author's GitHub: [arnabd64](https://github.com/arnabd64)")

    gr.Markdown("## Package versions")
    gr.Markdown(f"* Python: {sys.version}")
    gr.Markdown(f"* Spacy: {spacy.__version__}")
    gr.Markdown(f"* Gradio: {gr.__version__}")

Interfaces = {
    "Tokenizer": Tokenizer,
    "Parts of Speech": PartsOfSpeech,
    "Named Entity Recognition": NamedEntityRecognition,
    "About":  About
}
