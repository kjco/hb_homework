melon_names = {
    1: "Honeydew",
    2: "Crenshaw",
    3: "Crane",
    4: "Casaba",
    5: "Cantaloupe",
}

melon_prices = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedlessness = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}


# seedless: False
# price: 2.5
# flesh_color: None
# weight: None
# rind_color: None

melon_lst = []
for key, value in melon_names.items():
    melon_lst.append(value)
# print(melon_lst)
melon_lst.append("Watermelon")

info_lst = ["price", "seedless", "flesh_color", "weight", "rind_color"]
# print(info_lst)

melon_info_dict = {}

for key in melon_names.keys():
    melon_info_dict[melon_names[key]] = {"price": melon_prices[key],
    "seedless": melon_seedlessness[key]}

# print(melon_info_dict)
