#usage of basic if else and for loop its easy

#dictionaries
myage = 1


infos = {'name' : 'sur',
         'age' : 21,
         'sex' : 'male'}
print(infos)

infos['phone'] = 'IQOO'
print(infos)

del infos['phone']

print(infos)
#learnt some looping modifying and creating using ranage and loops many times

#basic inputs

# name = input("What's ur name\n");
# print(f"hello {name}, How are you!")

myage = 1

while myage<10:
    print(myage)
    myage +=1


# message = input("repeat : ")
# print(message)


#functions

def greet():
    print("greet hello")

greet()


def greet_user(name,age):
    print(f"well hello {name} u are "+ str(age) + " years old")
greet_user('suraj',9)



def hello_user(names):
    for name in names:
        print(f"Well Hello {name}, How are you")

names = ['suraj','chinmay','rajiv','sam']

hello_user(names)


unprinted_model = ['tesla','tata','lambo']
completed_model = []

while unprinted_model:
    current_model = unprinted_model.pop()
    print("printing model : " + current_model)
    completed_model.append(current_model)

print("the following models are printed : ")
for model in completed_model:
    print(model)


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')