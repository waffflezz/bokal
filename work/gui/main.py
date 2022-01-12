import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import QtGui
from hotel import Ui_Form
from work.main import Terminal


class hotel_ui(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.terminal = Terminal()

        self.buttons_room = []
        self.current_button = None

        for room in self.terminal.hotel.rooms:
            button = QPushButton(self.scrollAreaWidgetContents)
            button.setText(f'{room.room_type} | номер: {room.number} | цена: {room.cost}р')
            button.room = room
            button.clicked.connect(self.choose)

            if room.state is False:
                button.setStyleSheet('background: rgb(114, 213, 147);')
            else:
                button.setStyleSheet('background: rgb(189, 90, 94);')

            self.verticalLayout.addWidget(button)
            self.buttons_room.append(button)

        self.showButton.clicked.connect(self.show_info)
        self.buyButton.clicked.connect(self.buy_room)
        self.cancelButton.clicked.connect(self.cancel_arend)

    def choose(self):
        button = self.sender()
        self.current_button = button
        self.textBrowser.setText(button.room.__str__())

    def show_info(self):
        self.textBrowser.setText(
            self.terminal.show_arend() +
            f'\nДата и время аренды: '
            f'{self.dateTimeEdit.dateTime().toPyDateTime()}')

    def buy_room(self):
        if self.current_button is not None and self.current_button.room.state is False:
            self.terminal.arend_room(self.current_button.room.number)
            self.textBrowser.setText(self.current_button.room.__str__())
            self.current_button.setStyleSheet('background: rgb(113, 105, 182);')

    def cancel_arend(self):
        self.terminal.hotel.arend_rooms.remove(self.current_button.room)
        self.current_button.room.state = False
        self.current_button.setStyleSheet('background: rgb(114, 213, 147);')
        self.textBrowser.setText(self.current_button.room.__str__())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = hotel_ui()
    window.show()
    app.exec_()
    exit()
