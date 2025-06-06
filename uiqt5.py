from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QCheckBox, QMessageBox
from logi_class import ADBLogic

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LDPlayer9 ADB Controller")
        self.adb = ADBLogic()

        # UI Elements
        self.btn_get_devices = QPushButton("Get LDPlayer9 Devices")
        self.checkbox_select_all = QCheckBox("Select All Devices")
        self.device_list_widget = QListWidget()
        self.btn_start_fb = QPushButton("Start Facebook App")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.btn_get_devices)
        layout.addWidget(self.checkbox_select_all)
        layout.addWidget(self.device_list_widget)
        layout.addWidget(self.btn_start_fb)
        self.setLayout(layout)

        # Events
        self.btn_get_devices.clicked.connect(self.load_devices)
        self.checkbox_select_all.stateChanged.connect(self.toggle_select_all)
        self.btn_start_fb.clicked.connect(self.start_facebook_on_selected)

    def load_devices(self):
        devices = self.adb.get_ldplayer_devices()
        self.device_list_widget.clear()
        for dev in devices:
            self.device_list_widget.addItem(dev)

    def toggle_select_all(self, state):
        for i in range(self.device_list_widget.count()):
            item = self.device_list_widget.item(i)
            item.setSelected(self.checkbox_select_all.isChecked())

    def start_facebook_on_selected(self):
        selected = [self.device_list_widget.item(i).text() 
                    for i in range(self.device_list_widget.count()) 
                    if self.device_list_widget.item(i).isSelected()]
        if not selected:
            QMessageBox.warning(self, "No Devices", "Please select at least one device.")
            return
        for device_id in selected:
            self.adb.start_facebook(device_id)
