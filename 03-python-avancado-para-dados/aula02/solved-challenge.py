# exercise 1 data-engineering-roadmap  
# instructions

# name validation block
while True:
    try:
        name = input("Please, type your name: ").strip().title()
        if len(name) == 0:
            raise ValueError("Please, fill the field 'name'")
        elif not name.replace(" ", "").isalpha():
            raise ValueError("Name cannot have numbers or special caracters")
        else:
            print(f"Valid name: {name}")
    except Exception as e:
        print(e)
        break

# income validation block
    try:
        income = float(input("Please inform your income: "))
        if income <= 0:
            print("income must be bigger than 0")
            break
    except Exception:
        print("income must be a number")
        break
        
# bonus validation block
    try:
        bonus = float(input("Please inform your bonus: "))
    except Exception:
        print("Bonus must be a number")
        break
    if bonus <= 0:
        raise ValueError("Bonus must be bigger than 0")

    # final calculations
    final_bonus = bonus * 1.2  
    kpi = (income + final_bonus) / 1000  

    print(f"Your KPI is: {kpi:.2f}")
    print(f"{name}, your income is: ${income} and your total bonus is: ${final_bonus:.2f}.")
    break