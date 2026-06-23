def simulate(config):
    return {
        "status": "success",
        "pages_generated": list(config["ui"].keys()),
        "apis_ready": list(config["api"].keys())
    }