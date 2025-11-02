import json
from datetime import datetime

ARCHIVE = []  # attach memory db here, storing in runtime-memory just for demo purposes

def archivist_agent(state: dict) -> dict:
    target = state.get("target", "target.example.com")
    logs = state.get("logs", [])

    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "target": target,
        "logs": list(logs)
    }
    ARCHIVE.append(record)

    logs.append(f"[Archivist] Archived record index={len(ARCHIVE) - 1} at {record['timestamp']}")

    return {"target": target, "logs": logs}