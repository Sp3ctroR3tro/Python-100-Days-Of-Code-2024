from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
        ["Bulbasaur", "Grass"],
        ["Mewtwo", "Psychic"],
        ["Snorlax", "Normal"],
        ["Marshadow", "Fighting"]

    ]
)
print(table)