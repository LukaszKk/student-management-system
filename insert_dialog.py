import sqlite3

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, \
    QPushButton


class InsertDialog(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Student Management System")

        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astroomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def add_student(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        cursor.execute(
            "insert into students (name, course, mobile) values (?, ?, ?)",
            (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        self.main_window.load_data()
