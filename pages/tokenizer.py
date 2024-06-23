import gradio as gr
from spacy_functions import tokenizer

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

    submit.click(tokenizer, [text_input], tokens_list, queue=True)
