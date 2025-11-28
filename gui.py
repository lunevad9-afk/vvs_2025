import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 1. Сначала создаем QApplication
app = QApplication(sys.argv)

# 2. Затем создаем виджеты
window = QWidget()
window.setWindowTitle("My GUI App")
window.setGeometry(100, 100, 400, 300)  # x, y, width, height
window.show()

# 3. Запускаем главный цикл приложения
sys.exit(app.exec_())  # Обратите внимание на подчеркивание: exec_()