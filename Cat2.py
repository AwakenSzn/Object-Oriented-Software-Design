from abc import ABC, abstractmethod

# Abstract class demonstrating Abstraction
class Person(ABC):
    def __init__(self, name):
        self._name = name  # Protected attribute

    @abstractmethod
    def display_details(self):
        pass

# Student class demonstrating Inheritance, Encapsulation, Polymorphism
class Student(Person):
    def __init__(self, student_id, name, course, marks):
        super().__init__(name)
        self.__student_id = student_id  # Private attribute
        self.__course = course          # Private attribute
        self.__marks = marks            # Private attribute

    # Encapsulation: Getters and Setters
    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    # Method to calculate grade
    def get_grade(self):
        if self.__marks >= 70:
            return "A"
        elif self.__marks >= 60:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "Fail"

    # Polymorphism: Overriding abstract method
    def display_details(self):
        print("------ Student Details ------")
        print(f"ID: {self.__student_id}")
        print(f"Name: {self._name}")
        print(f"Course: {self.__course}")
        print(f"Marks: {self.__marks}")
        print(f"Grade: {self.get_grade()}")
        print("----------------------------")

# Main Application
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_details()

# Driver code
def main():
    sms = StudentManagementSystem()
    n = int(input("Enter number of students to add: "))

    for i in range(n):
        print(f"\nEnter details for student {i + 1}:")
        student_id = int(input("ID: "))
        name = input("Name: ")
        course = input("Course: ")
        marks = int(input("Marks: "))

        student = Student(student_id, name, course, marks)
        sms.add_student(student)

    print("\nDisplaying all student details:\n")
    sms.display_all_students()

if __name__ == "__main__":
    main()
