import gradio as gr
import gradio.components as grc
import spacy_functions

with gr.Blocks() as tokenizer:

    with gr.Row():

        with gr.Column(elem_id="input"):
            with gr.Row():
                text_input = grc.Textbox(
                    label = "Enter your Text",
                    value = "The five boxing wizards jump quickly."
                )
            
            with gr.Row(elem_id="buttons"):
                with gr.Column():
                    submit = grc.Button("Tokenize")

                with gr.Column():
                    grc.ClearButton([text_input])

        with gr.Column(elem_id="tokens-output"):
            tokens_list = grc.JSON(label="Tokens Found")

    submit.click(
        spacy_functions.tokenizer,
        inputs=[text_input],
        outputs=tokens_list
    )
