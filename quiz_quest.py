import random

# Function to open a specific category
def open_category(questions, category):
    """
    Opens a specific category and returns its questions.
    """
    if category in questions:
        return questions[category]
    else:
        raise ValueError(f"Category '{category}' does not exist.")


# Function to get a random question
def get_random_question(questions, category=None):
    """
    Returns a random question from the specified category 
    or from all categories if none is specified.
    """
    if category:
        if category in questions:
            selected = random.choice(questions[category])
        else:
            raise ValueError(f"Category '{category}' does not exist.")
    else:
        all_questions = [q for cat in questions.values() for q in cat]
        selected = random.choice(all_questions)
    return selected['q'], selected['o'], selected['a']