""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from text import cmudict

_pad        = '_'
_punctuation = '!\'(),.:;? '
_special = '-'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
_tamil_letters = ',ஂ,ஃ,அ,ஆ,இ,ஈ,உ,ஊ,எ,ஏ,ஐ,ஒ,ஓ,ஔ,க,ங,ச,ஜ,ஞ,ட,ண,த,ந,ன,ப,ம,ய,ர,ற,ல,ள,ழ,வ,ஶ,ஷ,ஸ,ஹ,ா,ி,C,ீ,ு,ூ,ெ,ே,ை,ொ,ோ,ௌ,்,ௐ,ௗ,௦,௧,௨,௩,௪,௫,௬,௭,௮,௯,௰,௱,௲,௳,௴,௵,௶,௷,௸,௹,௺'
# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet + _tamil_letters.split(',')



