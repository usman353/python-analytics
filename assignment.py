def replace(test_string, replace_string):
    new_str = str.replace(test_string, replace_string, 'bodega', 1)
    return new_str


print(replace('how are you?-you and you are fine and you are working', 'are'))
