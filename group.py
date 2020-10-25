group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}

#the maximum age of people in the group
ages = []
numsOfRelation = []
agesWithRelation = []
agesWithFriend = []
for ppl, info in group.items():
    age = info["age"]
    ages.append(age)

    numOfRelation = len(info["relations"])
    numsOfRelation.append(numOfRelation)

    if len(info['relations']) != 0:
        agesWithRelation.append(age)

    for ppls, relation in info["relations"].items():
        if "friend" in relation:
            agesWithFriend.append(age)


print(max(ages))
print(max(numsOfRelation))
print(max(agesWithRelation))
print(max(agesWithFriend))