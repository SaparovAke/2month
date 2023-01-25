class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f'Person name is: {self.fullname} age: {self.age} married: {self.is_married}'


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def med(self):
        return (sum(self.marks) // len(self.marks))


class Teacher(Person):
    salary = 10000

    def __init__(self, fullname, age, is_married, experience=3):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def zarplata(self):
        if self.experience > 3:
            new_salary = self.salary + ((self.salary / 100 * 5) * (self.salary * 3))
            return new_salary


teacher = Teacher(fullname='Fcnm', age=25, is_married=True)
print(teacher.introduce_myself())

def create_students():
    student1 = Student("ak", 18, False, marks={
        'история': 5,
        'математика': 4,
        'английский яз.': 4
    })
    student2 = Student("lal", 19, False, marks={
        'история': 5,
        'математика': 4,
        'английский яз.': 5
    })
    student3 = Student("ggg", 19, False, marks={
        'история': 4,
        'математика': 4,
        'английский яз.': 5
    })

    students = [student1, student2, student3]
    return students

p = create_students()
for i in p:
    z = []
    for l in i.marks.values():
        z.append(l)
    print(f"fullname: {i.fullname}\n"
          f"age: {i.age}\n"
          f"is_married: {i.is_married}\n"
          f"marks: {sum(z) / len(z) }")