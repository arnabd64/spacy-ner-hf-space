import gradio as gr
from spacy_functions import CONFIG, parts_of_speech

with gr.Blocks() as PartsOfSpeech:
    with gr.Row():
        with gr.Column():
            gr.Markdown("__Enter your Text__:")
            with gr.Row():
                text_input = gr.Textbox()
            
            gr.Markdown("__Choose Language Model__:")
            with gr.Row():
                model = gr.Radio(choices=CONFIG['allowed_model'], value=CONFIG['allowed_models'][0])
            
            with gr.Row():
                with gr.Column():
                    submit = gr.Button("Tag Parts of Speech")

                with gr.Column():
                    gr.ClearButton([text_input])

        with gr.Column():
            gr.Markdown("__Tokens Found__")
            tokens_list = gr.DataFrame()

    submit.click(parts_of_speech, [text_input, model], tokens_list)
