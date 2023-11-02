while(True):
    anagram1 = input()
    anagram2 = input()
    anagram1 = anagram1.replace(" ", "")
    anagram2 = anagram2.replace(" ", "")
    if(len(anagram1)<2 or len(anagram2)<2):
        print("try again, the word is less than 1 letter")
        continue
    anagram1.lower().sort()
    anagram2.lower().sort()
    if(anagram1==anagram2):
        print("this is an anagram")
    else:
        print("this is not ananagram")