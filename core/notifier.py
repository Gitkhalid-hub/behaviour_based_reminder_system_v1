# THE NOTIFICATION STAGE.

class Notifier:
	
	def notify(self, message):
		
		if message == "":
			raise Exception(f"Message cannot be empty!")
		
		print(message)
		return message