# ClawMirror

ClawMirror is a skill that mirrors (auto-syncs) your conversations with Claw directly into popular PKM tools like Obsidian, Logseq, or Anytype without manual copy-pasting.

## Core Flow

1. **Trigger**: Manual via `/mirror`, end-of-session, or cron schedule.
2. **Capture**: Grabs the most recent context from Claw (summary, highlights, logs).
3. **Generate**: Formats data into clean Markdown using templates.
4. **Sync**: Securely appends to or creates your Daily Notes locally.

## Development

Run the MVP pipeline:

```bash
python src/main.py
```
