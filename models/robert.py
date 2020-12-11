from transformers import pipeline

robert = pipeline(
    "question-answering",
    model="csarron/roberta-base-squad-v1",
    tokenizer="csarron/roberta-base-squad-v1"
)
