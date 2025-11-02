import json
from datetime import datetime

ARCHIVE = []  # attach memory db here, storing in runtime-memory just for demo purposes

def archivist_agent(defense: dict) -> dict:
    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "result": defense
    }

    ARCHIVE.append(record)

    # Text that will get displayed on the UI
    summary = {
        "archive_index": len(ARCHIVE) - 1,
        "timestamp": record["timestamp"],
        "defense_plan_preview": (defense.get("defense_plan") or "")[:500]
    }
    return {"archived": summary, "full_record": record}
