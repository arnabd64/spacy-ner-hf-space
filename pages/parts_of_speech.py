import gradio as gr
from spacy_functions import CONFIG, parts_of_speech

with gr.Blocks() as PartsOfSpeech:
    with gr.Row():
        with gr.Column():
            with gr.Row():
                text_input = gr.Textbox(
                    label = "Enter your Text",
                    value = "The five boxing wizards jump quickly."
                )
            
            with gr.Row():
                model = gr.Radio(
                    choices = CONFIG['allowed_models'],
                    value = CONFIG['allowed_models'][0],
                    label = "Choose language model"
                )
            
            with gr.Row():
                with gr.Column():
                    submit = gr.Button("Tag Parts of Speech")

                with gr.Column():
                    gr.ClearButton([text_input])

        with gr.Column():
            tokens_list = gr.DataFrame(label="Tokens Found")

    submit.click(
        parts_of_speech,
        inputs=[text_input, model],
        outputs=tokens_list
    )
