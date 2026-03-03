import datetime

def capture_session():
    """
    Simulate capturing details from a Claw session or ClawMemory.
    In production, this would read from the actual session buffer or databases.
    """
    now = datetime.datetime.now()
    return {
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "date_str": now.strftime("%Y-%m-%d"),
        "date_full": now.strftime("%A, %B %d %Y"),
        "summary": "Discussed OpenClaw architectures, PKM integrations, and created ClawMirror MVP.",
        "topics": ["OpenClaw", "PKM", "Obsidian", "ClawMirror"],
        "logs": [
            {"speaker": "User", "text": "I want to create a Claw skill that syncs conversations to Obsidian."},
            {"speaker": "Claw", "text": "That's a great idea! I can help you build ClawMirror. Where should we start?"},
            {"speaker": "User", "text": "Let's map out the core flow first."}
        ],
        "highlights": [
            "New project idea validated: ClawMirror.",
            "Reminder: Create MVP video demo for X on Day 5."
        ],
        "tasks": [
            "Test Obsidian write permissions",
            "Write the generator logic for Logseq"
        ]
    }
