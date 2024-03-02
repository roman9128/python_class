age = int(input("Ваш возраст (полных лет): "))
salary = int(input("Ваша ЗП: "))
expenses_for_loans = int(input("Ваши расходы по кредитам: "))
wanted_loan = int(input("Сколько хотите взять в кредит: "))
time_for_pay = int(input("На какой срок (в месяцах): "))
refuse_age = int(50)
payment_per_month = wanted_loan / time_for_pay
if age >= refuse_age:
    print("Мы не выдаём кредиты лицам старше 50 лет")
if (expenses_for_loans + payment_per_month > salary / 2) or (time_for_pay + age * 12 > refuse_age * 12):
    if time_for_pay + age * 12 > refuse_age * 12:
        new_term_for_pay = time_for_pay + 6 * (age - refuse_age)
        if new_term_for_pay > 1:
            if new_term_for_pay + age * 12 <= refuse_age * 12:
                print(f"Предлагаем Вам взять эту же сумму на {new_term_for_pay} месяцев")
    elif expenses_for_loans + payment_per_month > salary / 2:
        offered_loan = wanted_loan - (expenses_for_loans + payment_per_month - salary / 2)



else:
    print("Ваша заявка одобрена")