#Getting user choice/input
choice = int(input("CHOICES \n1. Convert kg to lb \n2. Convert lb to kg \nYour input: "))

if 1 <= choice <= 2:
    #Converting kg to lb
    if choice == 1:
        kg_value = float(input("\nEnter weight in kg: "))
        lb_value = kg_value*2.205
        print(f"\nWeight in kg: {kg_value} \nWeight in lb: {lb_value:.2f}")

    #Converting lb to kg
    elif choice == 2:
        lb_value = float(input("\nEnter weight in lb: "))
        kg_value = lb_value/2.205
        print(f"\nWeight in lb: {lb_value} \nWeight in kg: {kg_value:.2f}")

else:
    print("\nInvalid input.")
