import os
import re

from tutespiration.core.models import Quote

def is_valid(quote):
    """
    Sentences are valid quotes if they:
    * contain only alphanumeric characters, hyphens, and whitespace; and
    * do not start with a number (these are section headers); and
    * have between 6 and 12 words.
    """
    return all([re.match(r'^(?!\d+)[a-zA-Z0-9\-\s]+$', quote) is not None,
                len(quote.split(' ')) <= 12,
                len(quote.split(' ')) >= 6])

def get_url_from_file(filename):
    assert re.match(r'1721.1-[\d]+-new.txt', filename)
    m = re.search(r'1721.1-([\d]+)-new.txt', filename)
    file_id = m.group(1)
    return 'https://dspace.mit.edu/handle/1721.1/{id}'.format(id=file_id)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_RELATIVE_DIR = 'files'
DOCS_ABSOLUTE_DIR = os.path.join(BASE_DIR, DOCS_RELATIVE_DIR)
DOC_LIST = [f for f in os.listdir(DOCS_ABSOLUTE_DIR)
                    if os.path.splitext(f)[-1] == '.txt']

for doc in DOC_LIST:
    full_path = os.path.join(DOCS_ABSOLUTE_DIR, doc)
    url = get_url_from_file(doc)
    with open(full_path, 'r') as doc_contents:
        for sentence in doc_contents.read().split('.'):
            # Deal with hyphenated line breaks, which we do not want.
            sentence = re.sub(r'(\w)\-\s(\w)', r'\1\2', sentence)
            # Get rid of any remaining newlines.
            sentence = sentence.replace('\n', ' ').strip()
            if is_valid(sentence):
                Quote.objects.create(text=sentence, url=url)

