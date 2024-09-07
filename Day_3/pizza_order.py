
def pizza_order_calculator(size, add_pepperoni, extra_cheese):
    total_bill = 0
    while True:
        if size == "s" or size == "S":
            total_bill += 15
        elif size == "m" or size == "M":
            total_bill += 20
        elif size == "l" or size == "L":
            total_bill += 25
        else:
            print("Not a valid size, please select again")
            return

        if add_pepperoni == "y" or add_pepperoni == "Y":
            if size == "s" or size == "S":
                total_bill += 2
            else:
                total_bill += 3

        if extra_cheese == "y" or extra_cheese == "Y":
            total_bill += 1

        return total_bill


def main():
    print("Thank you for choosing Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L: \n")
    add_pepperoni = input("Do you want pepperoni? Y or N: \n")
    extra_cheese = input("Do you want extra cheese? Y or N: \n")

    final_bill = pizza_order_calculator(size, add_pepperoni, extra_cheese)
    print(f"Your final bill is {final_bill}.")


if __name__ == "__main__":
    main()

