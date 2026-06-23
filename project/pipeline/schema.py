def generate_schema(design):
    return {
        "ui": {
            "Login": {},
            "Dashboard": {},
            "Students": {}
        },
        "api": {
            "POST /login": {}
        },
        "database": ["students"],
        "roles": ["admin", "user"]
    }