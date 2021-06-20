# import chapter8

def make_pizza_fun(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)



def play_sports(size, *balls):
    """球类运动"""
    print("\nballs： " + str(size) +
          "-plays:")
    for ball in balls:
        print("- " + ball)