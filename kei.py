import re
import tkinter as tk

patterns = [
    (r'hi|hello|hey there', ['Hello!', 'Hi!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am great, thanks for asking!']),
    (r'who are you?', ['My name is Kei the chatbot!', 'I am Kei the chatbot.']),
    (r'what can you do?', ['I can do a lot! I specialize in answering math problems though! :)']),
    (r'(\d+) \+ (\d+)', lambda x, y: str(int(x) + int(y))),
    (r'(\d+) \- (\d+)', lambda x, y: str(int(x) - int(y))),
    (r'(\d+) \* (\d+)', lambda x, y: str(int(x) * int(y))),
    (r'(\d+) \/ (\d+)', lambda x, y: str(int(x) / int(y))),
]

def send_message():
    user_input = entry.get()
    response = None
    for pattern, responses in patterns:
        match = re.match(pattern, user_input.lower())
        if match:
            if callable(responses):
                response = responses(*match.groups())
            else:
                response = responses[0]
            break
    if response:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_input + "\n", "user")
        chat_log.insert(tk.END, "Kei: " + response + "\n", "kei")
        chat_log.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Kei the Chatbot")

chat_log = tk.Text(root, width=50, height=20, state=tk.DISABLED)
chat_log.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, width=50)
entry.grid(row=1, column=0, padx=10, pady=10)
entry.bind("<Return>", lambda event: send_message())

style = tk.ttk.Style()
style.configure("user.TLabel", foreground="blue")
style.configure("kei.TLabel", foreground="green")
chat_log.tag_configure("user", justify="right", font=("Arial", 10), foreground="blue")
chat_log.tag_configure("kei", justify="left", font=("Arial", 10), foreground="green")

root.mainloop()

# Test the chatbot
print("╔════════════════════════════════════════╗")
print("║      Welcome to Kei the Chatbot!       ║")
print("║      Type 'quit' to exit.               ║")
print("╚════════════════════════════════════════╝")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("╔════════════════════════════════════════╗")
        print("║               Goodbye!                  ║")
        print("╚════════════════════════════════════════╝")
        break
    else:
        response = None
        for pattern, responses in patterns:
            match = re.match(pattern, user_input.lower())
            if match:
                if callable(responses):
                    response = responses(*match.groups())
                else:
                    response = responses[0]  # Select the first response
                break
        if response:
            print("╔════════════════════════════════════════╗")
            print("║              Kei:", response)
            print("╚════════════════════════════════════════════════════╝")
        else:
            print("╔════════════════════════════════════════╗")
            print("║    Kei: I'm sorry, I didn't understand that.   ║")
            print("╚════════════════════════════════════════╝")
