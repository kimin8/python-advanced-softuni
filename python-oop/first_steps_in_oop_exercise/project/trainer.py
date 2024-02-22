from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, input_pokemon: Pokemon):
        if input_pokemon not in self.pokemons:
            self.pokemons.append(input_pokemon)
            return f"Caught {input_pokemon.pokemon_details()}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for obj in self.pokemons:
            if pokemon_name == obj.name:
                self.pokemons.remove(obj)
                return f"You have released {pokemon_name}"
            else:
                return "Pokemon is not caught"

    def trainer_data(self):
        message_to_return = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for element in self.pokemons:
            message_to_return += f"- {element.pokemon_details()}\n"
        return message_to_return.strip()
