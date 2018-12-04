word_to_count = {}
text = input("Text: ").split()

for word in text:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

for key,value in sorted(word_to_count.items()):
    print(key," : ", value)
