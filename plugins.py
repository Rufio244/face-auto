from registry import registry

def email_api(data):
    return f"{data['name'].lower()}@gmail.com"


def identity_api(data):
    return {
        "name": data["name"],
        "status": "created"
    }

# auto register
registry.register("email_api", email_api)
registry.register("identity_api", identity_api)
