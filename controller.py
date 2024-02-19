import model
import view
import os.path

class Controller:
    
    def __init__(self):
        self.notes = []
        self.note_number = 0
        self.view = view.View()
        self.model = model.Model(self.notes)

    def start(self):
        flag = 'work'
        if(not(os.path.exists('note_book.csv'))):
            self.write_txt('note_book.csv', self.notes)
        self.notes = self.read_file('note_book.csv')
        while(flag != 'exit'):
            self.view.show_menu()
            flag = self.chose_action()
        self.write_txt('note_book.csv', self.notes)

    def chose_action(self):
        action = input('\nВыберите действие: ')
        match action:
            case '1':
                self.view.print_all_notes(self.notes)
            case '2':
                self.model.add_note()
            case '3':
                self.note_number = int(input('\nВыберите заметку: ')) - 1
                self.view.print_note(self.notes[self.note_number])
                self.view.show_additional_actions()
                self.chose_additional_action(input('\nВыберите действие: '))
            case '4':
                print(self.model.find_all_by_date(input('\nВведите дату: ')))
                
            case '8':
                return 'exit'

    def chose_additional_action(self, action):
        match action:
            case '1':
                self.model.edit_note(self.note_number)
            case '2':
                self.model.delite_note(self.note_number)
            case '3':
                return


    def read_file(self, filename):
        fields=['title', 'text', 'date']
        with open(filename, 'r', encoding='utf-8') as phb:
            for line in phb:
                if line == '\n':
                    continue
                record = dict(zip(fields, line.split(';')))
                self.notes.append(record)
        return self.notes

    def write_txt(self, filename, notes):
        with open(filename, 'w', encoding='utf-8') as phout:
            for i in range(len(notes)):
                s = ''
                for v in notes[i].values():
                    s += v + ';'
                phout.write(f'{s[:-1]}\n')