with open('input.txt', 'r') as file:
    lines = file.readlines()
new_lines = [line for line in lines if line.upper().startswith('A')]
with open('output.txt', 'w') as file:
    for line in new_lines:
        file.write(line)