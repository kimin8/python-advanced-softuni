import re
pattern = r'\w+'
words = {}
with open('words.txt', "r") as file:
    content_in_words_file = file.readline().split(" ")
    with open('text.txt', 'r') as to_check:
        for word in content_in_words_file:
            count_of_word = 0
            
            for line in to_check.readlines():
                only_words = re.findall(pattern, line)
                for i in range(0, len(only_words)):
                    only_words[i] = only_words[i].lower()
                count_of_word += only_words.count(word)
                print(content_in_words_file)
                print(only_words)

            if word in words.keys():
                words[word] += count_of_word
            else:
                words[word] = count_of_word

sorted_dict = sorted(words.items(), key= lambda kvp: (-kvp[1]))

for key in sorted_dict:
    print(f"{key} - {words[key]}")