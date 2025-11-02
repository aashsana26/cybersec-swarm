import json
from datetime import datetime

ARCHIVE = []  # runtime memory DB (demo only)

def archivist_agent(state: dict) -> dict:
    target = state.get("target", "target.example.com")
    logs = state.get("logs", [])

    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "target": target,
        "logs": list(logs)
    }
    ARCHIVE.append(record)

    # Create readable summary
    summary = {
        "archive_index": len(ARCHIVE) - 1,
        "timestamp": record["timestamp"],
        "log_count": len(logs)
    }

    logs.append(f"[Archivist] Archived record index={summary['archive_index']} at {summary['timestamp']}")

    return {
        "target": target,
        "logs": logs,
    }
