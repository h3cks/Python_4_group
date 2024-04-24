def write_question(file_path, surname, question):
    try:
        with open(file_path, 'a') as file:
            file.write(f"Surname: {surname}\n")
            file.write(f"Question: {question}\n\n")
        print("Питання успішно записано у файл.")
    except Exception as e:
        print(f"Виникла помилка при записі у файл: {e}")

def write_answer(file_path, surname, answer, next_question):
    try:
        with open(file_path, 'a') as file:
            file.write(f"Surname: {surname}\n")
            file.write(f"Answer: {answer}\n")
            file.write(f"Next Question: {next_question}\n\n")
        print("Відповідь успішно записана у файл.")
    except Exception as e:
        print(f"Виникла помилка при записі у файл: {e}")

# Шлях до файлу
file_path = "questions_and_answers.txt"

# Перший студент записує питання
write_question(file_path, "Іванов", "Як створити список у Python?")

# Другий студент записує відповідь та питання для наступного
write_answer(file_path, "Петров", "Для створення списку у Python використовується квадратні дужки [], наприклад: my_list = [1, 2, 3].", "Як видалити елемент зі списку у Python?")

# Посилання на файл для завантаження
print("Файл з питаннями та відповідями доступний за посиланням: <посилання>")
