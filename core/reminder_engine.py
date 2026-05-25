# THE DECISION STAGE.


class ReminderEngine:

    def generate_reminder(self, behaviour_counts, threshold):

        if behaviour_counts == {}:
            return "No reminder", "No behaviour data found."

        for tool_name, count in behaviour_counts.items():

            if count >= threshold:

                reminder_message = (
                    f"{tool_name} has been used frequently. "
                    f"Review or automate further."
                )

                return "Reminder needed!", reminder_message

        return "No reminder needed", "System behaviour is safe."