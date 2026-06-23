metrics = {
    "total_requests": 0,
    "success": 0,
    "failures": 0,
    "repairs": 0
}

def update(success, repaired):
    metrics["total_requests"] += 1

    if success:
        metrics["success"] += 1
    else:
        metrics["failures"] += 1

    if repaired:
        metrics["repairs"] += 1

    return metrics