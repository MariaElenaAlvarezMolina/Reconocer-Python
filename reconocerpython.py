num1 = 42 #Variable declaration
num2 = 2.3 #Variable declaration
boolean = True #Variable declaration
string = 'Hello World' #Variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Composite: list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #Tuple
print(type(fruit)) #Tuple: initialize
print(pizza_toppings[1]) #List: access value
pizza_toppings.append('Mushrooms') #List: add value
print(person['name']) #Dictionary: access value
person['name'] = 'George' #Dictionary: change value
person['eye_color'] = 'blue' #Dictionary: add value
print(fruit[2]) #Tuple: access value

if num1 > 45: #Conditional: if
    print("It's greater") #Log statement
else: #Conditional: else
    print("It's lower") #Log statement

if len(string) < 5: #Conditional: if
    print("It's a short word!") #Log statement
elif len(string) > 15: #Conditional: else if
    print("It's a long word!") #Log statement
else: #Conditional: else
    print("Just right!") #Log statement

for x in range(5): #for loop: start
    print(x) #for loop: stop
for x in range(2,5):#for loop: sequence
    print(x) #for loop: stop
for x in range(2,10,3): #for loop: sequence
    print(x) #for loop: stop

x = 0 #Variable declaration
while(x < 5): #while loop: start
    print(x) #while loop: stop
    x += 1 #while loop: increment

pizza_toppings.pop() #List: delete value
pizza_toppings.pop(1) #List: delete value

print(person) #Log statement
person.pop('eye_color') #Dictionary: delete value
print(person) #Log statement

for topping in pizza_toppings: #for loop: start
    if topping == 'Pepperoni': #conditional: if
        continue #for loop: continue
    print('After 1st if statement') #Log statement
    if topping == 'Olives': #conditional: if
        break #for loop: break

def print_hello_ten_times(): #Function: parameter
    for num in range(10): #Function: argument
        print('Hello') #Log statement

print_hello_ten_times() #Function: return

def print_hello_x_times(x): #Function: parameter
    for num in range(x): #Function: argument
        print('Hello') #Log statement

print_hello_x_times(4) #Function: return

def print_hello_x_or_ten_times(x = 10): #Function: parameter
    for num in range(x): #Function: argument
        print('Hello') #Log statement

print_hello_x_or_ten_times() #Function: return
print_hello_x_or_ten_times(4) #Function: return


"""
Bonus section
"""

#print(num3) #NameError: name <variable name> is not defined
#num3 = 72 #Variable declaration
#fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
#print(person['favorite_team']) #KeyError: 'favorite_team'
#print(pizza_toppings[7]) #IndexError: list index out of range
#  print(boolean) #IndentationError: unexpected indent
#fruit.append('raspberry') #AttributeError: 'tuple' object has no attibute 'append'
#fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'