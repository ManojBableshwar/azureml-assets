T5 Small is a text-to-text transformer model with 60 million parameters. It is developed by a group of researchers and is based on the Text-To-Text Transfer Transformer (T5) framework, which allows for a unified text-to-text format for input and output of all NLP tasks. T5-Small can be trained for multiple NLP tasks such as machine translation, document summarization, question answering, classification, and even regression tasks. It is pre-trained on the Colossal Clean Crawled Corpus (C4) and a multi-task mixture of unsupervised and supervised tasks in various languages, such as English, French, Romanian and German. You can use the code provided to get started with the model and refer to the resources provided for more information on the model.

> The above summary was generated using ChatGPT. Review the <a href="https://huggingface.co/t5-small" target="_blank">original-model-card</a> to understand the data used to train the model, evaluation metrics, license, intended uses, limitations and bias before using the model.

### Inference samples

Inference type|Python sample (Notebook)|CLI with YAML
|--|--|--|
Real time|<a href="https://aka.ms/azureml-infer-online-sdk-translation" target="_blank">translation-online-endpoint.ipynb</a>|<a href="https://aka.ms/azureml-infer-online-cli-translation" target="_blank">translation-online-endpoint.sh</a>
Batch | coming soon


### Finetuning samples

Task|Use case|Dataset|Python sample (Notebook)|CLI with YAML
|---|--|--|--|--|
Summarization|Summarization|<a href="https://huggingface.co/datasets/cnn_dailymail" target="_blank">CNN DailyMail</a>|<a href="https://aka.ms/azureml-ft-sdk-news-summary" target="_blank">news-summary.ipynb</a>|<a href="https://aka.ms/azureml-ft-cli-news-summary" target="_blank">news-summary.sh</a>
Translation|Translation|<a href="https://huggingface.co/datasets/cnn_dailymail" target="_blank">WMT16</a>|<a href="https://aka.ms/azureml-ft-sdk-translation" target="_blank">translation.ipynb</a>|<a href="https://aka.ms/azureml-ft-cli-translation" target="_blank">translation.sh</a>


### Model Evaluation

| Task        | Use case    | Dataset                                                            | Python sample (Notebook)                                                        | CLI with YAML                                                                 |
|-------------|-------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Translation | Translation | <a href="https://huggingface.co/datasets/wmt19/viewer/cs-en/" target="_blank">wmt19/cs-en</a> | <a href="https://aka.ms/azureml-eval-sdk-translation" target="_blank">evaluate-model-translation.ipynb</a> | <a href="https://aka.ms/azureml-eval-cli-translation" target="_blank">evaluate-model-translation.yml</a> |


### Sample inputs and outputs (for real-time inference)

#### Sample input
```json
{
    "inputs": {
        "input_string": ["My name is John and I live in Seattle", "Berlin is the capital of Germany."]
    }
}
```

#### Sample output
```json
[
    {
        "translation_text": "Mein Name ist John und ich lebe in Seattle."
    },
    {
        "translation_text": "Berlin ist die Hauptstadt Deutschlands."
    }
]
```
