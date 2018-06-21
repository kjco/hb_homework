"""Print out all the melons in our inventory."""


from melons import melon_lst, info_lst, melon_info_dict


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

#    print(f"{name}s {have_or_have_not} seeds and are ${price:.2f}")


# for i in melon_names:
    # print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])


#print(melon_info_dict)
#print(info_lst)


#print(blank_info_dict)

def print_melon_info(lst_of_melons, lst_of_info, dict_of_melons):
    for melon in lst_of_melons:
        dict_of_melons[melon] = dict_of_melons.get(melon, {})
        for feature in lst_of_info:
            dict_of_melons[melon][feature] = dict_of_melons[melon].get(feature, None)

        print("{}\n  price: {}\n  seedless: {}\n  weight: {}\n  flesh_color: {}\n  rind_color: {}".format(
            melon, dict_of_melons[melon]["price"], 
            dict_of_melons[melon]["seedless"],
            dict_of_melons[melon]["weight"],
            dict_of_melons[melon]["flesh_color"],
            dict_of_melons[melon]["rind_color"]))
#    print(dict_of_melons)


print_melon_info(melon_lst, info_lst, melon_info_dict)
    
