
import json
from datetime import datetime, timezone
from pathlib import Path

LOG_FILE = Path(__file__).parent / "results" / "request_log.jsonl"


def log_request(outcome, duration_seconds, error=None):
    """Append one request record to a JSON Lines log."""
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "question": outcome.get("question"),
        "answer": outcome.get("answer"),
        "sources": outcome.get("sources", []),
        "refused": outcome.get("refused"),
        "best_distance": outcome.get("best_distance"),
        "duration_seconds": round(duration_seconds, 3),
        "error": str(error) if error else None,
    }

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")
