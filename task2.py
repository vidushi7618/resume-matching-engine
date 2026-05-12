import math

resumes = {
    "Arjun Sharma": ["python", "machine_learning", "sql", "pandas", "numpy", "deep_learning"],

    "Priya Nair": ["javascript", "react", "nodejs", "mongodb", "rest_api", "html_css"],

    "Rahul Gupta": ["java", "spring_boot", "mysql", "microservices", "docker", "kubernetes"],

    "Sneha Patel": ["python", "tensorflow", "keras", "nlp", "bert", "data_visualization"],

    "Vikram Singh": ["cpp", "algorithms", "data_structures", "competitive_programming", "python"],

    "Ananya Krishnan": ["javascript", "vue", "python", "flask", "postgresql", "aws", "ci_cd"],

    "Karan Mehta": ["python", "machine_learning", "xgboost", "feature_engineering", "sql", "data_visualization"],

    "Deepika Rao": ["java", "android", "kotlin", "firebase", "rest_api", "ui_ux", "figma"],

    "Aditya Kumar": ["react", "typescript", "graphql", "redux", "tailwind", "nodejs", "jest"],

    "Meera Iyer": ["python", "r", "statistics", "machine_learning", "regression", "clustering", "data_visualization"]
}

# Vocabulary Construction

vocabulary = set()

for skills in resumes.values():
    vocabulary.update(skills)

vocabulary = sorted(list(vocabulary))

print("Vocabulary:")
print(vocabulary)

# Document Frequency

df = {}

for skill in vocabulary:

    count = 0

    for skills in resumes.values():

        if skill in skills:
            count += 1

    df[skill] = count

print("\nDocument Frequency:")
print(df)

# IDF Calculation

idf = {}

N = 10

for skill in vocabulary:
    idf[skill] = math.log(N / df[skill])

print("\nIDF Values:")
print(idf)
