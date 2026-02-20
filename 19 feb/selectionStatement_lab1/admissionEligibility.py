
percentage = float(input("Enter 12th grade percentage: "))
studied_math = input("Did the student study Mathematics? (yes/no): ").strip().lower()
entrance_score = float(input("Enter entrance exam score: "))


eligible = True


if percentage < 75:
    print("Not eligible: Minimum 75% in 12th grade required.")
    eligible = False

if studied_math != "yes":
    print("Not eligible: Must have studied Mathematics.")
    eligible = False

if entrance_score < 80:
    print("Not eligible: Entrance exam score must be at least 80.")
    eligible = False


if eligible:
    print("Student is eligible for admission.")
