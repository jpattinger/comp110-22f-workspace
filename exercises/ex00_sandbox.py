my_dict: dict[str, int] = {}
my_dict['j'] = 1
my_dict['f'] = 3
my_dict['r'] = 4
students: dict[int, int] = {}
for key in my_dict.values():
    key += 2
    students[key] = key    
    print(students)

def average_grades(grades: dict[str, list[int]]) -> dict[str, float]:
    result: dict[str, float] = {}
    for students in grades:
        total: int = 0
        for grade in grades[students]:
            total += grade
            result[students] = total / len(grades[students])
    return result
