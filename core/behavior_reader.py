# THE LOADING STAGE
import json

class BehaviorReader:
	
	def load_history(self, history_path):
		
		if not history_path.exists():
			raise Exception(f"File path cannot be empty!")
		
		if history_path.stat().st_size == 0:
			raise Exception(f"Path cannot be emtpy!")
		
		with open(history_path, "r") as file:
			usage_history = json.load(file)
			
		return usage_history
		