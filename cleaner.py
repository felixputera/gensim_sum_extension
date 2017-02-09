import logging
import re
from pycorenlp import StanfordCoreNLP
from gensim.parsing.preprocessing import preprocess_documents
from gensim.summarization.textcleaner import merge_syntactic_units, join_words

logger = logging.getLogger('summa.preprocessing.cleaner')

try:
    from pattern.en import tag
    logger.info("'pattern' package found; tag filters are available for English")
    HAS_PATTERN = True
except ImportError:
    logger.info("'pattern' package not found; tag filters are not available for English")
    HAS_PATTERN = False


def split_sentences(text):
    print('split sentences')
    sen_list = []
    nlp = StanfordCoreNLP('http://localhost:9000')
    output = nlp.annotate(text, properties={
        'annotators': 'ssplit',
        'outputFormat': 'text'
    })
    for s in re.finditer(r"Sentence\s[A-Za-z1-9\s()#]+:", output):
        text_splice = output[s.end()+1:]
        sentence_end = re.search(r"\[Text=", text_splice)
        if sentence_end:
            sen_list.append(text_splice[:sentence_end.start()-2].replace('\n', ' '))

    return(sen_list)


def clean_text_by_sentences(text):
    print('clean text by sentences')
    """ Tokenizes a given text into sentences, applying filters and lemmatizing them.
    Returns a SyntacticUnit list. """
    original_sentences = split_sentences(text)
    filtered_sentences = [join_words(sentence) for sentence in preprocess_documents(original_sentences)]

    return merge_syntactic_units(original_sentences, filtered_sentences)
