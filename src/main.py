from functions import send_data
from tkinter import (
    Frame,
    Label,
    Text,
    Entry,
    Button,
    LEFT,
    END,
    Tk,
)


class App:
    def __init__(self, root) -> None:
        root.title("ServiceNow query tester")
        root.resizable(0, 0)

        self.main_frame = Frame(root).pack()

        self.left_frame = Frame(self.main_frame, height=330, width=300)
        self.left_frame.pack(side=LEFT, anchor="n")
        self.left_frame.pack_propagate(0)

        self.right_frame = Frame(self.main_frame, height=330, width=300)
        self.right_frame.pack_forget()
        self.right_frame.pack_propagate(0)

        Label(self.left_frame, text="Tibco URL").pack(fill="x")
        self.url = Entry(self.left_frame)
        self.url.pack(fill="x")

        Label(self.left_frame, text="Table").pack(fill="x")
        self.table = Entry(self.left_frame)
        self.table.pack(fill="x")

        Label(self.left_frame, text="Query").pack(fill="x")
        self.query = Entry(self.left_frame)
        self.query.pack(fill="x")

        Label(self.left_frame, text="Fields").pack(fill="x")
        self.fields = Text(self.left_frame, height=10)
        self.fields.pack(fill="x")

        Button(
            self.left_frame,
            text="Send",
            command=self.send_data
        ).pack(fill="x", anchor='s', expand=True)

        Label(self.right_frame, text="Return").pack(fill="x")
        self.data = Text(
            self.right_frame,
            height=17
        ).pack(fill="x")

        Button(
            self.right_frame,
            text="Copy",
            command=self.copy_content
        ).pack(fill="x", anchor='s', expand=True)

    def send_data(self):
        url = self.url.get()
        table = self.table.get()
        query = self.query.get()
        fields = self.fields.get("1.0", END)
        fields_list = [i for i in fields.split('\n') if i]
        data = send_data(url, table, query, fields_list)
        print(data)
        self.right_frame.pack(side=LEFT, anchor="n")

    def copy_content(self):
        pass


if __name__ == "__main__":
    root = Tk()
    App(root)
    root.mainloop()
