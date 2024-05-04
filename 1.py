with open('input.txt', 'r') as f:
    a = f.read()
general = a.upper()
with open('output.txt', 'w') as f:
    f.write(general)