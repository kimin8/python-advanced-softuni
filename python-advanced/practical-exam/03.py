def cookbook(*args):
    book_with_recipes = {}
    sorted_book_with_recipes = {}

    for recipe_name, cuisine, list_of_ingredients in args:
        if cuisine in book_with_recipes.keys():
            book_with_recipes[cuisine][recipe_name] = list_of_ingredients
        else:
            book_with_recipes[cuisine] = {recipe_name: list_of_ingredients}

    book_sorted = sorted(book_with_recipes.items(), key = lambda kvp: (-len(kvp[1]), kvp[0]))

    for cuisine, rec_ing_dict in book_sorted:
            sorted_pairs = sorted(rec_ing_dict.items(), key = lambda kvp: kvp[0])
            mini_dict = {}
            for name, ing in sorted_pairs:
                 mini_dict[name] = ing
            sorted_book_with_recipes[cuisine] = mini_dict

    result_message = ""
    for key in sorted_book_with_recipes.keys():
        result_message += f"{key} cuisine contains {len(sorted_book_with_recipes[key].values())} recipes:\n"
        for key_two in sorted_book_with_recipes[key]:
            result_message += f"  * {key_two} -> Ingredients: {', '.join(sorted_book_with_recipes[key][key_two])}\n"
    return result_message.strip()
