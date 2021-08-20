class Province:
    name = ''
    population = 0.0
    rank = ''

    def __init__(self, name, population, rank):
        self.name = name
        self.population = population
        self.rank = rank


def search_province(provs, query):
    for prov in provs:
        if prov.name == query:
            return prov
    return None


if __name__ == '__main__':
    provinces = [
        Province("Cebu", 4632359, "1"),
        Province("Cavite", 3678301, "2"),
        Province("Bulacan", 3292071, "3"),
        Province("Negros Occidental", 3059136, "4"),
        Province("Laguna", 3035081, "5"),
        Province("Pangasinan", 2956726, "6"),
        Province("Rizal", 2884227, "7"),
        Province("Batangas", 2694335, "8"),
        Province("Pampanga", 2609744, "9"),	
    ]
    userInput = input("Enter a province: ")
    searched_province = search_province(provinces, userInput)
    print(f"{searched_province.name}’s population is {searched_province.population} and " +
          f"is at rank {searched_province.rank}")