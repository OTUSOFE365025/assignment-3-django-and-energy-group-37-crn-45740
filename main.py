############################################################################
# Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import Product

############################################################################
# START OF APPLICATION
############################################################################
""" Replace the code below with your own """
Product.objects.all().delete()
Product.objects.create(name="ProductA", price=49.99, upc="200001149995")
Product.objects.create(name="ProductB", price=11.25, upc="200002111254")
Product.objects.create(name="ProductC", price=239.21, upc="200003000454")

# Attempt to find provided item via UPC

# Initialize PyQt5 window
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cash Register")

        self.product_info = QLabel()
        self.product_info.setAlignment(Qt.AlignCenter)

        self.upc_lu_box = QLineEdit()

        button = QPushButton("Check UPC")
        button.clicked.connect(self.check_upc)

        buffer = QWidget()

        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(self.upc_lu_box)
        layout.addWidget(button)
        layout.addWidget(self.product_info)
        layout.addStretch()

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    
    def check_upc(self):
        try:
            upc_lu=self.upc_lu_box.text()
            p = Product.objects.get(upc=upc_lu)
            self.product_info.setText(f"UPC: {p.upc}, Name: {p.name}, Price: {p.price}")
        except Product.DoesNotExist:
            self.product_info.setText(f"Product with UPC '{upc_lu}' not found!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
