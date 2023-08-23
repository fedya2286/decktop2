from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QListWidget, QTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout
import json

# создаем приложение
app = QApplication([])
window = QWidget()
window.setWindowTitle('Путеводитель')


# создаем интерфейс
list_countries = QListWidget
text_countries = QTextEdit
name_countries = QLineEdit
add_country_button = QPushButton('добавить страну')
del_country_button = QPushButton('удалить страну')
edit_country_button = QPushButton('изменить страну')

main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
right_layout = QVBoxLayout()
layout_button = QHBoxLayout()

layout_button.addWidget(add_country_button)
layout_button.addWidget(del_country_button)
layout_button.addWidget(edit_country_button)

left_layout.addWidget(list_countries)
right_layout.addWidget(text_countries)
right_layout.addWidget(name_countries)
right_layou.addWidget(layout_button)

main_layout.addLayout(left_layout, 3)
main_layout.addLayout(right_layout, 7)

window.setLayout(main_layout)

# функционал
#countries = {
#   'Россия': 'самая большая страна в мире',
#  'Китай': 'самая населенная страна в мире'
#}

#   with open('countries.json', 'w', encoding='utf-8') as file:
#       json.dump(countries, file)

def fill_countries():
    list_countries.clear()
    with open('countries.json', 'r', encoding='utf-8') as file:
        coutries = json.load(file)
        for country in countries:
            list_countries.addItem(country)

fill_countries()

def clear_widgets():
    text_countries.clear()
    name_countries.clear()

#   with open('countries.json', 'r', encoding='utf-8') as file:
#       countries = json.load(file)
#       for country in countries:
#           list_countries.addItem(country)

def info_country():
    country = list_countries.selectedItems()[0].text()
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    text_countries.setText(countries[country])

def add_country():
    country = name_countries.text()
    with open('countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)
    if not(country in countries):
        countries[country] = ''
    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(countries, file)
    list_countries.clear()
    for country in countries:
        list_countries.addItem(country)

def del_country():
    if list_countries.selectedItems():
        country = list_countries.selectedItems()[0].text()
        with open('countries.json', 'r', encoding='utf-8') as file:
            countries = json.load(file)
        del countries[country]
        with open('countries.json', 'w', encoding='utf-8') as file:
            json.dump(countries, file)
        fill_countries()
        clear_widgets()


def edit_country():
    if list_countries.selectedItems():
        country = list_countries.selectedItems()[0].text()
        with open('countries.json', 'r', encoding='utf-8') as file:
            countries = json.load(file)
            text_country = text_countries.toPlainText()
            countries[country] = text_country
            with open('countries.json', 'w', encoding='utf-8') as file:
                json.dump(countries, file)
            text_countries.clear()
            clear_widgets



add_country_button.clicked.connect(add_country)
del_country_button.clicked.connect(del_country)
edit_country_button.clicked.connect(edit_country)
list_country_button.clicked.connect(list_country)




window.show()
app.exec()