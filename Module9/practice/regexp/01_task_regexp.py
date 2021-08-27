# Дано произвольное предложение. Слова разделены пробелами. Предложение содержит знаки препинания.
# Найдите:
# 1) первое слово из строки
# 2) первые два символа каждого слова
# 3) все слова начинающиеся на гласную букву
# 4) все слова начинающиеся на согласную букву
# 5) все уникальные(без дубликатов) знаки препинания



template1 = r"^\b[A-Z]\w*"
template2 = r"\b\w{2}"
template3 = r"\b[AEIOUaeiou]"
template4 = r"\b[^AEIOUaeiou]"
template5 = r"[,.!&:;-]"
text = "There are many variations of passages of Lorem Ipsum available. \n But the majority have suffered alteration in some form, by injected humour."
res = re.findall(template5,text)
res_uniq = []
for sign in res:
    if sign not in res_uniq:
        res_uniq.append(res)
print("первое слово из строки",re.findall(template1,text))
print("первые два символа каждого слова",re.findall(template2,text))
print("все слова начинающиеся на гласную букву",re.findall(template3,text))
print("все слова начинающиеся на соласную букву",re.findall(template3,text))
print("все уникальные(без дубликатов) знаки препинания",res_uniq)
