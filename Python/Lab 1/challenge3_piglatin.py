import enchant 

test_list = ['Quotient','Mustn\'t','Yellow', 'Honest', 'Thursday', 'Christmas', 
             'Alliteration', 'Information', 'Education', 'Fish', 'Numbers!', 'Toyota!',
             'Mother-in-law', 'Laps', 'Slap', 'August', 'empty-handed', 'Ice-cream',
             'Years', 'Yawn', 'Yard', 'Quiet', 'Quack', 'Yttrium', 'Up-to-date']

vowels = "aeiou"

def english_to_pig_latin(word):
    result = ""
    index = 0
    for x in word:
        if x.lower() not in vowels and x.lower() == 'y':
            # print(x)
            result = word[1:] + "y" + "ey"
            break
        elif x.lower() in vowels and index != 0:
            # print(x)
            result = word[index:] + word[:index] + "ay"
            break
        elif x.lower() in vowels and index == 0:
            # print(x)
            result = word + "yay"
            break
        elif x.lower() not in vowels:
            # print(x)
            pass

        index += 1

    return result

def pig_latin_to_english(word): 
    result = ""
    return result

# print(english_to_pig_latin("aloha"))
# print(english_to_pig_latin("yellow"))
# print(english_to_pig_latin("Switch"))

for i, word in enumerate(test_list):
    out1 = english_to_pig_latin(word)  
    # out2 = pig_latin_to_english(out1)
    print(i+1, 'inputted word:', word)
    print(i+1, 'english -> p-latin:', out1)
    # print(i+1, 'p-latin -> english:', out2)
