import unicodedata
vowels_map = {
        'a': '\u064E',
        'u': '\u064F',
        'i': '\u0650',
        's': '\u0652',
        'd': '\u0651',
        'y': '\u0649',
        'Aa': '\u0622',
        'A': '\u0627',
        'O': '\u0648',
        'E': '\u064A',
        'e': '\u0621',
        'e1': '\u0623',
        'e2': '\u0626',
        'e3': '\u0654',
        'M': '\u0645',
        'T': '\u0629',
        'C1' : '',
        'C2' : '',
        'C3' : '',
    }
def translate_verb_into_letters(word):
    uni_codes = []
    translated_word = []
    c = 1
    for char in word:
        
        category = unicodedata.category(char)
        
        if category.startswith('M'):
            if char == '\u064E':
                translated_word[-1] += 'a'
                
            elif char == '\u064F':
                translated_word[-1] += 'u'
                
            elif char == '\u0650':
                translated_word[-1] += 'i'
                
            elif char == '\u0652':
                translated_word[-1] += 's'
                
            elif char == '\u0651':
                translated_word[-1] += 'd'
                
            elif char == '\u0649':
                translated_word[-1] += 'y'
                
        elif category.startswith('L'):
            
            if char == '\u0622':
                translated_word.append('Aa')
                
            elif char == '\u0627':
                translated_word.append('A')
                
            elif char == '\u0648':
                translated_word.append('O')
                
            elif char == '\u064A':
                translated_word.append('E')
                
            elif char == '\u0621':
                translated_word.append('e')
                
            elif char == '\u0623':
                translated_word.append('e1')
                
            elif char == '\u0626':
                translated_word.append('e3')
                
            elif char == '\u0654':
                translated_word.append('e2')
                
            elif char == '\u0629':
                translated_word.append('T')
                
            elif char == '\u0649':
                translated_word.append('y')
            else:
                the_char = f'U+{ord(char):04X}'
                uni_codes.append(the_char)
                translated_word.append(f'C{c}')
                
            c += 1
            
    return ' '.join(translated_word), uni_codes

def unicode_list_to_word(unicode_list):
    word = ""
    for unicode_code in unicode_list:
        unicode_code = unicode_code.replace("U+", "").strip()
        unicode_int = int(unicode_code, 16)
        character = chr(unicode_int)
        word += character
    return word

def get_subject(translated_word):
    
    subject = []

    if translated_word == "C1a C2a C3a":
        subject.append("Mi C1s C2a A C3")
        
    if translated_word == "C1a C2ad":
        subject.append("Mi C1s C2a A C3")
        
    if translated_word == "e1a C2a C3a":
        subject.append("Mi e2s C1a A C2") #####
        
    if translated_word == "Oa C2a C3a":
        subject.append("Mi Es C1a A C2")
        
    if translated_word == "C1a A C3a":
        subject.append("Mi C1s Ea A C2")
        
    if translated_word == "C1a A C3a":
        subject.append("C1a Oad A C2a T")
        
    if translated_word == "C1a A C3a":
        subject.append("Mi C1s Oa A C2")
        
    if translated_word == "C1a C2a C3a":
        subject.append("Mi C1s C2a C3")
        
    if translated_word == "C1a C2a y":
        subject.append("Mi C1s C2a y")
        
    if translated_word == "C1a C2ad":
        subject.append("Mi C1a C2ad")
        
    if translated_word == "C1a A C3a":
        subject.append("Mi C1s Oa C2")
        
    if translated_word == "C1a C2a C3a":
        subject.append("Mi C1s C2a C3a T")
        
    if translated_word == "C1a C2ad":
        subject.append("Mi C1a C2ad T")
        
    if translated_word == "C1a C2a y":
        subject.append("Mi C1s Aa T")
        
    if translated_word == "C1a C2a y":
        subject.append("Mi C1s C2a A T")
        
    if translated_word == "C1a Oa y":
        subject.append("Mi C1s Oa A T")
        
    if translated_word == "C1a A C3a":
        subject.append("Mi C1s Ea C2a T")
        
    if translated_word == "C1a A C3a":
        subject.append("Mi C1s Oa C2a T")
        
    if translated_word == "C1a C2a C3a":
        subject.append("C1i C2a A C3a")
        
    if translated_word == "Oa C2a y":
        subject.append("Oi C1a A e")
        
    if translated_word == "C1a C2a C3a":
        subject.append("C1a A C2i C3a T")
        
    if translated_word == "C1a A C3a":
        subject.append("C1a A e2i C2a T")
        
    if translated_word == "C1a C2a y":
        subject.append("C1a A C2i Ea T")
        
    if translated_word == "C1a C2a C3a":
        subject.append("C1a C2ad A C3a T")
        
    if translated_word == "Oa C2a C3a":
        subject.append("Oa C1ad A C2a T")
        
    if translated_word == "C1a C2ad":
        subject.append("C1a C2ad A C3a T")
        
    if translated_word == "C1a C2i e3a":
        subject.append("C1a C2ad A Ea T")
        
    if translated_word == "C1a C2i e3a":
        subject.append("Mi C1s C2a e1a T")
        
    if translated_word == "C1a A C3a":
        subject.append("C1a Ead A C2a T")
        
    if translated_word == "C1a C2a y":
        subject.append("C1a C2ad A Ea T")
        
    if translated_word == "C1a Oa y":
        subject.append("C1a Oad A Ea T")
        
    if translated_word == "C1a C2a C3a":
        subject.append("C1a C2ad A C3")
        
    if translated_word == "C1a C2ad":
        subject.append("C1a C2ad A C3")
        
    if translated_word == "C1a A C3a":
        subject.append("C1a Oad A C2")
        
    if translated_word == "C1a C2a C3a":
        subject.append("C1a A C2u O C3")
        
    if translated_word == "C1a e1a y":
        subject.append("Mi C1s Aa T")
        
    return subject

