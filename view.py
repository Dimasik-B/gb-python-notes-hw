class View:
    
    def __init__(self):
        pass

    def show_menu(self):
        print('\n1. Вывести все заметки',
            '2. Добавить заметку',
            '3. Открыть заметку',
            '4. Выборка по дате',
            '8. Закончить работу', sep = '\n')
        
    def show_additional_actions(self):
        print('1. Редактировать заметку',
            '2. Удалить заметку',
            '3. Закрыть', sep = '\n')
        
    def print_note(self, note):
        print(f"\nЗаголовок: {note['title']}\nТекст: {note['text']}\n Дата: {note['date']}")
    
    def print_all_notes(self, notes):
        for i in range(len(notes)):
            print(f"\n{i + 1}). {notes[i]['title']}")
