def scanzaclip(task):

    if "email" in task:
        return {"type": "email_api", "score": 0.9}

    if "identity" in task:
        return {"type": "identity_api", "score": 0.8}

    return {"type": "generic", "score": 0.5}
