
from Models.Student import Student 


def _read_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print('Value cannot be empty. Try again.')


def _read_score(prompt):
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if 0 <= v <= 100:
                return v
            print('Score must be between 0 and 100.')
        except ValueError:
            print('Score must be a number')


def add_students(student_list):
    print('\n=== Add Students ===')
    while True:
        name = _read_nonempty('Name: ')
        group = _read_nonempty('Group: ')
        spanish = _read_score('Spanish (0-100): ')
        english = _read_score('English (0-100): ')
        geography = _read_score('Geography (0-100): ')
        sciences = _read_score('Sciences (0-100): ')

        try:
            s = Student (name, group, spanish, english, geography, sciences)
            student_list.append (s) #objects are now saved
            print(f'Added: {s.name} (Group {s.group}) - Avg: {s.average(): .2f}')
        except ValueError as e:
            print(f'Could not add student: {e}')

        more = input('Add another? (y/n): ').strip().lower()
        if more != 'y':
            break    

def listing(students_list):
    print('\n=== Students List ===')
    if not students_list:
        print('No students yet.')
        return
    header = f"{'Name':<20}{'Group':<10}{'Spanish':>9}{'English':>9}{'Geography':>9}{'Sciences':>9}{'Avg':>8}"
    print(header)
    print("-" * len(header))

    for st in students_list:
        print(f'{st.name:<20}{st.group:<10}'
            f'{st.spanish:>9}{st.english:>9}{st.geography:>9}{st.sciences:>9}'
            f'{st.average():>8.1f}')
        

def top3(students_list):
    print('\n=== Top 3 Students ===')
    if not students_list:
        print('No students to rank')
        return
    
    ordered = sorted(students_list, key=lambda s: s.average(), reverse=True)[:3]
    for i, st in enumerate(ordered, 1):
        print(f'{i}. {st.name} (Group {st.group}) - Avg: {st.average():.2f}')

def global_average(students_list):
    print('\n=== Global Average ===')
    if not students_list:
        print('No students yet/')
        return
    avg = sum(s.average() for s in students_list) / len(students_list)
    print(f'Global average: {avg:.2f}')