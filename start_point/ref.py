def test_add(self):
    add_result = add( 1, 2 )
    self.assertEqual( 3, add_result )

def add( number_1, number_2 ):
    add_result = number_1 + number_2
    return add_result

def test_add_or_remove_cash__add(self):
    add_or_remove_cash(self.cc_pet_shop,10)
    cash = get_total_cash(self.cc_pet_shop)
    self.assertEqual(1010, cash)

def add_or_remove_cash(num_add_a, num_add_b):
    add_or_remove_cash = {self.cc_pet_shop["admin"]["total_cash"]} + num_add_b
    return add_or_remove_cash