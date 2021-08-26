# Пример: для строки 'pythonist'
# Получим словарь: {'p': 1, 'y': 1, 't': 2, 'h': 1, 'o': 1, 'n': 1, 's': 1, 'i': 1}
# Примечание: т.к. ключи неупорядочены, порядок следования ключей может быть произвольным
string = 'pythonist'
found = {}
unique = []
for letter in string:
    found.setdefault(letter,0)
    found[letter] += 1
print(found)
