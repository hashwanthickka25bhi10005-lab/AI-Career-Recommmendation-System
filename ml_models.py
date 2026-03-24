def run_regression():
    print("\n--- Linear Regression (Salary Prediction using CSV Data) ---")

    programming = []
    salary = []

    # Read CSV file manually
    with open("data/students.csv", "r") as file:
        lines = file.readlines()[1:]  # Skip header

        for line in lines:
            parts = line.strip().split(",")
            programming.append(int(parts[2]))  # Programming column
            salary.append(int(parts[7]))       # Salary column

    n = len(programming)

    sum_x = sum(programming)
    sum_y = sum(salary)
    sum_xy = sum(x*y for x, y in zip(programming, salary))
    sum_x2 = sum(x*x for x in programming)

    m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    b = (sum_y - m*sum_x) / n

    test_skill = 85
    predicted_salary = m * test_skill + b

    print("Predicted Salary for programming skill 85:", int(predicted_salary)
