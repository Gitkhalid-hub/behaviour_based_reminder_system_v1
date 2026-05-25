# THE ORCHESTRATION STAGE.

from pathlib import Path

from core.behavior_reader import BehaviorReader
from core.pattern_detector import PatternDetector
from core.reminder_engine import ReminderEngine
from core.notifier import Notifier

history_path = Path("sample_data/usage_history.json")
threshold = 3

behavior_reader = BehaviorReader()
pattern_detector = PatternDetector()
reminder_engine = ReminderEngine()
notifier = Notifier()

try:
	usage_history = behavior_reader.load_history(history_path)
	
	behaviour_counts = pattern_detector.detect_patterns(usage_history)
	
	reminder_needed, reminder_message = reminder_engine.generate_reminder(
		behaviour_counts,
		threshold
	)
	
	notifier.notify(reminder_message)
	
	print("\n=== BEHAVIOR REMINDER SUMMARY ===")
	print("Behavior Counts:", behaviour_counts)
	print("Threshold:", threshold)
	print("Reminder Status:", reminder_needed)
	print("COMPLETED SUCCESSFULLY!")
	
except Exception as err:
	print("FAILED!")
	print(err)