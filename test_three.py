from collections import Counter

colors = ['teal', 'PINK', 'PURPLE', 'ORANGE', 'green', 'BLUE', 'YELLOW', 'red', 'pink', 'TEaL', 'PurPLE', 'greEn', 'YELLOW', 'ORAnGE', 'blue', 'RED', 'teal', 'PINk', 'purPle', 'orange', 'GREEN', 'BluE', 'YelLow', 'ReD']

#Exercise 1
print(f'Number of colors: {len(colors)}')

#Exercise 2
colors_fixed = []
for items in colors:
    colors_fixed.append(items.lower())
counts = Counter(colors_fixed)
print(list(counts))

#Exercisa 3
color = "red"
print(f"The color {color} exists: {counts[color]} times")