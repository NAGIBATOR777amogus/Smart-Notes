from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout, QInputDialog
app = QApplication([])
import json


notes = {'Добро пожаловать': {'текст': 'в этом приложении можно создавать заметки с тегами', 'теги': ['умные заметки','инструкция']}}
with open("notes_data.json", "w",encoding='utf-8') as file:
    json.dump(notes, file)

def show_note():
    name = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[name]['теги']) 
    
def add_note():
    note_name, ok = QInputDialog.getText(notes_win,'добавить заметку','название заметки')
    if ok and note_name != '':
        notes[note_name] = {'текст': '' , 'теги':[]}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['теги'])
        print(notes)
def del_note():
    if list_notes.selectedItems():

        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open('notes_data.json','w')as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        print('Заметка для удаления выбрана')
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open('notes_data.json','w') as file:
            json.dump(notes,file, sort_keys = True)
        print(notes)
    else:
        print ('заметка для солхранения не выбрана')
def add_tag():
    if list_notes.selectedItems():
        key =list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open('notes_data.json','w') as file:
            json.dump(notes,file,sort_keys=True)

    else: 
        print('заметка для добавления тега не выбрана')
def del_tag():
    if list_tags.selectedItems():
        key =list_notes.selectedItems()[0].text()
        tag = list_notes.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        list_tags.addItems(notes[key]['теги'])
        with open('notes_data.json','w') as file:
            json.dump(notes,file,sort_keys=True)
    else:
        print('тег для удаления не выбран')
def search_tag():
    tag = field_tag.text()
    if button_tag_search.text() == 'Искать заметки по тегу'and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note]=notes[note]
        button_tag_search.setText('сбросить поиск')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)       
    elif button_tag_search.text() == 'сбросить поиск':
        field_tag.clear() 
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText('Искать заметки по тегу')
    else:
        pass

'''Интерфейс приложения'''
#параметры окна приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900, 600)

#виджеты окна приложения
list_notes = QListWidget()
list_notes.addItems(notes)
list_notes_label = QLabel('Список заметок')
 
button_note_create = QPushButton('Создать заметку') #появляется окно с полем "Введите имя заметки"
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
 
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
btn_lt1 = QHBoxLayout()
btn_lt1.addWidget(button_note_create)
btn_lt1.addWidget(button_note_save)
col_2.addLayout(btn_lt1)
col_2.addWidget(button_note_del)
btn_lt = QHBoxLayout()
btn_lt.addWidget(button_tag_add)
btn_lt.addWidget(button_tag_del)
col_2.addLayout(btn_lt)
col_2.addWidget(button_tag_search)
col_2.addWidget(list_tags_label)
col_2.addWidget(list_notes)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

layout_notes.addLayout(col_1, stretch = 2)   
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)
list_notes.itemClicked.connect(show_note)
button_note_del.clicked.connect(del_note)
button_note_create.clicked.connect(add_note)
button_note_save.clicked.connect(save_note)
button_tag_add.clicked.connect(add_tag)
button_note_del.clicked.connect(save_note)
button_tag_search.clicked.connect(search_tag)
notes_win.show()
app.exec_()
#начни тут создавать приложение с умными заметками