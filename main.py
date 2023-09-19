# PYAPI-88 Homework #1. OOP: inheritance, encapsulation and polymorphism. Student Akhmarov Ruslan

# Defining classes. Classes Student and Mentor are already defined.
# Classes Lecturer and Reviewer must inherit from class Mentor.
class Student:
    """Defines platform student. Contains student's name, surname,
    gender, list of finished courses, list of courses in progress
    and a dictionary of student's homework grades.
    """
    def __init__(self, name, surname, gender):
        """List of finished courses, list of courses in progress
        and a dictionary of student's homework grades are empty by default.
        """
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Overloading methods for formatted output and comparison of class instances.
    # Instances can be compared by the mean value of all grades.
    def __str__(self):
        string = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за домашние задания: {self.calc_mean()}\n'
                  f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                  f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return string

    def __gt__(self, other):
        return self.calc_mean() > other.calc_mean()

    def __lt__(self, other):
        return self.calc_mean() < other.calc_mean()

    def __eq__(self, other):
        return self.calc_mean() == other.calc_mean()

    # Defining method for calculation of a mean value of grades. Only used by internal methods.
    def calc_mean(self):
        """Calculates and returns the mean value of all student's grades"""
        course_mean = [sum(val) / len(val) for val in self.grades.values()]
        grades_mean = sum(course_mean) / len(course_mean)
        return grades_mean

    # Defining method for students to rate lectures
    def rate_lecture(self, lecturer, course, grade):
        """Takes Lecturer instance, string course title and grade number.
        Adds given grade to the corresponding Lecturer instance attribute.
        """
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    """Defines platform mentor. Contains mentor's name, surname and attached courses."""
    def __init__(self, name, surname):
        """List of attached courses is empty by default."""
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Defining Lecturer class which should inherit attributes from Mentor class
class Lecturer(Mentor):
    """Defines platform lecturer. Inherits all attributes from Mentor class.
    Also contains a dictionary of grades for their lectures.
    """
    def __init__(self, name, surname):
        """Dictionary of lecture grades is empty by default"""
        super().__init__(name, surname)
        self.lecture_grades = {}

    # Overloading methods for formatted output and comparison of class instances.
    # Instances can be compared by the mean value of all lecture grades.
    def __str__(self):
        string = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}\n'
                  f'Средняя оценка за лекции: {self.calc_mean()}')
        return string

    def __gt__(self, other):
        return self.calc_mean() > other.calc_mean()

    def __lt__(self, other):
        return self.calc_mean() < other.calc_mean()

    def __eq__(self, other):
        return self.calc_mean() == other.calc_mean()

    # Method for calculation of a mean value of grades. Only used by internal methods.
    def calc_mean(self):
        """Calculates and returns the mean value of all lecture grades"""
        course_mean = [sum(val) / len(val) for val in self.lecture_grades.values()]
        grades_mean = sum(course_mean) / len(course_mean)
        return grades_mean


