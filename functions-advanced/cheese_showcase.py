def sorting_cheeses(**kwargs):
    cheese_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    
    result = []

    for (cheese_name, quantity) in cheese_dict:
        result.append(cheese_name)
        quantity_list = sorted(quantity, reverse=True)
        result += quantity_list
    
    return "\n".join([str(x) for x in result])

print(sorting_cheeses(Parmesan=[102, 120, 135],Camembert=[100, 100, 105, 500, 430],Mozzarella=[50, 125]))