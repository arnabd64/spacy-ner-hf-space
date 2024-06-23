import gradio as gr
from spacy_functions import CONFIG, named_entity_recognition

with gr.Blocks() as NamedEntityRecognition:
    with gr.Row():
        with gr.Column():
            with gr.Row():
                text_input = gr.Textbox(
                    label = "Enter your Text",
                    value = "Apple Inc. is planning to open a new office in San Francisco in October 2024, and Tim Cook will be the keynote speaker at the opening ceremony.",
                    lines = 3
                )

            with gr.Row():
                model = gr.Radio(
                    choices = CONFIG['allowed_models'],
                    value = CONFIG['allowed_models'][0],
                    label = "Choose language model"
                )
                
            with gr.Row():
                filters = gr.CheckboxGroup(
                    label = "Choose Entities to Hide",
                    choices = CONFIG['entities']
                )

            with gr.Row():
                with gr.Column():
                    submit = gr.Button("Recognize Entities")

                with gr.Column():
                    gr.ClearButton([text_input, filters])

        with gr.Column():
            entity_list = gr.DataFrame(label="Entities Found")

    submit.click(
        named_entity_recognition,
        inputs=[text_input, model, filters],
        outputs=entity_list
    )
