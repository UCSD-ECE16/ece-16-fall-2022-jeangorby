import enchant 
import string
d = enchant.Dict("en_US")

test_list = ['Quotient','Mustn\'t','Yellow', 'Honest', 'Thursday', 'Christmas', 
             'Alliteration', 'Information', 'Education', 'Fish', 'Numbers!', 'Toyota!',
             'Mother-in-law', 'Laps', 'Slap', 'August', 'empty-handed', 'Ice-cream',
             'Years', 'Yawn', 'Yard', 'Quiet', 'Quack', 'Yttrium', 'Up-to-date','Bye']

vowels = "aeiou"

def english_to_pig_latin(word):
    result = ""
    index = 0
    for x in word:
        # Handles the case of hyphens existing using recursion
        if '-' in word:
            result = word
            words = word.split('-')
            for x in words:
                result = result.replace(x, english_to_pig_latin(x))
            # print("finished here 1")
            break
        # Handles the case where Y is at the beginning of the word nd it is considered a consonant
        elif x.lower() not in vowels and x.lower() == 'y' and index == 0:
            # print(x)
            result = word[1:] + word[0] + "ey"
            # print("finished here 2")
            break
        # Handles the case where Y is considered a vowel
        elif x.lower() not in vowels and x.lower() == 'y' and index != 0:
            result = word[index:] + word[:index] + "ay"
            break
        # Handles the case where it starts with qu
        elif x.lower() == 'u' and word[index - 1].lower() == 'q':
            result = word[index+1:] + word[:index+1] + "ay"
            # print("finished here 3")
            break
        # Handles the general case
        elif x.lower() in vowels and index != 0:
            # print(x)
            result = word[index:] + word[:index] + "ay"
            # print("finished here 4")
            break
        # Handles the case where the word starts with a vowel
        elif x.lower() in vowels and index == 0:
            # print(x)
            result = word + "yay"
            # print("finished here 5")
            break
        elif x.lower() not in vowels:
            # print(x)
            pass

        index += 1

    return result

def pig_latin_to_english(word): 
    result = ""
    size = len(word)
    # Handles the case of starting with the letter y
    if(word[size-3:].lower() == "yey"):
        result = word[size-3] + word[:size-3]
    # Handles the case of starting with Qu
    elif(word[size-4:].lower() == "quay"):
        result = word[size-4:size-2] + word[:size-4]
    # Handles the case of starting with a vowel
    elif(word[size-3:].lower() == "yay"):
        result = word[:size-3]
    elif(word[size-2:].lower() == "ay"):
        for x in range(size):
            # print(word[x-3:size-2] + word[:x-3])
            print(d.check(word[x-3:size-2] + word[:x-3]))
            if any(char in word for char in string.punctuation):
                
            elif(d.check(word[x-3:size-2] + word[:x-3])):
                result = word[x-3:size-2] + word[:x-3]
                break
    return result

# print(english_to_pig_latin("aloha"))
# print(english_to_pig_latin("yellow"))
# print(english_to_pig_latin("Switch"))

for i, word in enumerate(test_list):
    out1 = english_to_pig_latin(word)  
    out2 = pig_latin_to_english(out1)
    print(i+1, 'inputted word:', word)
    print(i+1, 'english -> p-latin:', out1)
    print(i+1, 'p-latin -> english:', out2)

print(d.check("Numbers!"))
