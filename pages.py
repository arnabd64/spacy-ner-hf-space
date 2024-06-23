from spacy_functions import CONFIG, tokenizer, named_entity_recognition, parts_of_speech
import gradio as gr
import spacy
import sys


with gr.Blocks() as Tokenizer:
    with gr.Row():
        with gr.Column():
            gr.Markdown("__Enter your Text__:")
            with gr.Row():
                text_input = gr.Textbox()
            
            with gr.Row():
                with gr.Column():
                    submit = gr.Button("Tokenize")

                with gr.Column():
                    gr.ClearButton([text_input])

        with gr.Column():
            gr.Markdown("__Tokens Found__:")
            tokens_list = gr.JSON()

    submit.click(tokenizer, [text_input], tokens_list)

with gr.Blocks() as PartsOfSpeech:
    with gr.Row():
        with gr.Column():
            gr.Markdown("__Enter your Text__:")
            with gr.Row():
                text_input = gr.Textbox()
            
            gr.Markdown("__Choose Language Model__:")
            with gr.Row():
                model = gr.Radio(CONFIG['allowed_models'], value=CONFIG['allowed_models'][0])
            
            with gr.Row():
                with gr.Column():
                    submit = gr.Button("Tag Parts of Speech")

                with gr.Column():
                    gr.ClearButton([text_input])

        with gr.Column():
            gr.Markdown("__Tokens Found__")
            tokens_list = gr.DataFrame()

    submit.click(parts_of_speech, [text_input, model], tokens_list)

with gr.Blocks() as NamedEntityRecognition:
    with gr.Row():
        with gr.Column():
            gr.Markdown("__Enter your Text__:")
            with gr.Row():
                text_input = gr.Textbox()

            gr.Markdown("__Choose Language Model__:")
            with gr.Row():
                model = gr.Radio(CONFIG['allowed_models'], value=CONFIG['allowed_models'][0])
                
            gr.Markdown("__Choose Entities to Hide__:")
            with gr.Row():
                filters = gr.CheckboxGroup(CONFIG['entities'])

            with gr.Row():
                with gr.Column():
                    submit = gr.Button("Recognize Entities")

                with gr.Column():
                    gr.ClearButton([text_input, filters])

        with gr.Column():
            gr.Markdown("__Entities Found__:")
            entity_list = gr.DataFrame()

    submit.click(named_entity_recognition, [text_input, model, filters], entity_list)

with gr.Blocks() as About:
    gr.Markdown("## About")
    gr.Markdown("* Author: [arnabdhar](https://hf.co/arnabdhar)")
    gr.Markdown("* Author's GitHub: [arnabd64](https://github.com/arnabd64)")

    gr.Markdown("## Package versions")
    gr.Markdown(f"* Python: {sys.version}")
    gr.Markdown(f"* Spacy: {spacy.__version__}")
    gr.Markdown(f"* Gradio: {gr.__version__}")

interfaces = [Tokenizer, PartsOfSpeech, NamedEntityRecognition, About]