def get_letters(code_list):
    letters = []
    for code in code_list:
        code_point = code[2:]
        letter = chr(int(code_point, 16))
        letters.append(letter)
    return letters


def translate_pattern_to_arabic(pattern):
    if isinstance(pattern, list):
        arabic_words = []
        for pat in pattern:
            arabic_word = ""
            pattern_parts = pat.split()
            
            for part in pattern_parts:
                if part.startswith('C') and part.endswith(('1', '2', '3')):
                    arabic_letter = vowels_map.get(part)
                    arabic_word += arabic_letter
                    
                elif part.startswith('C'):
                    letter_code = part[:2]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    letter_code = part[2]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    
                elif part.startswith('M'):
                    letter_code = part[0]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    if len(part) >= 2:
                        letter_code = part[1]
                        arabic_letter = vowels_map.get(letter_code)
                        arabic_word += arabic_letter
                    
                elif part.startswith('T'):
                    letter_code = part[0]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    if len(part) >= 2:
                        letter_code = part[1]
                        arabic_letter = vowels_map.get(letter_code)
                        arabic_word += arabic_letter
                    
                elif part.startswith('e1'):
                    letter_code = part[:2]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    if len(part) >= 2:
                        letter_code = part[2]
                        arabic_letter = vowels_map.get(letter_code)
                        arabic_word += arabic_letter
                    
                elif part.startswith('e2'):
                    letter_code = part[:2]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    if len(part) >= 2:
                        letter_code = part[2]
                        arabic_letter = vowels_map.get(letter_code)
                        arabic_word += arabic_letter
                    
                elif part.startswith('e'):
                    letter_code = part[0]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    if len(part) >= 2:
                        letter_code = part[1]
                        arabic_letter = vowels_map.get(letter_code)
                        arabic_word += arabic_letter
                        
                elif part.startswith('O'):
                    letter_code = part[0]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    if len(part) >= 2:
                        letter_code = part[1]
                        arabic_letter = vowels_map.get(letter_code)
                        arabic_word += arabic_letter
                        
                elif part.startswith('A'):
                    letter_code = part[0]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    if len(part) >= 2:
                        letter_code = part[1]
                        arabic_letter = vowels_map.get(letter_code)
                        arabic_word += arabic_letter
                    
                elif part.startswith('e3'):
                    letter_code = part[:2]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    if len(part) >= 2:
                        letter_code = part[2]
                        arabic_letter = vowels_map.get(letter_code)
                        arabic_word += arabic_letter
                        
                elif part.startswith('E'):
                    letter_code = part[0]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    if len(part) >= 2:
                        letter_code = part[1]
                        arabic_letter = vowels_map.get(letter_code)
                        arabic_word += arabic_letter
                    
                elif part.startswith('y'):
                    letter_code = part[0]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    if len(part) >= 2:
                        letter_code = part[1]
                        arabic_letter = vowels_map.get(letter_code)
                        arabic_word += arabic_letter
                    
                else:
                    arabic_word += vowels_map.get(part)
            arabic_words.append(arabic_word)
        return arabic_words
    
    else:
        arabic_word = ""
        pattern_parts = pattern.split()
        
        for part in pattern_parts:
            if part.startswith('C') and part.endswith(('1', '2', '3')):

                arabic_letter = vowels_map.get(part)
                arabic_word += arabic_letter
                
            elif part.startswith('C'):
                letter_code = part[:2]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                letter_code = part[2]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                
            elif part.startswith('M'):
                letter_code = part[0]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                if len(part) >= 2:
                    letter_code = part[1]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                
            elif part.startswith('T'):
                letter_code = part[0]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                if len(part) >= 2:
                    letter_code = part[1]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                
            elif part.startswith('e1'):
                letter_code = part[:2]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                if len(part) >= 2:
                    letter_code = part[2]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                
            elif part.startswith('e2'):
                letter_code = part[:2]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                if len(part) >= 2:
                    letter_code = part[2]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                
            elif part.startswith('e'):
                letter_code = part[0]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                if len(part) >= 2:
                    letter_code = part[1]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    
            elif part.startswith('O'):
                letter_code = part[0]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                if len(part) >= 2:
                    letter_code = part[1]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    
            elif part.startswith('A'):
                letter_code = part[0]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                if len(part) >= 2:
                    letter_code = part[1]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                
            elif part.startswith('e3'):
                letter_code = part[:2]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                if len(part) >= 2:
                    letter_code = part[2]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                    
            elif part.startswith('E'):
                letter_code = part[0]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                if len(part) >= 2:
                    letter_code = part[1]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                
            elif part.startswith('y'):
                letter_code = part[0]
                arabic_letter = vowels_map.get(letter_code)
                arabic_word += arabic_letter
                if len(part) >= 2:
                    letter_code = part[1]
                    arabic_letter = vowels_map.get(letter_code)
                    arabic_word += arabic_letter
                
            else:
                arabic_word += vowels_map.get(part)

        return arabic_word
    
