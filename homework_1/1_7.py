flag = False
age = int(input("Ваш возраст (полных лет): "))
salary = int(input("Ваша ЗП: "))
expenses_for_loans = int(input("Ваши расходы по кредитам: "))
wanted_loan = int(input("Сколько хотите взять в кредит: "))
time_for_pay = int(input("На какой срок (в месяцах): "))
refuse_age = int(50)
payment_per_month = wanted_loan / time_for_pay
new_term_for_pay = time_for_pay
offered_loan = wanted_loan
if (expenses_for_loans + payment_per_month > salary / 2) or (time_for_pay + age * 12 > refuse_age * 12):
    while new_term_for_pay + age * 12 < refuse_age * 12:
        if (offered_loan / new_term_for_pay + expenses_for_loans < salary / 2) and offered_loan > 1000:
            if flag == False:
                print(f"Предлагаем Вам взять {offered_loan} на {new_term_for_pay} мес.")
                flag = True
        else:
            new_term_for_pay = new_term_for_pay + 1
            offered_loan = offered_loan - 100
    else:
        print(f"Для Вас спецпредложение 1000 рублей на 1 месяц")
else:
    print("Ваша заявка одобрена")