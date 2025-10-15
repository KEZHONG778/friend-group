"""An example of how to represent a group of acquaintances in Python."""

my_group ={
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "friend": ["Zalika"],
            "partner": ["John"]
        }
    },
    "Zalika": {
        "age": 28, 
        "job": "artist",
        "relations": {
            "friend": ["Jill"]
        }
    },
    "John": {
        "age": 27,
        "job": "writer", 
        "relations": {
            "partner": ["Jill"],
            "cousin": ["Nash"]
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "cousin": ["John"],
            "landlord": ["Zalika"]  
        }
    }
}


if __name__ == "__main__":
    for name, info in my_group.items():
        print(f"{name} ({info['age']}age, {info['job']}) relationship：")
        for relation, people in info["relations"].items():
            print(f"  - {relation}: {', '.join(people)}")
        print()

# the maximum age of people in the group
    max_age = max([person["age"] for person in my_group.values()])
    print("Maximum age in group:", max_age)

#the average number of relations among members of the group
    avg_relations = sum(
        [sum(len(v) for v in person["relations"].values()) for person in my_group.values()]
    ) / len(my_group)
    print("Average number of relations:", round(avg_relations, 2))

#the maximum age of people in the group that have at least one relation
    max_age_with_relations = max([
        person["age"]
        for person in my_group.values()
        if any(person["relations"].values())
    ])
    print("Max age with at least one relation:", max_age_with_relations)

#the maximum age of people in the group that have at least one friend
    max_age_with_friend = max([
        person["age"]
        for person in my_group.values()
        if "friend" in person["relations"] and person["relations"]["friend"]
    ])
    print("Max age with at least one friend:", max_age_with_friend)