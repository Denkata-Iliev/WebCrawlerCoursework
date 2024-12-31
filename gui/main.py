import tkinter as tk
import utils
import threading
import socketio  # type: ignore
import requests  # type: ignore

class DynamicInputApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic Input UI")
        self.inputs = []  # Keep track of input widgets
        self.setup_ui()

    def setup_ui(self):
        # Create the first input row
        self.add_input()

        # Add the submit button at the bottom
        self.submit_button = tk.Button(self.root, text="Submit", command=self.on_submit)
        self.submit_button.pack(side=tk.BOTTOM, pady=10)

    def add_input(self):
        # Create a frame for the input and buttons
        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        # Add an entry widget
        entry = tk.Entry(frame, width=30)
        entry.pack(side=tk.LEFT, padx=5)
        self.inputs.append(frame)

        # Add the plus button
        plus_button = tk.Button(frame, text="+", command=self.add_input)
        plus_button.pack(side=tk.LEFT, padx=5)

        # Add the minus button if there are multiple inputs
        if len(self.inputs) > 1:
            minus_button = tk.Button(frame, text="-", command=lambda: self.remove_input(frame))
            minus_button.pack(side=tk.LEFT, padx=5)

        # Remove the minus button from the previous input row
        if len(self.inputs) > 1:
            for widget in self.inputs[-2].winfo_children():
                if widget.cget("text") == "-":
                    widget.pack_forget()
                if widget.cget("text") == "+":
                    widget.pack_forget()

    def remove_input(self, frame):
        # Remove the frame and its widgets
        self.inputs.remove(frame)
        frame.destroy()

        # Re-add the minus button to the last input if there are multiple inputs
        last_frame = self.inputs[-1]
        if len(self.inputs) > 1:
            for widget in last_frame.winfo_children():
                if widget.cget("text") == "+":
                    minus_button = tk.Button(last_frame, text="-", command=lambda: self.remove_input(last_frame))
                    minus_button.pack(side=tk.RIGHT, padx=5)
                if widget.cget("text") == "+":
                    plus_button = tk.Button(last_frame, text="+", command=lambda: self.add_input())
                    plus_button.pack(side=tk.LEFT, padx=5)
        else:
            plus_button = tk.Button(last_frame, text="+", command=lambda: self.add_input())
            plus_button.pack(side=tk.LEFT, padx=5)

    def on_submit(self):
        urls = []
        for frame in self.inputs:
            entry = frame.winfo_children()[0]  # Get the Entry widget (first child)
            url = entry.get()  # Get the text from the Entry widget
            if url.strip():  # Only add non-empty inputs
                urls.append(url)

        # Passing the list to the scraper container through this endpoint
        try:
            response = requests.post("http://scraper-app:5000/submit-urls", json={"urls": urls})
            if response.status_code == 200:
                print("Successfully sent URLs to the scraper container.")
            else:
                print(f"Error: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Failed to send URLs: {e}")

    def show_content(self, records):
    # Create a new window
        new_window = tk.Toplevel(root)
        new_window.title("Content Display")
        new_window.geometry("600x400")

        # Display the data in the new window
        text_widget = tk.Text(new_window, wrap="word", font=("Arial", 12))
        text_widget.pack(expand=True, fill="both", padx=10, pady=10)

        # Format and insert data into the text widget
        for item in records:
            text_widget.insert(
                "end",
                f"{item.url}: {item.content[:21]}...\n"
                f"compound: {item.compound}, negative: {item.negative}, neutral: {item.neutral}, positive: {item.positive}\n\n"
            )

        # Disable the text widget to make it read-only
        text_widget.config(state="disabled")


# Create a SocketIO client
sio = socketio.Client()

# Define event handlers
@sio.on('connect')
def on_connect():
    print("Connected to server!")

@sio.on('message')
def on_message(data):
    print("Message from server:", data)

    records = utils.get_analized_from_last_mins(2)

    root.after(0, app.show_content, records)
    

def socketio():
    # Connect to the server
    sio.connect('http://analizer-app:5001')

    # Keep the client running to listen for events
    sio.wait()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = DynamicInputApp(root)

    socketio_thread = threading.Thread(target=socketio, daemon=True)
    socketio_thread.start()

    root.mainloop()
