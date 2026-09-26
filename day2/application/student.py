class Student:
    """Represent a student."""

    def __init__(
        self,
        name,
        age,
        python,
        mathematics,
        communication,
    ):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication

    def calculate_percentage(self):
        """Calculate the student's percentage."""
        total = self.python + self.mathematics + self.communication

        return total / 3

    def display(self):
        """Display the student's details."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Python:", self.python)
        print("Mathematics:", self.mathematics)
        print("Communication:", self.communication)
        print("Percentage:", self.calculate_percentage())

if __name__ == "__main__":
            obj_1 = Student("rohith",19,34,56,78)
            obj_2 = Student("shymanth",20,65,45,34)
            obj_3 = Student("shreyas",19,67,65,30)
            obj_4 = Student("roh",19,34,56,78)
            obj_5 = Student("shy",20,65,45,34)
            obj_6 = Student("shre",19,67,65,30)
            obj_1.display()
            obj_2.display()
            obj_3.display()
            obj_4.display()
            obj_5.display()
            obj_6.display()