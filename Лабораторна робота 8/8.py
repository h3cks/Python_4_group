class StudentRecords:
    def __init__(self):
        self.records = {}

    def add_student(self, group_number, full_name, course, subjects_grades):
        if group_number not in self.records:
            self.records[group_number] = []
        self.records[group_number].append({
            'full_name': full_name,
            'course': course,
            'subjects_grades': subjects_grades
        })

    def display_records(self):
        for group_number, students in self.records.items():
            print(f"Номер групи: {group_number}")
            for student in students:
                print(f"ПІП: {student['full_name']}")
                print(f"Курс: {student['course']}")
                print("Предмети та оцінки за семестр:")
                for subject, grade in student['subjects_grades'].items():
                    print(f"\t{subject}: {grade}")
                print()

# Приклад використання
student_records = StudentRecords()

# Додавання даних
student_records.add_student(101, 'Іванов Іван Іванович', 2, {'Математика': 95, 'Фізика': 85})
student_records.add_student(102, 'Петров Петро Петрович', 3, {'Хімія': 90, 'Біологія': 88})

# Виведення записів
student_records.display_records()
