def get_valid_mark(subject_name):
    """Ask for a mark until the user enters a number between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter the mark for {subject_name}: "))

            if 0 <= mark <= 100:
                return mark

            print("Please enter a mark between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_grade(average):
    """Return a letter grade based on the average mark."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    print("=" * 40)
    print("Student Grade Calculator")
    print("=" * 40)

    subjects = {}

    while True:
        try:
            number_of_subjects = int(
                input("How many subjects do you want to enter? ")
            )

            if number_of_subjects > 0:
                break

            print("Please enter at least one subject.")

        except ValueError:
            print("Please enter a whole number.")

    for number in range(1, number_of_subjects + 1):
        subject_name = input(f"\nEnter the name of subject {number}: ").strip()

        if not subject_name:
            subject_name = f"Subject {number}"

        subjects[subject_name] = get_valid_mark(subject_name)

    marks = list(subjects.values())

    average = sum(marks) / len(marks)
    highest_subject = max(subjects, key=subjects.get)
    lowest_subject = min(subjects, key=subjects.get)
    final_grade = calculate_grade(average)

    # The student passes only when every subject has a mark of at least 40.
    result = "Pass" if all(mark >= 40 for mark in marks) else "Fail"

    print("\n" + "=" * 40)
    print("Grade Summary")
    print("=" * 40)

    for subject, mark in subjects.items():
        print(f"{subject}: {mark:.2f}")

    print(f"\nAverage mark: {average:.2f}")
    print(
        f"Highest mark: {highest_subject} "
        f"({subjects[highest_subject]:.2f})"
    )
    print(
        f"Lowest mark: {lowest_subject} "
        f"({subjects[lowest_subject]:.2f})"
    )
    print(f"Final grade: {final_grade}")
    print(f"Overall result: {result}")


if __name__ == "__main__":
    main()