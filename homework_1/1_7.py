age = int(input("Ваш возраст (полных лет): "))
salary = int(input("Ваша ЗП: "))
expenses_for_loans = int(input("Ваши расходы по кредитам: "))
wanted_loan = int(input("Сколько хотите взять в кредит: "))
time_for_pay = int(input("На какой срок (в месяцах): "))
refuse_age = int(50)
payment_per_month = wanted_loan / time_for_pay
free_money_to_pay = salary / 2 - expenses_for_loans - 0.1
max_available_time_to_pay = (refuse_age - age) * 12
max_available_loan = max_available_time_to_pay * free_money_to_pay
min_available_time_to_pay = max_available_loan / free_money_to_pay

if (expenses_for_loans + payment_per_month > salary / 2) or (time_for_pay + age * 12 > refuse_age * 12):
    if (max_available_loan > 1000) or max_available_time_to_pay > 1:
        if max_available_loan < wanted_loan:
            print(f"Максимум мы можем Вам предложить {max_available_loan} рублей на {min_available_time_to_pay} мес. по {free_money_to_pay} руб. в мес.")
        else:
            print(f"Мы можем одобрить Вам {wanted_loan} на {int(wanted_loan / free_money_to_pay)} мес. по {free_money_to_pay} руб. в мес.")
    else:
        print(f"Для Вас спецпредложение 1000 рублей на 1 месяц")
else:
    print("Ваша заявка одобрена")