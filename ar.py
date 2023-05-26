import translations

while True:
    
    word = input("Enter the Arabic verb: (or 'exit' to quit): ")
    if word == 'exit':
        break
    
    C1 = ""
    C2 = ""
    C3 = ""
    letters, uni_codes = translations.translate_verb_into_letters(word)
    subject = translations.get_subject(letters)
    the_letters = translations.get_letters(uni_codes)
    size = len(the_letters)
    C = [C1, C2, C3]
    for i in range(size):
        C[i] = the_letters[i]
        
    if C1 is not None:
        C1 = ord(C[0])
        C1 = chr(C1)
        translations.vowels_map['C1'] = C1
    if C2 is not None:
        try:
            C2 = ord(C[1])
            C2 = chr(C2)
            translations.vowels_map['C2'] = C2
        except:
            C2 = ord(C[0])
            C2 = chr(C2)
            translations.vowels_map['C2'] = C2
    if C3 is not None:
        try:
            C3 = ord(C[2])
            C3 = chr(C3)
            translations.vowels_map['C3'] = C3
        except:
            try:
                C3 = ord(C[1])
                C3 = chr(C3)
                translations.vowels_map['C3'] = C3
            except:
                C3 = ord(C[0])
                C3 = chr(C3)
                translations.vowels_map['C3'] = C3

    #print(uni_codes)
    print("Translation of the verb: " + letters)
    print("\n")
    print("Subjects of the verb in Arabic: ")
    subjects_in_arabic = translations.translate_pattern_to_arabic(subject)
    subjects_in_english = translations.customize_subjects(subject)
    for i in range(len(subjects_in_arabic)):
        print(subjects_in_arabic[i])
        print(subjects_in_english[i])
        print("\n")


