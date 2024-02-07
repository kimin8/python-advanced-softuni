def team_lineup(*player_base):
    football_wiki = {}

    for name, nationality in player_base:
        if nationality in football_wiki.keys():
            football_wiki[nationality].append(name)
        else:
            football_wiki[nationality] = [name]
    
    sorted_football_wiki = sorted(football_wiki.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = ""

    for country in sorted_football_wiki:
        result += f"{country[0]}:\n"
        country = country[1]
        for item in country:
            result += f"  -{item}\n"
    
    return result.strip()