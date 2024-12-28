import tkinter as tk

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

    def remove_input(self, frame):
        # Remove the frame and its widgets
        self.inputs.remove(frame)
        frame.destroy()

        # Re-add the minus button to the last input if there are multiple inputs
        if len(self.inputs) > 1:
            last_frame = self.inputs[-1]
            for widget in last_frame.winfo_children():
                if widget.cget("text") == "+":
                    minus_button = tk.Button(last_frame, text="-", command=lambda: self.remove_input(last_frame))
                    minus_button.pack(side=tk.LEFT, padx=5)

    def on_submit(self):
        urls = []
        for frame in self.inputs:
            entry = frame.winfo_children()[0]  # Get the Entry widget (first child)
            url = entry.get()  # Get the text from the Entry widget
            if url.strip():  # Only add non-empty inputs
                urls.append(url)
        print(urls)
    # TODO: Pass the list to another container or store in a DB


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = DynamicInputApp(root)
    root.mainloop()
