def display_question(question, choices):
    print(question)
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")
    user_choice = input("Enter the number of your choice: ")
    return int(user_choice)

def check_answer(question_number, user_answer, answers):
    correct_answer = answers[question_number - 1]
    return user_answer == correct_answer

questions = {
    "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
    "Which planet is known as the Red Planet?": ["Mars", "Venus", "Jupiter", "Saturn"],
    "What is the largest mammal on Earth?": ["Blue Whale", "African Elephant", "Giraffe", "Hippopotamus"],
}

answers = [1, 1, 1]  # Specify the correct choice for each question (1-indexed)

score = 0
for i, (question, choices) in enumerate(questions.items(), start=1):
    user_answer = display_question(f"Question {i}: {question}", choices)
    if check_answer(i, user_answer, answers):
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect.\n")

print(f"You got {score} out of {len(questions)} questions correct.")