# Defining Reviewer class which should inherit attributes from Mentor class
class Reviewer(Mentor):
    """Defines platform Reviewer. Inherits all attributes from Mentor class"""
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        string = (f'Имя: {self.name}\n'
                  f'Фамилия: {self.surname}')
        return string

    # Defining method for reviewers to grade students' homework
    def rate_hw(self, student, course, grade):
        """Takes Student instance, string course title and grade number.
        Adds given grade to the corresponding Student instance attribute.
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Creating 2 instances of each defined class to test out defined methods
student_a = Student('Ruoy', 'Eman', 'your_gender')
student_a.courses_in_progress += ['Python', 'Docker']
student_a.finished_courses += ['Maths in DS']

student_b = Student('Ivan', 'Durak', 'your_gender')
student_b.courses_in_progress += ['Python', 'Git']
student_b.finished_courses += ['Introduction to ML']

lecturer_a = Lecturer('Bob', 'Coolguy')
lecturer_a.courses_attached += ['Git', 'Docker']

lecturer_b = Lecturer('Larry', 'Notsocool')
lecturer_b.courses_attached += ['Python']

reviewer_a = Reviewer('Idris', 'Mecha')
reviewer_a.courses_attached += ['Git', 'Docker']

reviewer_b = Reviewer('Pavel', 'A+')
reviewer_b.courses_attached += ['Python']

# Testing out defined methods
reviewer_a.rate_hw(student_a, 'Docker', 6)
reviewer_a.rate_hw(student_a, 'Docker', 8)
reviewer_a.rate_hw(student_b, 'Git', 7)
reviewer_a.rate_hw(student_b, 'Git', 9)

reviewer_b.rate_hw(student_a, 'Python', 8)
reviewer_b.rate_hw(student_a, 'Python', 6)
reviewer_b.rate_hw(student_b, 'Python', 7)
reviewer_b.rate_hw(student_b, 'Python', 10)

student_a.rate_lecture(lecturer_a, 'Docker', 6)
student_a.rate_lecture(lecturer_a, 'Docker', 8)
student_a.rate_lecture(lecturer_b, 'Python', 9)
student_a.rate_lecture(lecturer_b, 'Python', 9)

student_b.rate_lecture(lecturer_a, 'Git', 7)
student_b.rate_lecture(lecturer_a, 'Git', 9)
student_b.rate_lecture(lecturer_b, 'Python', 8)
student_b.rate_lecture(lecturer_b, 'Python', 10)

# Testing out overloaded standard methods
print(f'СТУДЕНТ 1\n{student_a}', '\n')
print(f'СТУДЕНТ 2\n{student_b}', '\n')

print(f'ЛЕКТОР 1\n{lecturer_a}', '\n')
print(f'ЛЕКТОР 2\n{lecturer_b}', '\n')

print(f'ЭКСПЕРТ 1\n{reviewer_a}', '\n')
print(f'ЭКСПЕРТ 2\n{reviewer_b}', '\n')

if student_a < student_b:
    print(f'Средний балл у студента {student_a.name} меньше, чем у студента {student_b.name}')
elif student_a == student_b:
    print(f'Средние баллы студентов {student_a.name} и {student_b.name} равны')
else:
    print(f'Средний балл у студента {student_a.name} больше, чем у студента {student_b.name}')

if lecturer_a < lecturer_b:
    print(f'Средний балл у лектора {lecturer_a.name} меньше, чем у лектора {lecturer_b.name}')
elif lecturer_a == lecturer_b:
    print(f'Средние баллы лекторов {lecturer_a.name} и {lecturer_b.name} равны')
else:
    print(f'Средний балл у лектора {lecturer_a.name} больше, чем у лектора {lecturer_b.name}')
print()


# Defining functions for mean values calculation
def mean_course_hw(students, course):
    """Takes a list of Student instances and string course title.
    Returns mean value of all grades for given course among all students.
    """
    grades_all = []
    for student in students:
        if course in student.courses_in_progress:
            grades_all += [sum(student.grades[course]) / len(student.grades[course])]
        else:
            continue

    return sum(grades_all) / len(grades_all)


def mean_course_lectures(lecturers, course):
    """Takes a list of Lecturer instances and string course title.
    Returns mean value of all lecture grades for given course among all lecturers.
    """
    grades_all = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            grades_all += [sum(lecturer.lecture_grades[course]) / len(lecturer.lecture_grades[course])]
        else:
            continue

    return sum(grades_all) / len(grades_all)


# Testing out functions for mean values calculation
mean_python = mean_course_hw([student_a, student_b], 'Python')
print(f'Средняя оценка за домашние задания по всем студентам в рамках курса "Python" = {mean_python}')

mean_python_lec = mean_course_lectures([lecturer_a, lecturer_b], 'Python')
print(f'Средняя оценка за лекции всех лекторов в рамках курса "Python" = {mean_python_lec}')
