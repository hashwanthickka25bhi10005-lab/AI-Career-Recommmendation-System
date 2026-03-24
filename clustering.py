def run_clustering():
    print("\n--- Student Clustering using CSV Data ---")

    high = []
    medium = []
    low = []

    with open("data/students.csv", "r") as file:
        lines = file.readlines()[1:]

        for line in lines:
            parts = line.strip().split(",")
            name = parts[0]
            programming = int(parts[2])

            if programming > 85:
                high.append(name)
            elif programming > 65:
                medium.append(name)
            else:
                low.append(name)

    print("High Skill Students:", high)
    print("Medium Skill Students:", medium)
    print("Low Skill Students:", low)
