# JOB DESCRIPTIONS

jds = {
    "JD-1": [
        "python",
        "machine_learning",
        "deep_learning",
        "tensorflow",
        "pytorch",
        "sql",
        "data_visualization",
        "nlp",
        "bert",
        "feature_engineering",
        "statistics"
    ],

    "JD-2": [
        "java",
        "spring_boot",
        "mysql",
        "postgresql",
        "microservices",
        "docker",
        "kubernetes",
        "rest_api",
        "ci_cd",
        "redis"
    ],

    "JD-3": [
        "javascript",
        "react",
        "vue",
        "typescript",
        "rest_api",
        "html_css",
        "nodejs",
        "graphql",
        "redux",
        "jest",
        "aws"
    ]
}

# TF-IDF VECTORS

resume_vectors = {}

for name, skills in resumes.items():

    vector = []

    total_skills = len(skills)

    for skill in vocabulary:

        if skill in skills:

            tf = 1 / total_skills

            vector.append(tf * idf[skill])

        else:
            vector.append(0)

    resume_vectors[name] = vector

# JD BINARY VECTORS

jd_vectors = {}

for jd_name, jd_skills in jds.items():

    vector = []

    for skill in vocabulary:

        if skill in jd_skills:
            vector.append(1)
        else:
            vector.append(0)

    jd_vectors[jd_name] = vector

# COSINE SIMILARITY

def cosine_similarity(a, b):

    dot_product = 0

    for x, y in zip(a, b):
        dot_product += x * y

    magnitude_a = math.sqrt(sum(x * x for x in a))
    magnitude_b = math.sqrt(sum(y * y for y in b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0

    return dot_product / (magnitude_a * magnitude_b)

# FINAL RANKINGS

for jd_name, jd_vector in jd_vectors.items():

    scores = []

    for candidate, resume_vector in resume_vectors.items():

        similarity = cosine_similarity(resume_vector, jd_vector)

        scores.append((candidate, round(similarity, 2)))

    scores.sort(key=lambda x: (-x[1], x[0]))

    print("\n" + jd_name + " Results:")

    for candidate, score in scores[:3]:

        print(candidate, score)
