import random
import string

user_ids = list(range(1,101))
receipients_ids = list(range(1,101))

def genertate_messages() -> dict:
    random_user_id = random.choice(user_ids)

    #Copy the receipients array
    receipients_ids_copy = receipients_ids.copy()

    # User can't send message to himself
    receipients_ids_copy.remove(random_user_id)
    random_receipients_id = random.choice(receipients_ids_copy)

    #Generate a random message
    message = "".join(random.choice(string.ascii_letters) for i in range(32))

    return {
        "user_id": random_user_id,
        "receipients_id": random_receipients_id,
        "message": message
    }


