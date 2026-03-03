import os

def generate_markdown(session_data, pkm_type):
    """
    Generate markdown content based on PKM template and captured session data.
    """
    template_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', f'{pkm_type}.md')
    
    # If no template file exists, use default hardcoded ones for MVP
    if not os.path.exists(template_path):
        if pkm_type == 'obsidian':
            return _generate_obsidian(session_data)
        elif pkm_type == 'logseq':
            return _generate_logseq(session_data)
        else:
            raise ValueError(f"Unknown PKM type: {pkm_type}")

    # For production: read from template_path and replace placeholders
    pass

def _generate_obsidian(s):
    topics = ", ".join(s['topics'])
    logs_str = "\n\n".join([f"**{l['speaker']}**: {l['text']}" for l in s['logs']])
    highlights_str = "\n".join([f"- {h}" for h in s['highlights']])
    tasks_str = "\n".join([f"- [ ] {t}" for t in s['tasks']])

    return f"""---
date: {s['date_str']}
tags: [daily, claw-conversation]
---
# {s['date_full']}

## 🤖 Claw Conversation Summary
- **Session time**: {s['timestamp']}
- **Main topics**: {topics}

### Summary
{s['summary']}

## 📝 Full Log
{logs_str}

## ✨ Highlights
{highlights_str}

## ✅ Tasks / Reminders
{tasks_str}

---
"""

def _generate_logseq(s):
    topics = ", ".join(s['topics'])
    
    logs_str = "\n".join([f"      - **{l['speaker']}**: {l['text']}" for l in s['logs']])
    highlights_str = "\n".join([f"      - {h}" for h in s['highlights']])
    tasks_str = "\n".join([f"      - TODO {t}" for t in s['tasks']])
    
    return f"""
  - ### 🤖 Claw Conversation [{s['timestamp']}]
    - **Summary**: {s['summary']}
    - **Topics**: {topics}
    - **Full Log**:
{logs_str}
    - **Highlights**:
{highlights_str}
    - **Tasks**:
{tasks_str}
"""
