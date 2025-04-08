from datetime import datetime

def write_aetherion_log(message):
    with open("docs/naplok/aetherion_auto_log.md", "a", encoding="utf-8") as f:
        f.write(f"## {datetime.now().isoformat()}
")
        f.write(f"{message}\n\n")
