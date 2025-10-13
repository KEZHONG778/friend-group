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

def max_age():
   
    max_age = max(info['age'] for info in my_group.values())        
    print(f"max age of the group is {max_age}")

max_age()    

def avg_relations():
    total_relation = sum(len(info['relations']) for info in my_group.values())
    avg_realtions = total_relation/len(my_group)
    print(f"the average relationship  number is{avg_realtions}")

avg_relations()    

def max_age_with_relationship():
    age_with_relationship = []

    for info in my_group.values():
        if info ['relations'] :
            age_with_relationship.append(info ['age'])

    max_age_value_with_relationship = max(age_with_relationship)   
    print(f"the max age with relationship is {max_age_value_with_relationship} ")     

max_age_with_relationship()    

def max_age_with_friends():
    ages_with_friends = []
    
    for info in my_group.values():
        if 'friend' in info['relations']:  
            ages_with_friends.append(info['age'])
    
    if ages_with_friends: 
        max_age_value = max(ages_with_friends)
    else:
        max_age_value = 0
    
    print(f"max age with friends: {max_age_value}")
    
max_age_with_friends()