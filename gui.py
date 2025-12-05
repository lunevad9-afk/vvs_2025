from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtCore import Qt
import sys
<<<<<<< HEAD
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
=======


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.resize(800, 600)
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        
        input_label = QLabel("Введите текст для SEO анализа:")
        input_label.setStyleSheet("font-weight: bold; font-size: 10px;")
        layout.addWidget(input_label)
        
        self.text_input = QTextEdit()
        self.text_input.setMinimumHeight(200)
        self.text_input.setMaximumHeight(300)
        self.text_input.setPlaceholderText("Введите ваш текст здесь...")
        layout.addWidget(self.text_input)
        
        result_label = QLabel("результат:")
        result_label.setStyleSheet("font-weight: bold; font-size: 14px; margin-top: 10px;")
        layout.addWidget(result_label)
        
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)
        self.result_output.setMinimumHeight(200)
        self.result_output.setMaximumHeight(300)
        self.result_output.setPlaceholderText("Здесь появится SEO анализ вашего текста...")
        layout.addWidget(self.result_output)
        
        layout.addStretch()
        self.setLayout(layout)
        self.text_input.textChanged.connect(self.analyze_text)
    
    def analyze_text(self):
        text = self.text_input.toPlainText()
        
        if not text.strip():
            self.result_output.setPlainText("Введите текст для анализа")
            return
        
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        char_no_spaces = len(text.replace(" ", ""))
        paragraph_count = len([p for p in text.split('\n') if p.strip()])
        
        has_title = any(word in text.lower() for word in ["заголовок", "title"])
        has_keywords = any(word in text.lower() for word in 
                          ["ключ", "keyword", "seo", "оптимизация", "продвижение"])
        has_links = any(link in text.lower() for link in ["http://", "https://", "www."])
        
        analysis = f"""SEO АНАЛИЗ ТЕКСТА:

ОСНОВНЫЕ МЕТРИКИ:
• Количество слов: {word_count}
• Количество символов: {char_count}
• Количество символов без пробелов: {char_no_spaces}
• Количество абзацев: {paragraph_count}

SEO-ПОКАЗАТЕЛИ:
• {'✓ Наличие заголовка/тайтла' if has_title else '✗ Заголовок/тайтл не найден'}
• {'✓ Ключевые слова обнаружены' if has_keywords else '✗ Ключевые слова не обнаружены'}
• {'✓ Ссылки присутствуют' if has_links else '✗ Ссылки отсутствуют'}"""
        
        self.result_output.setPlainText(analysis)


if name == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow() 
    window.show()
    app.exec()
>>>>>>> 4a41242f6cebd501f95f81f768065d6b012885ac
