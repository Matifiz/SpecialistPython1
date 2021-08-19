names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
i = 0
length = 0
longest = 0
while i < len(names):
    if len(names[i]) > length:
        longest = names[i]
        length = len(names[i])
    i += 1
print(longest)
