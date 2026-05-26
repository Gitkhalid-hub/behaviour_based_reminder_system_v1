# 🧩 Breakdown Engine — Behavior-Based Reminder System

> **Technical Detective Lens:** This document dissects each module of the project, highlighting functionality, structure, edge cases, and design patterns.

---

## Module Links
- 🛠️ [PatternDetector — `core/pattern_detector.py`](core/pattern_detector.py)
- 🛠️ [ReminderEngine — `core/reminder_engine.py`](core/reminder_engine.py)
- 🛠️ [Notifier — `core/notifier.py`](core/notifier.py)
- 🛠️ [Usage History — `sample_data/usage_history.json`](sample_data/usage_history.json)
- 🛠️ [Orchestration — `main.py`](main.py)

> Clicking each link in PyCharm will open the respective file.

---

## 1️⃣ Surface Behavior

> What does the project output at a glance?

<details>
<summary>Behavior-Based Reminder System</summary>

```python
usage_history = behavior_reader.load_history(history_path)
behaviour_counts = pattern_detector.detect_patterns(usage_history)
reminder_needed, reminder_message = reminder_engine.generate_reminder(
    behaviour_counts,
    threshold
)
notifier.notify(reminder_message)
```

This system:

- Loads behavior history from JSON.
- Counts how often each tool appears.
- Compares tool usage count against a threshold.
- Generates a reminder if usage crosses the threshold.
- Displays a reminder message.
- Prints a final workflow summary.

</details>

---

## 2️⃣ Line-by-Line Behavior

> Inspect each line for concrete action.

<details>
<summary>PatternDetector — Counting Tool Usage</summary>

```python
behaviour_counts = {}

for event in usage_history:
    tool_name = event["tool_name"]

    if tool_name not in behaviour_counts:
        behaviour_counts[tool_name] = 0

    behaviour_counts[tool_name] += 1

return behaviour_counts
```

Line-by-line meaning:

- `behaviour_counts = {}`  
  Creates an empty dictionary to store tool usage frequency.

- `for event in usage_history:`  
  Loops through every usage event from the JSON file.

- `tool_name = event["tool_name"]`  
  Extracts the tool name from the current event.

- `if tool_name not in behaviour_counts:`  
  Checks whether this tool has already been counted.

- `behaviour_counts[tool_name] = 0`  
  Starts the count at zero for a new tool.

- `behaviour_counts[tool_name] += 1`  
  Adds one usage count for that tool.

- `return behaviour_counts`  
  Returns the final frequency dictionary.

</details>

---

## 3️⃣ Variable Purpose

> What each variable represents and how it interacts.

<details>
<summary>ReminderEngine — Decision Variables</summary>

```python
for tool_name, count in behaviour_counts.items():
    if count >= threshold:
        reminder_message = (
            f"{tool_name} has been used frequently. "
            f"Review or automate further."
        )

        return "Reminder needed!", reminder_message
```

Variable meanings:

- `behaviour_counts`  
  A dictionary containing how many times each tool was used.

- `tool_name`  
  The current tool being checked.

- `count`  
  The number of times that tool appears in the usage history.

- `threshold`  
  The minimum number of uses required before a reminder is triggered.

- `reminder_message`  
  The message created when the tool usage reaches or passes the threshold.

</details>

---

## 4️⃣ System Flow

> Stepwise progression of the program.

<details>
<summary>main.py — Orchestration Flow</summary>

```python
usage_history = behavior_reader.load_history(history_path)

behaviour_counts = pattern_detector.detect_patterns(usage_history)

reminder_needed, reminder_message = reminder_engine.generate_reminder(
    behaviour_counts,
    threshold
)

notifier.notify(reminder_message)
```

Workflow steps:

1. Load historical usage data.
2. Count occurrences per tool.
3. Compare counts against the threshold.
4. Generate reminder if threshold is reached.
5. Notify user with the reminder message.
6. Print final summary.

</details>

---

## 5️⃣ Edge Cases

> Handle unexpected inputs or failures.

<details>
<summary>BehaviorReader — Possible Failures</summary>

Possible edge cases:

- File does not exist → raises `Exception`.
- Empty JSON file → raises `Exception`.
- Invalid JSON format → may raise `JSONDecodeError`.
- Missing `tool_name` key in event dictionaries → may raise `KeyError`.
- Empty usage history list → reminder system returns safe no-reminder message.

</details>

---

## 6️⃣ Structural Pattern

> Patterns and design principles employed.

<details>
<summary>Accumulator Pattern — Dictionary Counting</summary>

```python
usage_count_by_tool = {}

for event in events:
    tool_name = event["tool_name"]

    if tool_name not in usage_count_by_tool:
        usage_count_by_tool[tool_name] = 0

    usage_count_by_tool[tool_name] += 1
```

Pattern explanation:

- Uses a dictionary as an accumulator for counting.
- Initializes a tool count the first time the tool appears.
- Increases the count every time the tool appears again.
- Maintains `O(n)` linear time complexity because each event is processed once.

</details>

---

## 7️⃣ Reframe / Visualize

> Conceptual visualization for quick understanding.

<details>
<summary>Usage History Table</summary>

| Tool Name | Usage Count | Reminder Result |
|---|---:|---|
| smart_file_organizer | 3 | Reminder needed |
| email_automation_engine | 1 | No reminder |
| usage_analytics_tracker | 2 | No reminder |

What this table helps reveal:

- Which tools are used most often.
- Which tools cross the reminder threshold.
- Which tools may need review or further automation.
- Which behaviors are safe and do not need reminders yet.

</details>

---

## 8️⃣ Project Data Shape

> What the system expects inside `usage_history.json`.

<details>
<summary>sample_data/usage_history.json</summary>

```json
[
  {
    "tool_name": "smart_file_organizer",
    "action": "run",
    "status": "success"
  },
  {
    "tool_name": "smart_file_organizer",
    "action": "run",
    "status": "success"
  },
  {
    "tool_name": "smart_file_organizer",
    "action": "run",
    "status": "success"
  },
  {
    "tool_name": "email_automation_engine",
    "action": "run",
    "status": "success"
  }
]
```

This file represents persistent behavior history.

The system expects:

- A list.
- Each item inside the list should be a dictionary.
- Each dictionary should contain a `tool_name`.
- Optional supporting fields include `action` and `status`.

</details>

---

## 9️⃣ Insights & Recommendations

> Critical observations for future upgrades.

- ✅ Track edge cases for each module.
- ✅ Annotate accumulators and dictionary structures.
- ✅ Keep `README.md` professional and use this file for deeper code dissection.
- ✅ Maintain collapsible modular structure in PyCharm for clarity.
- ✅ Use this file as the project’s detective/debugging companion.

### ⚡ 8-Step Truth-Finding Approach

Use this approach whenever extending features:

1. Surface Behavior
2. Line-by-Line Behavior
3. Variable Purpose
4. System Flow
5. Edge Cases
6. Structural Pattern
7. Reframe / Visualize
8. Insights & Recommendations

---

## 🧠 Final Detective Summary

This breakdown engine exists to help you avoid guessing while reading code.

The goal is to make every part of the project answerable:

- What does this module own?
- What does this variable represent?
- What does this loop change?
- What does this condition decide?
- What happens if the input is empty, missing, or unusual?
- What pattern is being used?
- How does this module connect to the system flow?

When those questions are clear, the code becomes easier to debug, extend, and explain.
<!-- content verified -->