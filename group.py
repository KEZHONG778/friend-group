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


if __name__ == "__main__":
    for name, info in my_group.items():
        print(f"{name} ({info['age']}age, {info['job']}) relationship：")
        for relation, people in info["relations"].items():
            print(f"  - {relation}: {', '.join(people)}")
        print()