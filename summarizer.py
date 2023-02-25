import re
import nltk
import heapq
import openai
from nltk.tokenize import sent_tokenize

MAX_LENGTH = 5000
def split_into_chunks(rt):
    arr = []
    string = ""
    for s in sent_tokenize(rt):
        string += s
        if len(string) > MAX_LENGTH:
            arr.append(string)
            string = ""

    return arr

# OpenAI text summarizer
openai.api_key = "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"

def summarize(text: str) -> str:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text + "\n\nTl;dr",
        temperature=0.7,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=1
        )
    
    return response["choices"][0]["text"]


# Online text summarizer 
def text_summarizer(text: str) -> str:
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', text )
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

    sentence_list = nltk.sent_tokenize(text)

    stopwords = nltk.corpus.stopwords.words('english')

    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_article_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    
    summary_sentences = heapq.nlargest(10, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    return summarize(summary)
