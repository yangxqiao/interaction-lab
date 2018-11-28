import random


def make_a_decision(options):
    not_valid_answer = True
    while not_valid_answer and len(options) != 0:
        answer = raw_input('You can pick a number between 1 and ' + str(len(options)) + '\n')
        int_answer = int(answer)
        if int_answer <= len(options) and int_answer > 0:
            not_valid_answer = False
            return int_answer - 1


def ask_for_final_choice(options, number, category):
    print ("Great! We have following %s offered: " % options[number])
    for key, value in category.items():
        if key == options[number]:
            for i in range(len(value)):
                print(str(i + 1) + '. ' + value[i])
            what_to_eat = make_a_decision(value)
            customer_final_choice.append(value[what_to_eat])


customer_final_choice = []

my_dictionary = {"greeting": ["Hi.", "Hello.", "Hey."],
                 "warm up questions": ["How's your day going?", "What's up?", "How's everything going?",
                                       "How are you?"],
                 "nice": ["Great!","Perfect!","Nice!","Sure"],
                 "minutes": ["5", "10", "15", "20", "25", "20"]}

text_1 = "{greeting} {warm up questions}"


my_new_dictionary = {}
for key, value in my_dictionary.items():
    if type(value) != list:
        value = [value]
    my_new_dictionary[key] = random.choice(value)

print (text_1.format(**my_new_dictionary))

sample_yes_answer = ['yeah', 'yes', 'sure', 'definitely', 'of course', 'yup']
answer_for_food = raw_input("Do you want any food?\n")

for key, value in my_dictionary.items():
    if key == "minutes":
        waiting_time = random.choice(value)

order_food = False
order_drinks = False
order_dessert = False
order_check = False

# what if printing 'ye'
if answer_for_food.lower() in sample_yes_answer:
    order_food = True
elif answer_for_food.lower() == "no":
    answer_for_drinks = raw_input("Do you want any drinks?\n")
    if answer_for_drinks.lower() in sample_yes_answer:
        order_drinks = True
    elif answer_for_drinks.lower() == "no":
        answer_for_dessert = raw_input("Do you want any dessert?\n")
        if answer_for_dessert.lower() in sample_yes_answer:
            order_dessert = True
        elif answer_for_dessert.lower() == "no":
            print("Thank you for your time. You can order again whenever you want. Bye.")

if order_food or order_drinks or order_dessert:
    print("Great! I'm also hungry! What do you want?\n")


# block for food
if order_food:
    food_options = [
        'chinese food',
        'mexican food',
        'burger',
        'sushi',
    ]

    food = {"chinese food": ['kong pao chicken','beijing beef','noodles','pork dumplings','duck\'s feet'],
            "mexican food": ['tostada','taco','chilaquiles','sweet potatoes'],
            "burger": ['fish burger','chicken burger','cheese burger'],
            "sushi": ['spicy tuna','california roll','philadelphia roll']
            }

    for i in range(len(food_options)):
        print(str(i + 1) + '. ' + food_options[i])
    order_food = False

    food_number = make_a_decision(food_options)

    ask_for_final_choice(food_options,food_number,food)

    answer_for_drinks = raw_input("Do you want any drinks?\n")
    if answer_for_drinks.lower() in sample_yes_answer:
        order_drinks = True
    elif answer_for_drinks.lower() == "no":
        answer_for_dessert = raw_input("Do you want any dessert?\n")
        if answer_for_dessert.lower() in sample_yes_answer:
            order_dessert = True
        elif answer_for_dessert.lower() == "no":
            answer_for_checking = raw_input("Thanks for ordering! Do you want to check you orders?\n")
            if answer_for_checking in sample_yes_answer:
                order_check = True
            elif answer_for_checking == "no":
                print("If there is no question, then please wait for %s minutes." % waiting_time)



# block for drinks
if order_drinks:
    if order_food:
        for key, value in my_dictionary.items():
            if key == "nice":
                word_nice = random.choice(value)
                print(word_nice)

    drinks_options = ['alcohol',
                      'coffee',
                      'chocolate',
                      'soft drinks',]

    drinks = {"alcohol": ["beer","cider","cocktail","wine","mixed drinks"],
              "coffee": ["cappuccino","flat white","cafe mocha","latte"],
              "chocolate": ["hot chocolate", "cream frozen hot chocolate"],
              "soft drinks": ["cola","carbonate water","lemon-lime drink","pepsi"]}

    for i in range(len(drinks_options)):
        print(str(i+1) + '. ' + drinks_options[i])

    drinks_number = make_a_decision(drinks_options)

    ask_for_final_choice(drinks_options,drinks_number,drinks)

    answer_for_dessert = raw_input("Do you want any dessert?\n")
    if answer_for_dessert.lower() in sample_yes_answer:
        order_dessert = True
    elif answer_for_dessert.lower() == "no":
            answer_for_checking = raw_input("Thanks for ordering! Do you want to check you orders?\n")
            if answer_for_checking in sample_yes_answer:
                order_check = True
            elif answer_for_checking == "no":
                print("If there is no question, then please wait for %s minutes." % waiting_time)


# block for dessert
if order_dessert:
    if order_food or order_drinks:
        for key, value in my_dictionary.items():
            if key == "nice":
                word_nice = random.choice(value)
                print(word_nice)

    dessert_options = ["pie",
                       "cake",
                       "pudding",
                       "ice cream",]

    dessert = {"pie": ["apple pie","banana pie","blueberry pie"],
               "cake":["cheesecake","straberry sponge cake","red velvet cake","coffee cake","chocolate brownie","swiss roll"],
               "pudding": ["banana pudding","custard","chocolate pudding"],
               "ice cream": ["mint chocolate ice cream","green tea ice cream","cookies and cream","strawberry sundae"],}

    for i in range(len(dessert_options)):
        print(str(i+1) + '. ' + dessert_options[i])

    dessert_number = make_a_decision(dessert_options)

    ask_for_final_choice(dessert_options,dessert_number,dessert)

    answer_for_checking = raw_input("Thanks for ordering! Do you want to check you orders?\n")
    if answer_for_checking in sample_yes_answer:
        order_check = True
    elif answer_for_checking == "no":
        print("If there is no question, then please wait for %s minutes." % waiting_time)


# print final answer
if order_check:
    print("You have ordered: ")
    for i in range(len(customer_final_choice)):
        print customer_final_choice[i]

    print("If there is no question, then please wait for %s minutes." % waiting_time)