grade_book = {
    "Alice": 85,
    "Bob": 92,
    "Jake": 78,
    "John": 95,
    "Ayan": 88
}

print("======Student Grade Book========")
print("Current Students and scores:", grade_book)

total_score = 0
for name in grade_book:
    total_score += grade_book[name]

class_average = total_score / len(grade_book)
print(f"\nClass Average: {class_average:.2f}")

top_student = max(grade_book, key=grade_book.get)
highest_score = grade_book[top_student]

bottom_student = min(grade_book, key=grade_book.get)
lowest_score = grade_book[bottom_student]

print(f"Top Scorer: {top_student} ({highest_score})")
print(f"Bottom Scorer: {bottom_student} ({lowest_score})")
print("\n======== Student Search ===========")
search_name = input("Enter the student name to look up :")
score = grade_book.get(search_name)

if score is not None:
    print(f"Found! {search_name}'s score is {score}.")
else:
    print(f"Sorry, '{search_name}'s is not in the grade book.")