import json

class Student:
    def __init__(self, name, sname, year, marks):
        self.name = name
        self.sname = sname
        self.year = year
        self.marks = marks

    def to_dict(self):
        return {
            "Name": self.name,
            "SName": self.sname,
            "Year": self.year,
            "Marks": self.marks
        }

def save_students_to_file(students, filename):
    with open(filename, 'w') as file:
        json.dump([student.to_dict() for student in students], file, indent=4)

def load_students_from_file(filename):
    with open(filename, 'r') as file:
        return [Student(**data) for data in json.load(file)]

def main():
    students = []
    for i in range(5): 
        name = input(f"Введіть ім'я учня {i + 1}: ")
        sname = input(f"Введіть прізвище учня {i + 1}: ")
        year = int(input(f"Введіть рік народження учня {i + 1}: "))
        marks = list(map(int, input(f"Введіть оцінки учня {i + 1} через кому: ").split(',')))
        
        students.append(Student(name, sname, year, marks))

    save_students_to_file(students, 'students.json')

    while True:
        try:
            student_number = int(input("Введіть номер учня (1-5) для перегляду даних, або 0 для виходу: "))
            if student_number == 0:
                break
            if 1 <= student_number <= 5:
                student = students[student_number - 1]
                print(f"Дані учня {student_number}:")
                print(f"Ім'я: {student.name}")
                print(f"Прізвище: {student.sname}")
                print(f"Рік народження: {student.year}")
                print(f"Оцінки: {student.marks}")
            else:
                print("Неправильний номер учня. Спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, введіть коректний номер.")

if __name__ == "__main__":
    main()
