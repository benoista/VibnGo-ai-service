from src.questionnaire import QUESTIONS

ANSWER_VALUES = {
    "A": 1.0,
    "B": 0.33,
    "C": -0.33,
    "D": -1.0
}

def create_user_vector(responses):
    dimensions = {
        "urbanite": [],
        "intensite": [],
        "planification": [],
        "social": [],
        "confort": [],
        "decouverte": []
    }

    for question in QUESTIONS:
        question_id = question["id"]
        dimension = question["dimension"]

        answer = responses.get(question_id)

        if answer not in ANSWER_VALUES:
            raise ValueError(
                f"Réponse invalide ou manquante pour la question {question_id}"
            )

        value = ANSWER_VALUES[answer]

        dimensions[dimension].append(value)

    user_profile = {}

    for dimension, values in dimensions.items():
        user_profile[dimension] = sum(values) / len(values)

    user_vector = [
        user_profile["urbanite"],
        user_profile["intensite"],
        user_profile["planification"],
        user_profile["social"],
        user_profile["confort"],
        user_profile["decouverte"]
    ]

    return user_vector