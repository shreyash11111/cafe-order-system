menu={
    'Maggie': 70,
    'burger': 60,
    'pizza' : 130,
    "chaas" : 20,
    "tea" : 15,
    "coffe" : 20,
    'ice cream' : 30
}

print('Hola !,welcome to our cafe!')
print("")
print('Maggie : 70\nburger : 60\npizza : 130\nchaas : 20\ntea : 15\ncoffe : 20\nice cream:30')

order_total=0

item=(input("what you want to order : "))

if item in menu:
    order_total+=menu[item]
    print(f"{item} is added just give us moment")

else:
    print(f" sorry {item} is not avaliable yet")


update_order=input("Do you want to add more items (Yes/No)").lower()

if update_order== "yes":
    item_2=(input("Enter your item : "))

    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"{item_2} is added in the order")

    else :
        print(f"{item_2} is not in menu")

print(f"Your total is {order_total}")

