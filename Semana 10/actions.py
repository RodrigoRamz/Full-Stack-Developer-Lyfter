#actions.py
#program logic to read grades and students with validation
#add/list/top3/average from the students list

def read_grade(label): #ask for a grade, retry when grade is not <=0 and >=100.
    while True:
        grade = input(f'Grade of {label} (0-100): ').strip()
        try:
            n = int(grade) #convert to a number. If fail then ValueError
        except ValueError:
            print('Error: Add a valid number.')
            continue
        if 0 <= n <= 100:
            return n
        print('Error: grade should be a number between 0 and 100')


def read_student(): #returns a dictionary with the student valid values
    while True:
        name = input('Full Name: ').strip() #.strip() clean the spaces/jumps
        if not name:
            print('Full Name cannot be empty.')
            continue

        group = input('Add your group: ').strip()
        if not group:
            print('Group field cannot be empty.')
            continue

        spa = read_grade('spanish')
        eng = read_grade('english')
        geo = read_grade('geography')
        sci = read_grade('sciences')

        return {
            'name': name, 
            'group': group,
            'spanish': spa,
            'english': eng,
            'geography': geo,
            'sciences': sci,
        }
    

def add_students(students): #allow adding n students, register is added by .append()
        while True:
            register = read_student()
            students.append(register) #the list is updated here
            print(f"Added: {register['name']} ({register['group']})")
            if input('Add another student? (Yes/No): ').strip() != 'Yes':
                break


def student_average_grade(s): #Average grade from the 4 signature
    return (s['spanish'] + s['english'] + s['geography'] + s['sciences']) / 4


def listing(students): #print all students in a table format
    if not students:
        print('There are no students.')
        return
    print('\nName     Group spa eng geo sci avg')
    print('_'*70)
    for s in students:
        avg = student_average_grade(s)
        print(
            f"{s['name'][:30]:30} {s['group'][:8]:8}"
            f"{s['spanish']:>3} {s['english']:>3} {s['geography']:>3} {s['sciences']:>3} {avg:5.2f}"
        )


def top3(students): #show the top 3 best average grades
    if not students:
        print('There is no data to show the Top 3.')
        return
    rank = sorted(students, key=student_average_grade, reverse=True)
    top = rank[:3]
    print('\nTop 3')
    print('Rank Name.     Group Avg')
    print('_'*50)
    for i, s in enumerate(top, start=1):
        print(f"{i:>4} {s['name'][:30]:30} {s['group'][:8]:8} {student_average_grade(s):>5.2f}")


def global_average(students): #calculate the global average all grades
    if not students:
        print('There is no data for global average.')
        return
    average_grade = [student_average_grade(s) for s in students]
    print(f'Global Average: {sum(average_grade) / len(average_grade):.2f}') 