from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt6.QtCore import Qt
import sys


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
