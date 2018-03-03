

def word_distribution(string):
    import re
    dict1 = {}
    split_text = string.split(' ')
    new_list = list()
    for word in split_text:
        new_list.append(re.sub('^[^a-zA-z]+|[^a-zA-Z]+$', '', word))
    for item in new_list:
        item = item.lower()
        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1
    return dict1


text_string = 'Hello. How how how ??>how?/ are you? Please say hello if you don’t love me!'

print(word_distribution(text_string))
