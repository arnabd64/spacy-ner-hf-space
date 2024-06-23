import gradio as gr
import spacy_functions

with gr.Blocks() as ner:
    with gr.Row():
        with gr.Column(elem_id="input"):
            with gr.Row(elem_id="text"):
                text_input = gr.Textbox(
                    label = "Enter your Text",
                    value = "Apple Inc. is planning to open a new office in San Francisco in October 2024, and Tim Cook will be the keynote speaker at the opening ceremony.",
                    lines = 3
                )

            with gr.Row(elem_id="model"):
                model = gr.Radio(
                    choices = spacy_functions.ALLOWED_MODELS,
                    value = spacy_functions.ALLOWED_MODELS[0],
                    label = "Choose language model"
                )
                
            with gr.Row(elem_id="entity-filter"):
                filters = gr.CheckboxGroup(
                    label = "Choose Entities to Hide",
                    choices = spacy_functions.ENTITIES
                )

            with gr.Row(elem_id="buttons"):
                with gr.Column():
                    submit = gr.Button("Recognize Entities")

                with gr.Column():
                    gr.ClearButton([text_input, filters])

        with gr.Column(elem_id="output"):
            entity_list = gr.DataFrame(label="Entities Found")

    submit.click(
        spacy_functions.named_entity_recognition,
        inputs=[text_input, model, filters],
        outputs=entity_list
    )
