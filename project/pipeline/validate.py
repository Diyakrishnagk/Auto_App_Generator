def cross_validate(data):
    errors = []

    # DB vs API
    for table in data["database"]:
        if f"GET /{table}" not in data["api"]:
            errors.append(f"Missing API for {table}")

    # UI vs API
    if "Students" in data["ui"]:
        if "GET /students" not in data["api"]:
            errors.append("UI-API mismatch")

    return errors