import math
from src.traveler_profiles import TRAVELER_PROFILES


def cosine_similarity(vector_a, vector_b):

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    norm_a = math.sqrt(sum(a ** 2 for a in vector_a))
    norm_b = math.sqrt(sum(b ** 2 for b in vector_b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)


def find_traveler_profile(user_vector):

    best_profile = None
    best_similarity = -1

    for profile_name, profile_data in TRAVELER_PROFILES.items():

        profile_vector = profile_data["vector"]

        similarity = cosine_similarity(
            user_vector,
            profile_vector
        )

        if similarity > best_similarity:
            best_similarity = similarity
            best_profile = {
                "name": profile_name,
                "description": profile_data["description"],
                "similarity": round(similarity, 3)
            }

    return best_profile