# THE PATTERN DETECTION STAGE.


class PatternDetector:

    def detect_patterns(self, usage_history):

        behaviour_counts = {}

        for event in usage_history:

            tool_name = event["tool_name"]

            if tool_name not in behaviour_counts:
                behaviour_counts[tool_name] = 0

            behaviour_counts[tool_name] += 1

        return behaviour_counts