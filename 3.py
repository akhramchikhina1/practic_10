with open('input.txt', 'r') as file:
    lines = file.readlines()
first_letters = [line[0] for line in lines]
new_word = ''.join(first_letters)
with open('output.txt', 'w') as file:
    file.write(new_word)