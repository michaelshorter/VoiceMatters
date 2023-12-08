import tkinter as tk
import time


def count_words():
    # Read the contents of the file
    with open("/home/wordcloud/WordCloud/AzureSpeechCC/content.txt", "r") as file:
        contents = file.read()

    # Count the number of words
    word_count = len(contents.split())

    # Update the label text
    count_label.config(text="WORD COUNT:\n{}".format(word_count))

    # Schedule the next update after 3 seconds
    root.after(3000, count_words)


# Create the Tkinter window
root = tk.Tk()
root.title("Word Count")

# Set the initial window dimensions
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Configure the background color
root.configure(bg='#F8C9D3')

# Create a label to display the word count
count_label = tk.Label(root, fg="#E73E55", font=('The Led Display St', 80), background="#F8C9D3")
count_label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

# Configure the grid to expand vertically
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start counting words
count_words()

# Start the Tkinter event loop
root.mainloop()
