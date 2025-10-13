"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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


def forget(person1, person2):
    for person in [person1, person2]:
        if person in my_group:
            for relation_type in list(my_group[person]['relations'].keys()):
                if person2 in my_group[person]['relations'].get(relation_type, []):
                    my_group[person]['relations'][relation_type].remove(person2)

def add_person(name, age, job=None, relations=None):
    my_group[name] = {
        "age": age,
        "job": job,
        "relations": relations or {}
    }

def average_age():
    ages = [info['age'] for info in my_group.values()]
    return sum(ages) / len(ages) if ages else 0



print(f"average age: {average_age()}")

add_person("Tom", 30, "engineer")

forget("Jill", "Zalika")

if __name__ == "__main__":
    for name, info in my_group.items():
        print(f"{name} ({info['age']}age, {info['job']}) relationship：")
        for relation, people in info["relations"].items():
            print(f"  - {relation}: {', '.join(people)}")
        print()