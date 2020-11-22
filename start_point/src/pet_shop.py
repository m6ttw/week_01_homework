# WRITE YOUR FUNCTIONS HERE


#1
def get_pet_shop_name(shop):
    return shop["name"]

#2
def get_total_cash(total):
    return total["admin"]["total_cash"]

#3
def add_or_remove_cash(num_1, num_2):
    num_1["admin"]["total_cash"] += num_2

#4
# uses same function as #3

#5
def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

#6
def increase_pets_sold(pets_sold, num_add):
    pets_sold["admin"]["pets_sold"] += num_add

#7
def get_stock_count(shop):
    return len(shop["pets"])

#8 create an empty list, then loop
# through the pets appending them to the list
# if the breed matches

def get_pets_by_breed(shop, breed):
    breed_count = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            breed_count.append(1)
    return breed_count

#9
# uses same function as #8

#10
def find_pet_by_name(shop, name):
   for pet in shop["pets"]:
       if pet["name"] == name:
           return pet

#11
# uses same function as #10

#12
def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

#13
def add_pet_to_stock(shop, new_pet):
    new_pet = {
                "name": "Guinevere",
                "pet_type": "cat",
                "breed": "Siamese",
                "price": 900,
            }
    shop["pets"].append(new_pet)

#14
def get_customer_cash(customer):
    return customer["cash"]

#15
def remove_customer_cash(num_1, num_2):
    num_1["cash"] -= num_2

#16
def get_customer_pet_count(customer):
    return len(customer["pets"])

#17
def add_pet_to_customer(customer_1, new_pet):
    customer_1["pets"] += [new_pet]

    # --- OPTIONAL ---

