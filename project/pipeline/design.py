def create_design(intent):
    return {
        "modules": intent["features"] + intent["entities"],
        "flows": ["login → dashboard"]
    }