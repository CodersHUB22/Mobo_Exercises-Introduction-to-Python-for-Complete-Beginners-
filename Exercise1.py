def output(dictionary):
    for i in dictionary.keys():
        print(i)
        for x in dictionary[i]:
            print(x + ": " + dictionary[i][x])
        print()

def gender(dictionary):
    genders = {"Male":[],"Female":[]}
    for i in dictionary.keys():
        if dictionary[i]["gender"] == "Male": genders["Male"].append(i)
        else: genders["Female"].append(i)
    print(genders["Male"])
    print(genders["Female"])


celebrities = {"Drake": {'name': 'Aubrey Drake Graham', 'age': '34', 'gender': 'Male'},
    "Taylor Swift": {'name': 'Taylor Swift', 'age': '31', 'gender': 'Female'},
    "Eminem": {'name': 'Marshall Bruce Mathers III', 'age': '48', 'gender': 'Male'},
    "Post Malone": {'name': 'Austin Richard Post', 'age': '26', 'gender': 'Male'},
    "Ed Sheeran": {'name': 'Edward Christopher Sheeran', 'age': '30', 'gender': 'Male'},
}

output(celebrities)
gender(celebrities)