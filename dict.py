company = {
    "Engineering": {
        "Alice": {"age": 30, "role": "Senior Engineer", "languages": ["Python", "C++"]},
        "Bob": {"age": 25, "role": "Engineer", "languages": ["JavaScript", "Ruby"]}
    },
    "HR": {
        "Carol": {"age": 32, "role": "HR Manager", "skills": ["Recruitment", "Employee Relations"]},
        "David": {"age": 28, "role": "HR Specialist", "skills": ["Payroll", "Compliance"]}
    }
}
print(company["Engineering"]["Alice"]["languages"])
print(company["Engineering"]["Bob"]["languages"])
print(company["HR"]["Carol"]["skills"])


coordinates = {
    (0, 0): "origin",
    (1, 2): "point A",
    (2, 3): "point B",
}
print(coordinates[(1, 2)])  # Outputs: point A


students = {
    "John": {
        "grades": {"math": 90, "science": 85},
        "attendance": 96,
        "extra_activities": ["chess", "soccer"]
    },
    "Emily": {
        "grades": {"math": 92, "science": 89},
        "attendance": 98,
        "extra_activities": ["drama", "basketball"]
    }
}
print(students["Emily"]["grades"]["math"])  # Outputs: 92


inventory = {
    "fruits": {"apple", "banana", "cherry"},
    "vegetables": {"carrot", "celery", "lettuce"},
    "grains": {"wheat", "rice", "barley"}
}
print("apple" in inventory["fruits"])  # Checks if 'apple' is in the fruit set

