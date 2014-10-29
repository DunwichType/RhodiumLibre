# !/usr/bin/python

# Mixer v.0.02
# Mixer originated by James Puckett, jp@dunwichtype.com
# Mixer can be downloaded at www.DunwichType.com
# Mixer is a program for 

# Codecs module is needed to generate working text files on Mac OS X
import codecs

# Declare my lists
# Spam and eggs are just short lists for testing
spam = [ '1', '2', '3']
eggs = [ 'a', 'b', 'c']

majbasic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

minbasic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

allbasic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lc_control = ['anon ', 'bnon ', 'cnon ', 'dnon ', 'enon ', 'fnon ', 'gnon ', 'hnon ', 'inon ', 'jnon ', 'knon ', 'lnon ', 'mnon ', 'nnon ', 'onon ', 'pnon ', 'qnon ', 'rnon ', 'snon ', 'tnon ', 'unon ', 'vnon ', 'wnon ', 'xnon ', 'ynon ', 'znon ']

controls = ['H', 'O', 'h', 'n', 'o']
majcontrols = ['H', 'O']
mincontrols = ['h', 'o', 'n']
figcontrols = ['0', '1']

majuscules = ['A', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ā', 'Ă', 'Ą', 'Æ', 'Ǽ', 'Z', 'B', 'C', 'Ç', 'Ć', 'Ĉ', 'Ċ', 'Č', 'D', 'Ď', 'Đ', 'E', 'È', 'É', 'Ê', 'Ë', 'Ē', 'Ĕ', 'Ė', 'Ę', 'Ě', 'F', 'G', 'Ĝ', 'Ğ', 'Ġ', 'Ģ', 'H', 'Ĥ', 'Ħ', 'I', 'Ì', 'Í', 'Î', 'Ï', 'Ĩ', 'Ī', 'Ĭ', 'Į', 'J', 'Ĵ', 'K', 'Ķ', 'L', 'Ĺ', 'Ļ', 'Ľ', 'Ł', 'Ŀ', 'M', 'N', 'Ń', 'Ņ', 'Ň', 'Ŋ', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', 'Ō', 'Ŏ', 'Ő', 'Ø', 'Ǿ', 'Œ', 'P', 'Q', 'Þ', 'R', 'Ŕ', 'Ř', 'Ŗ', 'S', 'Ś', 'Ŝ', 'Ş', 'Š', 'Ș', 'T', 'Ţ', 'Ť', 'Ŧ', 'Ț', 'U', 'Ù', 'Ú', 'Û', 'Ü', 'Ũ', 'Ū', 'Ŭ', 'Ů', 'Ű', 'Ų', 'V', 'W', 'Ŵ', 'Ẁ', 'Ẃ', 'Ẅ', 'X', 'Y', 'Ý', 'Ŷ', 'Ÿ', 'Z', 'Ź', 'Ż', 'Ž']

minuscules = ['a', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ā', 'ă', 'ą', 'æ', 'ǽ', 'b', 'v', 'ç', 'ć', 'ĉ', 'ċ', 'č', 'd', 'ď', 'đ', 'e', 'è', 'é', 'ê', 'ë', 'ē', 'ĕ', 'ė', 'ę', 'ě', 'f', 'g', 'ĝ', 'ğ', 'ġ', 'ģ', 'h', 'ĥ', 'ħ', 'i', 'ì', 'í', 'î', 'ï', 'ĩ', 'ī', 'ĭ', 'į', 'j', 'ĵ', 'k', 'ķ', 'l', 'ĺ', 'ļ', 'ľ', 'ł', 'ŀ', 'm', 'n', 'ń', 'ņ', 'ň', 'ŋ', 'ñ', 'o', 'ò', 'ó', 'ô', 'õ', 'ö', 'ō', 'ŏ', 'ő', 'ø', 'ǿ', 'œ', 'p', 'þ', 'q', 'r', 'ŕ', 'ř', 'ŗ', 's', 'ś', 'ŝ', 'ş', 'š', 'ș', 'ß', 't', 'ţ', 'ť', 'ŧ', 'ț', 'u', 'ù', 'ú', 'û', 'ü', 'ũ', 'ū', 'ŭ', 'ů', 'ű', 'ų', 'v', 'w', 'ŵ', 'ẁ', 'ẃ', 'ẅ', 'x', 'y', 'ý', 'ŷ', 'ÿ', 'z', 'ź', 'ż', 'ž']

punct = ['.', '…', ',', ':', ';', '?', '¿', '!', '¡', '\'', '\"', '‘', '’', '‚', '“', '”', '„', '‹', '›', '«', '»', '-', '–', '—', '_', '†', '‡', '•', '*', '©', '®', '™', '@', '¶', '(', ')', '[', ']', '{', '}', '/', '\\', '|',]

currency = ['#', '%', '&', '¢', '$', '£', '¥', 'ƒ', '€']

figures = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

prebuilt = ['½', '¼', '¾', '⅓', '⅔', '⅛', '⅜', '⅝']

math = ['<', '+', '−', '=', '÷', '×', '>', '±', '^', '~', '|', '¦', '§', '°', 'ª', 'º', '%']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '½', '¼', '¾', '⅓', '⅔', '⅛', '⅜', '⅝', '#', '%', '&', '¢', '$', '£', '¥', 'ƒ', '€', '<', '+', '−', '=', '÷', '×', '>', '±', '^', '~', '|', '¦', '§', '°', 'ª', 'º', '%'] 

