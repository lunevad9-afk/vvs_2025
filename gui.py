import sys
from PyQt5.QtWidgets import *

class TextAnalyzer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Анализатор текста')
        self.setGeometry(100, 100, 600, 500)
        
        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Основной layout
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Метка для поля ввода
        input_label = QLabel("Введите текст:")
        main_layout.addWidget(input_label)
        
        # Поле для ввода текста со скроллбаром
        self.text_input = QTextEdit()
        self.text_input.setAcceptRichText(False)
        main_layout.addWidget(self.text_input)
        
        # Кнопка для анализа
        analyze_button = QPushButton("Анализировать текст")
        analyze_button.clicked.connect(self.analyze_text)
        main_layout.addWidget(analyze_button)
        
        # Метка "Результат"
        result_label = QLabel("Результат:")
        main_layout.addWidget(result_label)
        
        # Поле для вывода результата
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)
        main_layout.addWidget(self.result_output)
        
        # Пространство внизу
        main_layout.addStretch(1)
        
    def analyze_text(self):
        # Получаем текст из поля ввода
        text = self.text_input.toPlainText()
        
        # Простой анализ текста
        char_count = len(text)
        word_count = len(text.split())
        line_count = len(text.splitlines())
        
        # Формируем результат
        result = f"Статистика текста:\n"
        result += f"Символов: {char_count}\n"
        result += f"Слов: {word_count}\n"
        result += f"Строк: {line_count}\n"
        
        # Выводим результат
        self.result_output.setPlainText(result)

# Запуск приложения
app = QApplication(sys.argv)
window = TextAnalyzer()
window.show()
sys.exit(app.exec_())