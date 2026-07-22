print("welcome")

import os

# Root folder
root = "python-learning"

# Subfolders (2nd highest level categories)
folders = [
    "01_basics/intro",
    "01_basics/syntax",
    "01_basics/output",
    "01_basics/variables",
    "01_basics/datatypes",
    "01_basics/operators",
    "01_basics/control_flow",

    "02_functions",
    "03_oop",
    "04_file_handling",
    "05_libraries/numpy",
    "05_libraries/pandas",
    "05_libraries/scipy",
    "05_libraries/matplotlib",
    "05_libraries/django",

    "06_machine_learning/regression",
    "06_machine_learning/classification",
    "06_machine_learning/clustering",
    "06_machine_learning/evaluation",

    "07_dsa/lists_arrays",
    "07_dsa/stacks_queues",
    "07_dsa/linked_lists",
    "07_dsa/trees",
    "07_dsa/graphs",
    "07_dsa/sorting_searching",

    "08_databases/mysql",
    "08_databases/mongodb",

    "09_misc",
    "10_examples/exercises",
    "10_examples/quizzes",
    "10_examples/challenges",
    "10_examples/practice_problems",

    "notes"
]

# Create folders
for folder in folders:
    path = os.path.join(root, folder)
    os.makedirs(path, exist_ok=True)

print("✅ Folder structure created successfully!")
