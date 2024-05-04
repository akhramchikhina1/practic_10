with open('input.txt', 'r') as file:
    steps_data = file.readlines()

s_month = [0] * 12 #для общ колва шагов каждого мес года
d_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, steps in enumerate(steps_data):
    month_index = i % 12
    s_month[month_index] += int(steps)

average = [steps // d_month[i] for i, steps in enumerate(s_month)]

with open('output.txt', 'w') as file:
    for a in average:
        file.write(str(a) + '\n')