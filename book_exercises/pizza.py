# Book lesson
def make_pizza(size, *toppings):
    # Summarizes the pizza about to be made
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")


