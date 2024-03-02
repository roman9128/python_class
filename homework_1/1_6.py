age = int(input("Ваш возраст (полных лет): "))
salary = int(input("Ваша ЗП: "))
expenses_for_loans = int(input("Ваши расходы по кредитам: "))
wanted_loan = int(input("Сколько хотите взять в кредит: "))
time_for_pay = int(input("На какой срок (в месяцах): "))
refuse_age = int(50)
payment_per_month = wanted_loan / time_for_pay
if (expenses_for_loans + payment_per_month > salary / 2) or (time_for_pay / 12 + age > refuse_age):
    print("Отказ")
else:
    print("Ваша заявка одобрена")