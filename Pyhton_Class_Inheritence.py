class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'**Name: {self.name} and Age: {self.age}'


class Student(User):
    def __init__(self, name, age, degree, semester):
        super().__init__(name, age)
        self.degree = degree
        self.semester = semester

    def __str__(self):
        return f'^{super().__str__()} Degree: {self.degree} and Semester: {self.semester}'
    

class Teacher(User):
    def __init__(self, name, age, qualification, salary):
        super().__init__(name, age)
        self.qualification = qualification
        self.salary = salary

    def __str__(self):
        return f'^{super().__str__()} Qualification: {self.qualification} and Salary: {self.salary}'


x = Student('Sanjay',18,'MTech',1)
print(x)


y = Teacher('Mr. Prabhakar', 47, 'PHd', 150000)
print(y)
