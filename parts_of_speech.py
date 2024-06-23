import gradio as gr
import gradio.components as grc
import spacy_functions


with gr.Blocks() as parts_of_speech:

    with gr.Row():

        with gr.Column(elem_id="input"):
            with gr.Row(elem_id="text"):
                text_input = grc.Textbox(
                    label = "Enter your Text",
                    value = "The five boxing wizards jump quickly."
                )
            
            with gr.Row(elem_id="model"):
                model = grc.Radio(
                    choices = spacy_functions.ALLOWED_MODELS,
                    value = spacy_functions.ALLOWED_MODELS[0],
                    label = "Choose language model"
                )
            
            with gr.Row(elem_id="buttons"):
                with gr.Column():
                    submit = grc.Button("Tag Parts of Speech")

                with gr.Column():
                    grc.ClearButton([text_input])

        with gr.Column(elem_id="tokens-output"):
            tokens_list = grc.DataFrame(label="Tokens Found")

    submit.click(
        spacy_functions.parts_of_speech,
        inputs=[text_input, model],
        outputs=tokens_list
    )