adhesion = ['a', 'd', 'h', 'e', 's', 'i', 'o', 'n']

ADHESION = ['A', 'D', 'H', 'E', 'S', 'I', 'O', 'N']

handgloves = ['h', 'a', 'n', 'd', 'g', 'l', 'o', 'v', 'e', 's']

HANDGLOVES = ['H', 'A', 'N', 'D', 'G', 'L', 'O', 'V', 'E', 'S']

hamburgefontivs = ['h', 'a', 'm', 'b', 'u', 'r', 'g', 'e', 'f', 'o', 'n', 't', 'i', 'v', 's']

HAMBURGEFONTIVS = ['H', 'A', 'M', 'B', 'U', 'R', 'G', 'E', 'F', 'O', 'N', 'T', 'I', 'V', 'S']

basicpunct = ['.', ',', '\"', '!', '?']

arabic = ['ain-ar', 'alef-ar', 'alefhamzabelow-ar', 'beh-ar', 'dad-ar', 'dal-ar', 'feh-ar', 'ghain-ar', 'hah-ar', 'hamza-ar', 'heh-ar', 'jeem-ar', 'kaf-ar', 'khah-ar', 'lam-ar', 'meem-ar', 'noon-ar', 'qaf-ar', 'reh-ar', 'sad-ar', 'seen-ar', 'sheen-ar', 'tah-ar', 'tehmarbuta-ar', 'thal-ar', 'theh-ar', 'waw-ar', 'yeh-ar', 'zah-ar', 'zain-ar']

positions = ['.fina\r', '.medi\r', '.init\r', '',]

majLatinXB = ['Ɓ', 'Ƃ', 'Ƅ', 'Ɔ', 'Ƈ', 'Ɖ', 'Ɗ', 'Ƌ', 'Ǝ', 'Ə', 'Ɛ', 'Ƒ', 'Ɠ', 'Ɣ', 'Ɩ', 'Ɨ', 'Ƙ', 'Ɯ', 'Ɲ', 'Ɵ', 'Ơ', 'Ƣ', 'Ƥ', 'Ʀ', 'Ƨ', 'Ʃ', 'ƪ', 'Ƭ', 'Ʈ', 'Ư', 'Ʊ', 'Ʋ', 'Ƴ', 'Ƶ', 'Ʒ', 'Ƹ', 'ƻ', 'Ƽ', 'ǀ', 'ǁ', 'ǂ', 'ǃ', 'Ǆ', 'ǅ', 'Ǉ', 'ǈ', 'Ǌ', 'ǋ', 'Ǎ', 'Ǐ', 'Ǒ', 'Ǔ', 'Ǖ', 'Ǘ', 'Ǚ', 'Ǜ', 'Ǟ', 'Ǡ', 'Ǣ', 'Ǥ', 'Ǧ', 'Ǩ', 'Ǫ', 'Ǭ', 'Ǯ', 'Ǳ', 'ǲ', 'Ǵ', 'Ƕ', 'Ƿ', 'Ǹ', 'Ǻ', 'Ǽ', 'Ȁ', 'Ȃ', 'Ȅ', 'Ȇ', 'Ȉ', 'Ȋ', 'Ȍ', 'Ȏ', 'Ȑ', 'Ȓ', 'Ȕ', 'Ȗ', 'Ș', 'Ț', 'Ȝ', 'Ȟ', 'Ƞ', 'Ȣ', 'Ȥ', 'Ȧ', 'Ȩ', 'Ȫ', 'Ȭ', 'Ȯ', 'Ȱ', 'Ȳ', 'Ⱥ', 'Ȼ', 'Ƚ', 'Ⱦ', 'Ɂ', 'Ƀ', 'Ʉ', 'Ʌ', 'Ɇ', 'Ɉ', 'Ɋ', 'Ɍ', 'Ɏ']

