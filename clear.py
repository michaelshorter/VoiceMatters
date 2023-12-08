import os

file_path = "/home/wordcloud/WordCloud/AzureSpeechCC/content.txt"

try:
    # Open the file in write mode, which truncates the file
    with open(file_path, 'w') as file:
        # File is now empty
        print(f"Contents of {file_path} deleted successfully.")
except Exception as e:
    print(f"Error: {e}")

# Script completes here
