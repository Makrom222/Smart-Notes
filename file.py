from PyQt5.QtWidgets import (
    QPushButton, QWidget,QVBoxLayout,QHBoxLayout,QApplication,QLabel,
    QTextEdit,QLineEdit,QListWidget,QInputDialog
)

import json

app = QApplication([])
window = QWidget()
window.resize(800,600)
window.setWindowTitle('Smart Notes')


field_text = QTextEdit()

label_notes = QLabel('Список заметок')
list_notes = QListWidget()
create_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить  заметку')
save_note = QPushButton('Сохранить заметку')

label_tags = QLabel('Список тегов')
list_tags = QListWidget()
tag_input = QLineEdit()
create_tag = QPushButton('Добавить к  заметке')
delete_tag = QPushButton('Открепить от  заметки')
search_tag = QPushButton('Искать  заметку по тегу')



main_line = QHBoxLayout()
col_left = QVBoxLayout()
col_right = QVBoxLayout()
notes_line = QHBoxLayout()
tags_line = QHBoxLayout()



col_left.addWidget(field_text)

col_right.addWidget(label_notes)
col_right.addWidget(list_notes)


notes_line.addWidget(create_note)
notes_line.addWidget(delete_note)


col_right.addLayout(notes_line)
col_right.addWidget(save_note)

col_right.addWidget(label_tags)
col_right.addWidget(list_tags)
col_right.addWidget(tag_input)
tags_line.addWidget(create_tag)
tags_line.addWidget(delete_tag)


col_right.addLayout(tags_line)
col_right.addWidget(search_tag)

main_line.addLayout(col_left)
main_line.addLayout(col_right)
window.setLayout(main_line)

def add_note():
    note_name, confirm = QInputDialog.getText(window, 'Добавить заметку?','Название заметки:')
    if confirm and note_name != '' :


        notes[note_name] = {"текст":"","теги":[]}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["теги"])



def show_note():
    note = list_notes.selectedItems()[0].text()
    field_text.setText(notes[note]["текст"])
    list_tags.clear()
    # list_tags.addItems(notes[note]["тeги"])



def save():
    if list_notes.selectedItems():
        note = list_notes.selectedItems()[0].text()
        notes[note]["текст"] = field_text.toPlainText()
        with open("notes_data.json","w",encoding = 'utf-8') as file:
            json.dump(notes,file,sort_keys=True, ensure_ascii=False)
    else:
        print("Заметка для сохранения не выбрана!")



def del_note():
    if list_notes.selectedItems():
        note = list_notes.selectedItems()[0].text()
        del notes[note]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("notes_data.json","w",encoding = 'utf-8') as file:
            json.dump(notes,file,sort_keys=True, ensure_ascii=False)
    else:
        print("Заметка для удаления не выбрана!")

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = tag_input.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            list_tags.addItem(tag)
            tag_input.clear()
        with open  ("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print (notes)
    else:
        print("Заметка для добавления тега не выбрана!")


def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["теги"].append(tag)
        list_tags.clear()
        list_tags.addItem(notes[key]["теги"])
        with open ("notes_data.json","w")as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Тег для управления не выбран!")


def search_tag():
    print(search_tag.text())
    tag = tag_input.text()
    if search_tag.text() == "Искать заметки по тегу" and tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes [note]["теги"]:
                notes_filtered[note] = notes[note]
        search_tag.setText("Сбросить поиск")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
        print(search_tag.text())
    elif search_tag.text() == "Сбросить поиск":
        tag_input.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        search_tag.setText("Искать заметку по тегу")
        print(search_tag.text())
    else:
        pass






window.show()
with open('notes_data.json','r',encoding = 'utf-8')as file:
    notes = json.load(file)
list_notes.addItems(notes)


create_note.clicked.connect(add_note)


save_note.clicked.connect(save)

list_notes.itemClicked.connect(show_note)



delete_note.clicked.connect(del_note)







app.exec() 
