---
title: Spacy Token Classifier
emoji: 📈
# emoji: https://img.stackshare.io/service/7312/7-7zis8f_400x400.png
colorFrom: blue
colorTo: indigo
python_version: 3.12
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: apache-2.0
header: mini
models:
    - spacy/en_core_web_sm
    - spacy/en_core_web_trf
tags:
    - token-classification
    - named-entity-recognition
    - parts-of-speech-tagging
---

# Spacy NER Pipeline

## Overview

This gradio based webapp is used to showcase the capabilities of the Spacy NER pipelineline. NER which an abbreviation for Named Entity Recognition is a task of assigning each token or a group of token in a text a predetermined entity tag. These tags can be `PERSON`, `LOCATION`, `EVENT`, `DATE` etc. [Spacy](https://spacy.io) is a production ready python library that offers many natural language processing pipelines and is also one of the most easy to use python libraries out there for NLP.

The UI for the webapp has been built using [Gradio](https://www.gradio.app/) which is another easy to use python library for building simple webapps. The User Interface gradio provides is simple and responsive. It provides the necessary HTML, CSS and Javascript needed to render the final UI.

The final application has been deployed on [Huggingface Spaces](https://huggingface.co/spaces). They provide a several deployment templates for several machine learning models and use cases. The free space provides a 16-core vCPU with 16GB of virtual RAM which is more than enough for this project's hardware needs.

## Packages used

```
spacy==3.7.6
spacy-transformers==1.3.5
gradio==4.44
```

Spacy provides a ton of language models, but we have restricted ouselves to `en_core_web_sm` and `en_core_web_trf` language models. `en_core_web_sm` model is optimized for CPU and low latency but sacrifices accuracy in complex scenarios whereas `en_core_web_trf` uses transformer based models thus is optimized for accuracy and sacrifices speed and low latency.

## Deploy Space in your Hardware

### Duplicate this Huggingface Space to your profile

Click on the vertical three dots located on the top right corner beside the Settings tab then click __Duplicate this Space__ option. Then choose the correct options and finally click on __Duplicate Space__ to deploy the Space onto your own Huggingface profile.

### Deploy using docker

Use the following `docker run` command to deploy the space as a docker container:

```bash
docker run -itd --name spacy-ner-space -p 7860:7860 registry.hf.space/pitangent-ds-spacy-ner:latest python app.py
```



Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
