from spacy_functions import CONFIG, tokenizer, named_entity_recognition, parts_of_speech
import gradio as gr

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

        gr.Markdown("__Entities Found__:")
        with gr.Column():
            entity_list = gr.DataFrame()

    submit.click(named_entity_recognition, [text_input, model, filters], entity_list)
