from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self._name = name  

    @abstractmethod
    def display_details(self):
        pass


class Course:
    def __init__(self, course_name):
        self.__course_name = course_name 

    def get_course_name(self):
        return self.__course_name


class Student(Person):
    def __init__(self, student_id, name, marks, course_name):
        super().__init__(name)  
        self.__student_id = student_id   
        self.__marks = marks            
        self.__course = Course(course_name)  

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    def calculate_grade(self):
        if self.__marks >= 70:
            return "A"
        elif self.__marks >= 60:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "Fail"

    def display_details(self):
        print("\nThe Student Details are:")
        print("Student ID:", self.__student_id)
        print("Name:", self._name)
        print("Course:", self.__course.get_course_name())
        print("Marks:", self.__marks)
        print("Grade:", self.calculate_grade())


def main():
    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    course_name = input("Enter Course Name: ")
    marks = int(input("Enter Marks: "))

    student1 = Student(student_id, name, marks, course_name)

    student1.display_details()


if __name__ == "__main__":
    main()
