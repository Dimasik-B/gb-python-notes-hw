import datetime

class Model:

    def __init__(self, notes):
        self.notes = notes

    def add_note(self):
        today = datetime.date.today()
        note = {}
        note['title'] = input('\nВведите заголовок: ')
        note['text'] = input('\nВведите текст заметки: ')
        note['date'] = today.strftime("%d.%m.%Y")
        self.notes.append(note)

    def find_all_by_date(self, date):
        temp_notes = []
        for i in range(len(self.notes)):
                    if self.notes[i]['date'][:10] == date:
                        temp_notes.append(self.notes[i])
        return temp_notes
    
    def edit_note(self, note_number):
        self.notes[note_number]['text'] = input('\nВведите новый текст заметки: ')

    def delite_note(self, note_number):
        self.notes.pop(note_number)
