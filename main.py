import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.player = "𝕏"
        self.next_player = "𝕏"
        self.player1_score = 0
        self.player2_score = 0

        self.ui.pushButton_1.clicked.connect(self.button_clicked)
        self.ui.pushButton_2.clicked.connect(self.button_clicked)
        self.ui.pushButton_3.clicked.connect(self.button_clicked)
        self.ui.pushButton_4.clicked.connect(self.button_clicked)
        self.ui.pushButton_5.clicked.connect(self.button_clicked)
        self.ui.pushButton_6.clicked.connect(self.button_clicked)
        self.ui.pushButton_7.clicked.connect(self.button_clicked)
        self.ui.pushButton_8.clicked.connect(self.button_clicked)
        self.ui.pushButton_9.clicked.connect(self.button_clicked)

    def button_clicked(self):
        button = self.sender()

        if button.text() == "":
            button.setText(self.player)

            if self.check_winner():
                if self.player == "𝕏":
                    self.player1_score += 1
                    self.ui.label.setText(f"Player1_Score: {self.player1_score}")
                    QMessageBox.information(self, "Player Win", "Player 1 Wins!")

                    if self.player1_score == 3:
                        QMessageBox.information(
                            self,
                            "Game Winner",
                            "Player 1 Win Game!"
                        )
                        self.reset_game()
                        return

                else:
                    self.player2_score += 1
                    self.ui.label_2.setText(f"Player2_Score: {self.player2_score}")
                    QMessageBox.information(self, "Player Win", "Player 2 Wins!")

                    if self.player2_score == 3:
                        QMessageBox.information(
                            self,
                            "Game Winner",
                            "Player 2 Win Game!"
                        )
                        self.reset_game()
                        return

                self.change_start_player()
                self.reset_round()
                return

            if self.check_draw():
                QMessageBox.information(self, "Game Draw", "Game Draw!")
                self.change_start_player()
                self.reset_round()
                return

            if self.player == "𝕏":
                self.player = "𝕆"
            else:
                self.player = "𝕏"

    def check_winner(self):
        buttons = [
            self.ui.pushButton_1,
            self.ui.pushButton_2,
            self.ui.pushButton_3,
            self.ui.pushButton_4,
            self.ui.pushButton_5,
            self.ui.pushButton_6,
            self.ui.pushButton_7,
            self.ui.pushButton_8,
            self.ui.pushButton_9
        ]

        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winning_combinations:
            if (
                buttons[a].text() == self.player
                and buttons[b].text() == self.player
                and buttons[c].text() == self.player
            ):
                if self.player == "𝕏":
                    buttons[a].setStyleSheet("background-color: green;")
                    buttons[b].setStyleSheet("background-color: green;")
                    buttons[c].setStyleSheet("background-color: green;")
                else:
                    buttons[a].setStyleSheet("background-color: blue;")
                    buttons[b].setStyleSheet("background-color: blue;")
                    buttons[c].setStyleSheet("background-color: blue;")


                return True

        return False

    def check_draw(self):
        buttons = [
            self.ui.pushButton_1,
            self.ui.pushButton_2,
            self.ui.pushButton_3,
            self.ui.pushButton_4,
            self.ui.pushButton_5,
            self.ui.pushButton_6,
            self.ui.pushButton_7,
            self.ui.pushButton_8,
            self.ui.pushButton_9
        ]

        for button in buttons:
            if button.text() == "":
                return False

        return True

    def change_start_player(self):
        if self.next_player == "𝕏":
            self.next_player = "𝕆"
        else:
            self.next_player = "𝕏"

    def reset_round(self):
        buttons = [
            self.ui.pushButton_1,
            self.ui.pushButton_2,
            self.ui.pushButton_3,
            self.ui.pushButton_4,
            self.ui.pushButton_5,
            self.ui.pushButton_6,
            self.ui.pushButton_7,
            self.ui.pushButton_8,
            self.ui.pushButton_9,
        ]

        for button in buttons:
            button.setText("")
            button.setStyleSheet("")

        self.player = self.next_player

    def reset_game(self):
        self.player1_score = 0
        self.player2_score = 0

        self.ui.label.setText("Player1_Score: 0")
        self.ui.label_2.setText("Player2_Score: 0")

        self.reset_round()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())