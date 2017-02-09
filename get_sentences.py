from gensim.summarization.summarizer import _format_results
from .cleaner import clean_text_by_sentences as _clean_text_by_sentences

def get_extracted_number(sum_sentences, original_text):
    sum_number = []
    sum_sentences = _format_results(_clean_text_by_sentences(sum_sentences), True)
    sentences = _format_results(_clean_text_by_sentences(original_text), True)
    for ss in sum_sentences:
        sum_number.append(sentences.index(ss))
    return sum_number

def sentence_from_number(sum_number, text):
    sum_sentences = []
    sentences = _format_results(_clean_text_by_sentences(text), True)
    for i in sum_number:
        sum_sentences.append(sentences[i])
    return '\n'.join(sum_sentences)


