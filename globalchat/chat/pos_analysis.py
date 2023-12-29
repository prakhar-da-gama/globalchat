# pos_analysis.py
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def get_full_part_of_speech(pos_tag):
    pos_mapping = {
        'CC': 'Coordinating conjunction',
        'CD': 'Cardinal number',
        'DT': 'Determiner',
        'EX': 'Existential there',
        'FW': 'Foreign word',
        'IN': 'Preposition or subordinating conjunction',
        'JJ': 'Adjective',
        'JJR': 'Adjective, comparative',
        'JJS': 'Adjective, superlative',
        'LS': 'List item marker',
        'MD': 'Modal',
        'NN': 'Noun, singular or mass',
        'NNS': 'Noun, plural',
        'NNP': 'Proper noun, singular',
        'NNPS': 'Proper noun, plural',
        'PDT': 'Predeterminer',
        'POS': 'Possessive ending',
        'PRP': 'Personal pronoun',
        'PRP$': 'Possessive pronoun',
        'RB': 'Adverb',
        'RBR': 'Adverb, comparative',
        'RBS': 'Adverb, superlative',
        'RP': 'Particle',
        'SYM': 'Symbol',
        'TO': 'to',
        'UH': 'Interjection',
        'VB': 'Verb, base form',
        'VBD': 'Verb, past tense',
        'VBG': 'Verb, gerund or present participle',
        'VBN': 'Verb, past participle',
        'VBP': 'Verb, non-3rd person singular present',
        'VBZ': 'Verb, 3rd person singular present',
        'WDT': 'Wh-determiner',
        'WP': 'Wh-pronoun',
        'WP$': 'Possessive wh-pronoun',
        'WRB': 'Wh-adverb',
    }

    return pos_mapping.get(pos_tag, pos_tag)

def get_parts_of_speech(sentence):
    words = word_tokenize(sentence)
    pos_tags = pos_tag(words)

    pos_dict = {}
    for word, pos in pos_tags:
        full_pos = get_full_part_of_speech(pos)
        if full_pos in pos_dict:
            pos_dict[full_pos].append(word)
        else:
            pos_dict[full_pos] = [word]

    return pos_dict

def analyze_sentence(sentence):
    parts_of_speech = get_parts_of_speech(sentence)

    print("\nParts of Speech and Corresponding Words:")
    for pos, words in parts_of_speech.items():
        print(f"{pos}: {', '.join(words)}")


