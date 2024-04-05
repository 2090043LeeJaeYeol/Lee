class Student:
    def __init__(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math

    def average(self):
        return (self.korean + self.english + self.math) / 3


def main():
    num_students = int(input("학생 수를 입력하세요: "))
    students = []

    for i in range(num_students):
        korean = float(input(f"{i + 1}번째 학생의 국어 점수를 입력하세요: "))
        english = float(input(f"{i + 1}번째 학생의 영어 점수를 입력하세요: "))
        math = float(input(f"{i + 1}번째 학생의 수학 점수를 입력하세요: "))

        student = Student(korean, english, math)
        students.append(student)

        average = student.average()
        print(f"{i + 1}번째 학생의 평균 점수: {average}")


if __name__ == "__main__":
    main()