import json
import csv
import datetime


def read_note_file(file_name):
    with open(file_name, 'r') as f:
        notes = json.load(f)
        return notes


def save_notes_json(notes, file_name):
    with open(file_name, 'w') as f:
        json.bump(notes, f)


def save_note_csv(notes, file_name):
    with open(file_name, 'w') as f:
        json.dump(notes, f)


def filter_notes_by_date(notes, date):
    filter_notes = []
    for note in notes:
        note_date = datetime.datetime.strptime(note['timestamp'], '%Y-%m-%d-%H:%M:%S.%f')
        if note_date.date() == date:
            filter_notes.append(note)
            return filter_notes


def print_notes(notes):
    if not notes:
        print("None not found")
    else:
        for note in notes:
            print(f'ID: {note(["id"])}')
            print(f'Title: {note(["title"])}')
            print(f'Note: {note(["body"])}')
            print(f'Date/Time: {note(["timestamp"])}')
            print('---')


def add_note(notes):
    id - len(notes) + 1
    title = input('Enter title: ')
    body = input('Enter note')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f')
    new_note = {'id': id, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(new_note)
    return notes


# Функция для редактирования записи
def edit_note(note, id):
    for note in notes:
        if note['id'] == id:
            new_title = input(f'Enter new title: (was: {note["title"]}):')
            new_body = input(f'Enter new note (was: {note["body"]}): ')
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            break
            return notes

def delete_note(notes, id):
    for note in notes:
        if note['id']==id:
            notes.remove(note)
            break
            return notes

def main():
    file_name = 'notes.json'
    notes = read_note_file(file_name)

    while True:
        print('Choose action: ')
        print('1. Print all notes.')
        print('2. Print notes on date')
        print('3. Print note')
        print('4. Add new note')
        print('5. Edit note')
        print('6. Delite note')
        print('7. Exit')

        choice = input('Select option: ')

        if choice == '1':
            print_notes(notes)
        elif choice == '2':
            date_str = input('Enter date YEAR.MM.DD: ')
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            filted_notes = filter_notes_by_date(notes,date)
            print_notes(filted_notes)
        elif choice == '3':
            id = int(input('Enter ID note: '))
            note = [note for note in notes if note['id']==id]
            print_notes(note)
        elif choice == '4':
            notes = add_note(notes)
            save_notes_json(notes, file_name)
        elif choice == '5':
            id = int(input('Enter ID note for edit: '))
            notes = edit_note(notes, id)
            save_notes_json(notes,file_name)
        elif choice == '6':
            id = int(input('Enter ID note for delete: '))
            notes = delete_note(note,id)
            save_notes_json(notes, file_name)
        elif choice == '7':
            break
        print('Wrong enter')

        if _name_ == '_main_':
            main()

