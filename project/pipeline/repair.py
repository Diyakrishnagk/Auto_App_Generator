def repair(data, errors):
    for err in errors:
        if "Missing API" in err:
            table = err.split()[-1]
            data["api"][f"GET /{table}"] = {"response": f"list of {table}"}

    return data