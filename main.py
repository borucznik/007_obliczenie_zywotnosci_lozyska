import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#reakcja na przycisk
def przelicz():
    #rzutowanie na int
    F_sila  = int(e1.text())
    C_nosnosc = int(e2.text())

    #sprawdzanie jaki jest typ łożyska
    if r1.isChecked():
        p_wsk = 3
    else:
        p_wsk = 3.33333
    #obliczenia zywotnosci
    L_10 = (C_nosnosc/F_sila)**p_wsk*100000
    e3.setText(str(L_10))
    #dane diagnostyczne
    print("Obliczenia:")
    print("F = " + str(F_sila) + " [N]")
    print("C = " + str(C_nosnosc) + " [N]")
    print("p = " + str(p_wsk))
    print("L_10 = " + str(L_10) + " [m]")

#zamykanie aplikacji
def zamknij():
    app.closeAllWindows()


app = QApplication(sys.argv)
win = QWidget()

#wigety

e0 = QLabel()
e0.setText("Wprowadź dane w jednostkach SI")

e1 = QLineEdit("1")
e1.setValidator(QIntValidator())

e2 = QLineEdit("1")
e2.setValidator(QIntValidator())

e3 = QLineEdit("0")
e3.setReadOnly(True)

validator = QDoubleValidator(0.99, 9.99,2)
validator.setNotation(QDoubleValidator.ScientificNotation)
e3.setValidator(validator)
#e3.setMaxLength(6)

flo = QFormLayout()
flo.addRow("Podaj dane", e0)
flo.addRow("Obciążenie [N]", e1)
flo.addRow("Nośność [N]", e2)
flo.addRow("Żywotność [m]", e3)

#radiobuttony do rodzaju łozyska
hbox = QHBoxLayout()
r1 = QRadioButton("Ball")
r1.setChecked(1)
r2 = QRadioButton("Roller")
hbox.addWidget(r1)
hbox.addWidget(r2)
hbox.addStretch()
flo.addRow(QLabel("Typ:"), hbox)

#przyciski
wyjscie = QPushButton("Wyjście")
wyjscie.clicked.connect(zamknij)
oblicz = QPushButton("Oblicz")
oblicz.clicked.connect(przelicz)
flo.addRow(wyjscie, oblicz)

#ustawienie widoku
win.setLayout(flo)

win.setWindowTitle("Kalkulator nośności łożysk")
win.show()

sys.exit(app.exec_())
