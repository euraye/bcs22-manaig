def years_of_Service():
    service = int(input("enter your years of service in the company: "))
    salary = int(input("enter your salary: "))

    bonusPercent = [0.05, 1.0, 1.5, 2.0]

    if service < 5:
        print("the amount of years you have worked here is not enough :(")
    else:
        if service >= 5 and service < 10:
            bonus = salary *  bonusPercent[0]
            total(bonus, salary)
        if service >= 10 and service < 15:
            bonus = salary *  bonusPercent[1]
            total(bonus, salary)
        if service >= 15 and service < 20:
            bonus = salary *  bonusPercent[2]
            total(bonus, salary)
        if service >= 20:
            bonus = salary *  bonusPercent[3]
            total(bonus, salary)

def total(bonus, salary):
    totalsalary = bonus + salary
    print(f"You will receive a bonus of PHP {bonus}")
    print(f"Your total salary will be PHP {totalsalary}")

years_of_Service()