def customize_subjects(subject):
    for s in range(len(subject)):
        if subject[s] == 'Mi e2s C1a A C2':
            subject[s] = 'Mi e2s C2a A C3'
            
        if subject[s] == 'Mi Es C1a A C2':
            subject[s] = 'Mi Es C2a A C3'
            
        if subject[s] == 'Mi C1s Ea A C2':
            subject[s] = 'Mi C2s Ea A C3'
            
        if subject[s] == 'Mi C1s Oa A C2':
            subject[s] = 'Mi C2s Oa A C3'
            
        if subject[s] == 'Mi C1s Oa C2':
            subject[s] = 'Mi C1s Oa C3'
            
        if subject[s] == 'Mi C1s Ea C2a T':
            subject[s] = 'Mi C1s Ea C3a T'
            
        if subject[s] == 'Mi C1s Oa C2a T':
            subject[s] = 'Mi C1s Oa C3a T'
            
        if subject[s] == 'Oi C1a A e':
            subject[s] = 'Oi C2a A e'
            
        if subject[s] == 'C1a A e2i C2a T':
            subject[s] = 'C1a A e2i C3a T'
            
        if subject[s] == 'Oa C1ad A C2a T':
            subject[s] = 'Oa C2ad A C3a T'
            
        if subject[s] == 'C1a Ead A C2a T':
            subject[s] = 'C1a Ead A C3a T'
            
        if subject[s] == 'C1a Oad A C2a T':
            subject[s] = 'C1a Oad A C3a T'
            
        if subject[s] == 'C1a Oad A C2a T':
            subject[s] = 'C1a Oad A C3a T'
            
        if subject[s] == 'C1a Oad A C2':
            subject[s] = 'C1a Oad A C3'
    return subject