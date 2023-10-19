import os
import interpreter
import json

interpreter.auto_run = True

interpreter.system_message += """
Utilize Python for operations and commands. Ensure independent task completion, delivering concise responses. This directive encapsulates core actions of analysis and examination, imperative instruction through a direct voice, elimination of redundant phrases for clarity, specification of tools and flags for precise operation, and structured formatting for enhanced readability and comprehension.
"""


# class MessageHandler:
#     def __init__(self, file_path="./logs/messages.json"):
#         self.file_path = file_path
#         self.messages = self.load_messages()

#     def load_messages(self):
#         try:
#             with open(self.file_path, "r") as file:
#                 messages = json.load(file)
#             return messages
#         except Exception as e:
#             print(f"Error loading messages: {e}")
#             return []

#     def save_messages(self, new_messages):
#         try:
#             with open(self.file_path, "w") as file:
#                 json.dump(new_messages, file)
#         except Exception as e:
#             print(f"Error saving messages: {e}")


# message_handler = MessageHandler()

interpreter.chat()
