from src.questionnaire import QUESTIONS

DIMENSIONS = [
    "urbanite",
    "intensite",
    "planification",
    "social",
    "confort",
    "decouverte"
]

ANSWER_VALUES = {
    "A": 1.0,
    "B": 0.33,
    "C": -0.33,
    "D": -1.0
}

def create_user_vector(responses):
    dimensions = {
        dimension: []
        for dimension in DIMENSIONS
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
        user_profile[dimension]
        for dimension in DIMENSIONS
    ]

    return user_vector