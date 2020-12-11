from transformers import pipeline
squeezebert = pipeline('question-answering', model='mrm8488/squeezebert-finetuned-squadv1')