minusLatinXB = ['ƀ', 'ƃ', 'ƅ', 'ƈ', 'ƌ', 'ƍ', 'ƕ', 'ƙ', 'ƚ', 'ƛ', 'ơ', 'ƣ', 'ƥ', 'ƨ', 'ƫ', 'ƭ', 'ư', 'ƴ', 'ƶ', 'ƹ', 'ƺ', 'ƽ', 'ƾ', 'ƿ', 'ǆ', 'ǉ', 'ǌ', 'ǎ', 'ǐ', 'ǒ', 'ǔ', 'ǖ', 'ǘ', 'ǚ', 'ǜ', 'ǝ', 'ǟ', 'ǡ', 'ǣ', 'ǥ', 'ǧ', 'ǩ', 'ǫ', 'ǭ', 'ǯ', 'ǳ', 'ǵ', 'ǹ', 'ǻ', 'ǽ', 'ȁ', 'ȃ', 'ȅ', 'ȇ', 'ȉ', 'ȋ', 'ȍ', 'ȏ', 'ȑ', 'ȓ', 'ȕ', 'ȗ', 'ș', 'ț', 'ȝ', 'ȟ', 'ȡ', 'ȣ', 'ȥ', 'ȧ', 'ȩ', 'ȫ', 'ȭ', 'ȯ', 'ȱ', 'ȳ', 'ȴ', 'ȵ', 'ȶ', 'ȷ', 'ȸ', 'ȹ', 'ȼ', 'ȿ', 'ɀ', 'ɂ', 'ɇ', 'ɉ', 'ɋ', 'ɍ', 'ɏ']

devaHalfCons = [u'क्', u'ख्', u'ग्', u'घ्', u'च्', u'छ्', u'ज्', u'झ्', u'ञ्', u'ण्', u'त्', u'थ्', u'ध्', u'न्', u'प्', u'फ्', u'ब्', u'भ्', u'म्', u'य्', u'ल्', u'ळ्', u'व्', u'श्', u'ष्', u'स्', u'ह्']

devaCons = [u'क ', u'ख ', u'ग ', u'घ ', u'च ', u'छ ', u'ज ', u'झ ', u'ञ ', u'ट ', u'ठ ', u'ड ', u'ढ ', u'ण ', u'त ', u'थ ', u'द ', u'ध ', u'न ', u'प ', u'फ ', u'ब ', u'भ ', u'म ', u'य ', u'ल ', u'ळ ', u'व ', u'श ']

# mixer is the function that iterates through the lists, combining them

def mixer (dough, chips, title):
	
	# Prepare output file for writing
	output = open( title+'.txt', 'w')
	output.write( codecs.BOM_UTF8 )
	
	output.write ( title.encode( "utf-8" ))
	output.write( '\n')
	for i in dough:
		mix = ''
		for z in chips:
			mix += i 
			mix += z
		output.write( mix.encode( "utf-8" ))
		output.write( '\n')
	output.close()
    
# make the mixes!
#mixer(spam, eggs, 'Test')
#mixer(majbasic, majbasic, 'Basic_Caps')
#mixer(majbasic, minbasic, 'Basic_Mixed')
#mixer(minbasic, minbasic, 'Basic_Lowercase')
#mixer(majuscules, majuscules, 'All_Caps')
#mixer(majuscules, minuscules, 'All_Mixed')
#mixer(minuscules, minuscules, 'All_Lowercase') 
#mixer(majuscules, punct, 'All_UC_Punct')
#mixer(minuscules, punct, 'All_LC_Punct')
#mixer(figures, figures, 'Numbers')
#mixer(figures, math, 'Numbers_Math')
#mixer(figures, currency, 'Numbers_Currency')
#mixer(figures, prebuilt, 'Numbers_Prebuilts')
#mixer(prebuilt, math, 'Math_Prebuilts')
#mixer(numbers, numbers, 'All_Numbers')
#mixer(allbasic, figures, 'Numbers_Alpha')
#mixer (majbasic, lc_control, 'CapsLCtest')
#mixer (adhesion, adhesion, 'adhesion_lc')
#mixer (adhesion, ADHESION, 'adhesion_mix')
#mixer (ADHESION, adhesion, 'adhesion_caps')
#mixer (adhesion, basicpunct, 'lc_punct')
#mixer (ADHESION, basicpunct, 'uc_punct')
#mixer (arabic, positions, 'arabic_complete')
#mixer (figures, allbasic, 'figures_alpha')
mixer (devaHalfCons, devaCons, 'deva_halfs')


# close the output file.