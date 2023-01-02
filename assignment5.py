data = [12, 75, 150, 180, 145, 525, 50]


for value in data:
    if value % 5 == 0:
        continue
        if value > 150:
            continue
        if value > 500:
            break
print(data)