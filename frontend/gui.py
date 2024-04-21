import tkinter
from backend.receiver import Receiver
from backend.sender import Sender


class GUI:
    def __init__(self, email, password):
        self.window = tkinter.Tk()
        self.state = "receiver"
        self.left_canvas = None

        self.sender = Sender(email, password)
        self.receiver = Receiver(email, password)
        self.show_receiver_screen()

    def clear_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def send_pressed(self):
        if self.state != "sender":
            self.left_canvas.delete("all")
            self.left_canvas.pack_forget()
            self.clear_screen()
            self.show_sender_screen()

    def inbox_pressed(self):
        self.receiver.establish_connection()
        self.left_canvas.delete("all")
        self.left_canvas.pack_forget()
        self.clear_screen()
        self.show_receiver_screen()

    def send_message_pressed(self, to, bcc, subject, message, to_entry, bcc_entry, subject_entry, text_widget):
        self.sender.send_message(to, bcc, subject, message)
        to_entry.delete(0, tkinter.END)
        bcc_entry.delete(0, tkinter.END)
        subject_entry.delete(0, tkinter.END)
        text_widget.delete('1.0', tkinter.END)

    def show_sender_screen(self):
        self.state = "sender"

        width = 800
        height = 600

        self.window.maxsize(width=width, height=height)
        self.window.minsize(width=width, height=height)
        self.window.title("Sender")

        button_font = ("Helvetica", 15, "bold")
        label_font = ("Helvetica", 10)

        self.left_canvas = tkinter.Canvas(self.window, width=width, height=height)
        self.left_canvas.pack()

        seperator = self.left_canvas.create_rectangle(250, 10, 251, 590, fill="black")

        buttons_width = 180
        buttons_height = 50

        inbox_button_x = 120
        inbox_button_y = 100
        inbox_button = tkinter.Button(text="Inbox", font=button_font, foreground="white", background="blue",
                                      command=self.inbox_pressed)
        inbox_button_window = self.left_canvas.create_window(inbox_button_x, inbox_button_y, width=buttons_width,
                                                             height=buttons_height, window=inbox_button)

        send_button_x = 120
        send_button_y = 170
        send_button = tkinter.Button(text="Send", font=button_font, foreground="white", background="blue",
                                     relief=tkinter.SUNKEN, command=self.send_pressed)
        send_button_window = self.left_canvas.create_window(send_button_x, send_button_y, width=buttons_width,
                                                            height=buttons_height, window=send_button)

        to_label_x = 270
        to_label_y = 10
        to_label = tkinter.Label(text="To: ", font=label_font)
        to_label.place(x=to_label_x, y=to_label_y)

        to_entry_x = 330
        to_entry_y = 10
        to_entry = tkinter.Entry(font=label_font, width=62)
        to_entry.place(x=to_entry_x, y=to_entry_y)

        bcc_label_x = 270
        bcc_label_y = 30
        bcc_label = tkinter.Label(text="BCC: ", font=label_font)
        bcc_label.place(x=bcc_label_x, y=bcc_label_y)

        bcc_entry_x = 330
        bcc_entry_y = 30
        bcc_entry = tkinter.Entry(font=label_font, width=62)
        bcc_entry.place(x=bcc_entry_x, y=bcc_entry_y)

        subject_label_x = 270
        subject_label_y = 50
        subject_label = tkinter.Label(text="Subject: ", font=label_font)
        subject_label.place(x=subject_label_x, y=subject_label_y)

        subject_entry_x = 330
        subject_entry_y = 50
        subject_entry = tkinter.Entry(font=label_font, width=62)
        subject_entry.place(x=subject_entry_x, y=subject_entry_y)

        text_widget_x = 270
        text_widget_y = 90
        text_widget = tkinter.Text(self.window, font=label_font, width=72)

        # Create a frame to hold the Text widget and scrollbar
        frame = tkinter.Frame(self.window)
        frame.place(x=text_widget_x, y=text_widget_y)

        # Create a Text widget with a specific height and width
        text_widget = tkinter.Text(frame, width=62, wrap="word")
        text_widget.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        # Create a vertical scrollbar
        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Attach the scrollbar to the Text widget
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)

        send_message_button_x = 450
        send_message_button_y = 500
        send_message_button = tkinter.Button(text="Send", font=button_font, foreground="white", background="blue",
                                             command=lambda: self.send_message_pressed(to_entry.get(), bcc_entry.get(),
                                                                                       subject_entry.get(),
                                                                                       text_widget.get("1.0",
                                                                                                       tkinter.END),
                                                                                       to_entry,
                                                                                       bcc_entry,
                                                                                       subject_entry,
                                                                                       text_widget
                                                                                       ))
        send_message_button.place(x=send_message_button_x, y=send_message_button_y, width=buttons_width,
                                  height=buttons_height)

        self.window.mainloop()

    def show_receiver_screen(self):
        self.state = "receiver"

        width = 800
        height = 600
        left_canvas_width = 252
        left_canvas_height = 600

        button_font = ("Helvetica", 15, "bold")
        label_font = ("Helvetica", 10)

        self.window.maxsize(width=width, height=height)
        self.window.minsize(width=width, height=height)
        self.window.title("Receiver")

        self.left_canvas = tkinter.Canvas(self.window, width=left_canvas_width, height=left_canvas_height)
        self.left_canvas.place(x=0, y=0)

        seperator = self.left_canvas.create_rectangle(250, 10, 251, 590, fill="black")

        buttons_width = 180
        buttons_height = 50

        inbox_button_x = 120
        inbox_button_y = 100
        inbox_button = tkinter.Button(text="Inbox", font=button_font, foreground="white", background="blue",
                                      relief=tkinter.SUNKEN, command=self.inbox_pressed)
        inbox_button_window = self.left_canvas.create_window(inbox_button_x, inbox_button_y, width=buttons_width,
                                                             height=buttons_height, window=inbox_button)

        send_button_x = 120
        send_button_y = 170
        send_button = tkinter.Button(text="Send", font=button_font, foreground="white", background="blue",
                                     command=self.send_pressed)
        send_button_window = self.left_canvas.create_window(send_button_x, send_button_y, width=buttons_width,
                                                            height=buttons_height, window=send_button)

        message_info = self.receiver.get_last_message()

        from_label_x = 270
        from_label_y = 10
        from_label = tkinter.Label(text="From: ", font=label_font)
        from_label.place(x=from_label_x, y=from_label_y)

        from_data_label_x = 320
        from_data_label_y = 10
        from_data_label = tkinter.Label(text=message_info["From"], font=label_font)
        from_data_label.place(x=from_data_label_x, y=from_data_label_y)

        bcc_label_x = 270
        bcc_label_y = 30
        bcc_label = tkinter.Label(text="BCC: ", font=label_font)
        bcc_label.place(x=bcc_label_x, y=bcc_label_y)

        bcc_data_label_x = 320
        bcc_data_label_y = 30
        bcc_data_label = tkinter.Label(text=message_info["BCC"], font=label_font)
        bcc_data_label.place(x=bcc_data_label_x, y=bcc_data_label_y)

        date_label_x = 270
        date_label_y = 50
        date_label = tkinter.Label(text="Date: ", font=label_font)
        date_label.place(x=date_label_x, y=date_label_y)

        date_data_label_x = 320
        date_data_label_y = 50
        date_data_label = tkinter.Label(text=message_info["Date"], font=label_font)
        date_data_label.place(x=date_data_label_x, y=date_data_label_y)

        subject_label_x = 270
        subject_label_y = 70
        subject_label = tkinter.Label(text="Subject: ", font=label_font)
        subject_label.place(x=subject_label_x, y=subject_label_y)

        subject_data_label_x = 320
        subject_data_label_y = 70
        subject_data_label = tkinter.Label(text=message_info["Subject"], font=label_font)
        subject_data_label.place(x=subject_data_label_x, y=subject_data_label_y)

        text_widget_x = 270
        text_widget_y = 90
        text_widget = tkinter.Text(self.window, font=label_font, width=72)

        # Create a frame to hold the Text widget and scrollbar
        frame = tkinter.Frame(self.window)
        frame.place(x=text_widget_x, y=text_widget_y)

        # Create a Text widget with a specific height and width
        text_widget = tkinter.Text(frame, width=62, wrap="word")
        text_widget.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        # Create a vertical scrollbar
        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        # Attach the scrollbar to the Text widget
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)

        text_widget.insert(tkinter.END, message_info["Content"])
        self.window.mainloop()
