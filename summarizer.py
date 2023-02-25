import re
import nltk
import heapq

# class Summarizer:
#     """
#     A class used to summarize texts.

#     This class can summarize texts from strings, list of string or a file.
#     It can use language specific stop word lists containg words to ignore during the 
#     determination of the most important subjects of the text. The language and stop word lists
#     can be set seperately or can be detected automatically from a text.

#     Attributes
#     ----------
#     stop_words : set
#         a set of stopwords. These are ignored when searching for the most used
#         words in the text
#     language : str
#         the current selected language. The stop words set is language specific
#     summary_length : int
#         the default number of sentences to use for the summary.
#     balance_length : bool
#         determines if the sentence weight is weighted based on sentence length

#     """
    
#     stop_words:set = {}
#     language:str = None
#     summary_length:int = 0
#     balance_length:bool = False
    
#     def __init__(self, language:str='dutch', summary_length:int=3, balance_length=False):
#         """
#         :param str language: The language to use, defaults to 'dutch'
#         :param int summary_length: The default length for the summary to generate, defaults to 3
#         :param bool balance_length: Balance sentences on lebgth, default to False
#         """
#         self.set_language(language)
#         self.set_summary_length(summary_length)
#         self.set_balance_length(balance_length)
    
#     def set_language(self, lang:str) -> None:
#         """
#         Sets the language to use and set the stop words to the default
#         list provided by NLTK corpus for this language
#         :param str lang: The language to use
#         """
#         try:
#             self.stop_words = set(stopwords.words(lang))
#             self.language = lang
#         except:
#             self.stop_words = {}
#             self.language = None
        
#     def set_stop_words(self, stop_words:set) -> None:
#         """
#         Sets the stop words to the provided list.
#         :param set stop_words: The stop words to use
#         """
#         if stop_words:
#             self.stop_words = set(stop_words)
#         else:
#             self.stop_words = {}
        
#     def read_stopwords_from_file(self, language:str, filename:str) -> None:
#         """
#         Read the stop words from the specified file and set the language to
#         the given language name
#         :param strlanguage: The name of the language to set
#         :param str filename: The name of the file containing the stop words
#         """
#         try:
#             with open(filename, "r", encoding="utf-8") as f:
#                  text = " ".join(f.readlines())
#             self.stop_words = set(text.split())  # prevent duplicate entries
#             self.language = language
#         except:
#             self.stop_words = {}
#             self.language = None
            
#     def set_summary_length(self, summary_length:int) -> None:
#         """
#         Sets the default length for the summaries to be created
#         :param int summary_length: The new default length
#         """
#         self.summary_length = summary_length

#     def set_balance_length(self, balance_length:bool) -> None:
#         """
#         Sets the swith if the sentence weights need to weighted on
#         sentence length. This might improve performance if the text
#         contains a variety of short and long sentences.
#         :param bool balance_length: new vale
#         """
#         self.balance_length = balance_length

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

    
    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    return summary
