# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    head_ticket_list = []
    tail_ticket_list = []
    while ticket_number > 0:
        digit = ticket_number % 10
        if len(tail_ticket_list) < 3:
            tail_ticket_list.append(digit)
        else:
            head_ticket_list.append(digit)
        ticket_number = ticket_number // 10
    return sum(tail_ticket_list) == sum(head_ticket_list)


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(123006))
print(lucky_ticket(123210))
print(lucky_ticket(436751))
