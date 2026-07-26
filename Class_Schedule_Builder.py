import csv
from operator import truediv

all_classes = []

#load data commented out because define error. Tried moving it to the top but the helper functions had the same errors.
#master_data = load_schedule()

add_another_class = True

while add_another_class:
    print('Create a course profile')

    class_name = input("Enter Class Name: ").strip().title()
    class_number = int(input("Enter Class Number: "))
    professor = input("Enter Professor name: ").strip().title()
    building = input("Enter Building name or 'online': ").strip().title()

    if building.lower() == "online":
        building = "Online"
        room_number = 'N/A'
    else:
        building = building
        room_number = input("Enter Room Number: ")

    course_profile = {
        'Name': class_name,
        'Number': class_number,
        'Professor': professor,
        'Building': building,
        'Room': room_number
    }
    all_classes.append(course_profile)
    print(f' Added {class_name} {class_number} with {professor}. Location: {building} {room_number}')

    print(f'[1] Add Another Class')
    print(f'[2] Continue to Schedule')
    decision = input('Enter 1 or 2: ')
    if decision == '1':
        add_another_class = True
    else:
        add_another_class = False

print(f'Total classes added: {len(all_classes)}')


#Course assignment inputs
master_data = []
processing_data = True
while processing_data:
    print('Select the class you want to add assignments to')
    for index, course_profile in enumerate(all_classes):
        print(f' {index + 1}. {course_profile}')

    while True:
        try:
            selection = int(input('Enter menu number: ').strip())
            if 1 <= selection <= len(all_classes):
                break
            else:
                print(f'Invalid option. Select from 1 to {len(all_classes)}')
        except ValueError:
            print('Please enter a valid number')
    selected_class = all_classes[selection - 1]
    print(f'Adding assignments to {selected_class['Name']}')
    print(f'Copy/Paste assignemnt schedule for {selected_class['Name']}')

    print("Type DONE on a separate line when finished.")
    pasted_schedule = []
#Change(1) to prevent a second blank enter from Professor (Enter DONE)
    while True:
        line = input()

        if line.strip().upper() == 'DONE':
            break

        pasted_schedule.append(line)
    raw_schedule = '\n'.join(pasted_schedule)


    #To remember the most recent date for an assignment to appear
    current_date = None
    pending_assignments = ''
    pending_module = ''

    for raw_line in raw_schedule.splitlines():
        cleaned_line = raw_line.strip()

        if not cleaned_line:
            continue

        #common headers to ignore
        if cleaned_line.lower() in ('date', 'due date', 'assignment', 'assignments'):
            continue
        line_lower = cleaned_line.lower()
        if line_lower.startswith(('week', 'no classes', 'midterm grades', 'holiday', 'last day', 'finals')):
            continue

        #month conversion for abbreviations
        month = {
            'JAN': '1', 'FEB': '2', 'MAR': '3', 'APR': '4', 'MAY': '5', 'JUN': '6', 'JUL': '7', 'AUG': '8', 'SEP': '9', 'SEPT': '9', 'OCT': '10', 'NOV': '11', 'DEC': '12'
        }
        #To read ranges with/without space
        try:
            parts = cleaned_line.replace('-', ' - ').split()

            #Merge modules with content name
            word_count = len(parts)
            is_module = cleaned_line.lower().startswith('module')
            if word_count <= 2 and is_module:
                pending_module = cleaned_line
                continue
            if pending_module:
                cleaned_line = pending_module + ': ' + cleaned_line
                parts = cleaned_line.replace('-', ' - ').split()
                pending_module = ''

            #Abbreviation converted to numerical value
            for part_index in range(len(parts)):
                upper_part = parts[part_index].upper()
                if upper_part in month:
                    parts[part_index] = month[upper_part]

            task_part = ''

            #Move date to front

            for i, part in enumerate(parts):
                if '/' in part and i!= 0:
                    parts = [parts[i]] + parts[:i] + parts[i+1:]
                    break
            #Numeric value for date or range
            if '/' in parts[0] and parts[0].replace('/', '').replace('-', '').isdigit():
                if len(parts) >= 3 and parts[1] == '-':
                    start_month = parts[0].split('/')[0]

                    if '/' in parts[2]:
                        end_date = parts[2]
                    else:
                        end_date = f'{start_month}/{parts[2]}'
                    current_date = f'{parts[0]}-{end_date}'
                    task_part = ' '.join(parts[3:])
                else:
                    current_date = parts[0]
                    task_part = ' '.join(parts[1:])

            #Numeric value for abbreviation date or range
            elif len(parts) >= 2 and parts[0].isdigit() and parts[1].isdigit():
                start_date = f'{parts[0]}/{parts[1]}'

                if len(parts) >= 4 and parts[2] == '-':
                    #Abv double digits x2
                    if len(parts) >= 5 and parts[3].isdigit() and parts[4].isdigit():
                        end_date = f'{parts[3]}/{parts[4]}'
                        task_date = ' '.join(parts[5:])
                    else:
                        end_date = f'{parts[0]}/{parts[3]}'
                        task_date = ' '.join(parts[4:])
                    current_date = f'{start_date}-{end_date}'
                else:
                    current_date = start_date
                    task_part = ' '.join(parts[2:])
        #Separate line/assignment problem fix!!
            elif current_date:
                task_part = cleaned_line

            #Remove tabs like separations for description
            if '\t' in task_part:
                task_part = task_part.split('\t')[0]
            elif '  ' in task_part:
                task_part = task_part.split('  ')[0]

            #Remove days for due dates
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

            for day in days:
                if day.lower() in task_part.lower():
                    task_part = task_part.replace(day, '').replace(day.lower(), '').strip()

            if current_date and task_part:
                assignment = {
                    'class_name': selected_class['Name'],
                    'class_number': selected_class['Number'],
                    'date': current_date,
                    'task': task_part.title(),
                    'completed': False
                }
                master_data.append(assignment)
            else:
                continue
        #Gives the error an explanation instead of burying it
        except Exception as error:
            print(f'Could not process: {cleaned_line}')
            print(f'Error: {error}')

    while True:
        print('What would you like to do next?')
        print('[1] Select another class')
        print('[2] Continue to Schedule')

        user_input = input('Enter 1 or 2: ')
        if user_input == '1':
            print('Returning to course selection')
            break
        elif user_input == '2':
            processing_data = False
            break
        else:
            print('Please enter a valid number')

#Sorting loop

for item in master_data:
    date_string = item['date']

    if '-' in date_string:
        range_parts = date_string.split('-')
        due_date = range_parts[1]
    else:
        due_date = date_string

    date_parts = due_date.split('/')
    item['month'] = int(date_parts[0])
    item['day'] = int(date_parts[1])

def sort_dates(item):
    """Extracts month and day from the assignments to sort chronologically"""
    return item['month'], item['day']

master_data.sort(key=sort_dates)

#Dynamic columns based on max assignment length
if master_data:
    max_task_length = max(max(len(item['task']) for item in master_data), 12)
else:
    max_task_length = 12

#Master Schedule

master_schedule = {}
for class_profile in all_classes:
    class_name = class_profile['Name']
    master_schedule[class_name] = []

for assignment in master_data:
    assignment_class = assignment['class_name']
    if assignment_class in master_schedule:
        master_schedule[assignment_class].append(assignment)

for class_name, assignments in master_schedule.items():
    profile_info = None
    for profile in all_classes:
        if profile['Name'] == class_name:
            profile_info = profile
            break
    print(f'{class_name.upper()} {profile_info['Number']}')
    print(f'Professor: {profile_info['Professor']}')
    print(f'Building: {profile_info['Building']} | Room Number: {profile_info['Room']}')
    print(f'{'Due Date':<12} | {'Assignment':<{max_task_length}} | {'Status'}')
    for item in assignments:
        status = 'Complete' if item['completed'] else 'Pending'
        print(f'{item['date']:<12} | {item['task']:<{max_task_length}} | {status}')

#load function not ordered properly at the top and caused more errors when this function and the write/read were moved up.
# def load_schedule(filename):
#     filename = 'master_schedule.csv'
#     '''supposed to load saved data from the csv and organize similarly to the read function below'''
#     data = []
#     try:
#         with open(filename, 'r', newline='') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 data.append({
#                     'class_name': row['Class Name'],
#                     'class_number': row['Class Number'],
#                     'date': row['Due Date'],
#                     'task': row['Assignment'],
#                     'completed': row['Status'] == 'Complete'
#                 })
#     except FileNotFoundError:
#         pass
#         print(f"No saved file found named '{filename}'.")
#     return data


#Write to CSV
def save_to_csv(data_list, filename):
    filename = 'master_schedule.csv'
    ''' saves assignments as a file to recall, update and save'''
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Class Name', 'Class Number', 'Due Date', 'Assignment', 'Status'])
        for item in data_list:
            status = 'Complete' if item['completed'] else 'Pending'
            writer.writerow([item['class_name'], item['class_number'], item['date'], item['task'], status])
save_to_csv(master_data, 'master_schedule.csv')

#Read CSV
def read_schedule_from_csv(filename):
    filename = 'master_schedule.csv'
    '''reads assignment records from the csv file and organizes them into a dictionary grouped by class name'''
    csv_schedule = {}
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                class_name = row['Class Name']
                if class_name not in csv_schedule:
                    csv_schedule[class_name] = []

                csv_schedule[class_name].append({
                    'class_name': row['Class Name'],
                    'class_number': row['Class Number'],
                    'date': row['Due Date'],
                    'task': row['Assignment'],
                    'completed': row['Status'] == 'Complete'
                })
    except FileNotFoundError:
        print(f"No saved file found named '{filename}'.")

    return csv_schedule

#Loop to edit status
while True:
    print('Update Assignment status')
    print('[1] Mark as assignment as completed')
    print('[2] Display updated schedule')
    print('[3] Exit program')

    try:
        choice = int(input('Enter your choice: ').strip())
    except ValueError:
        print('Please enter a valid number')
        continue
    if choice == 1:
        if not master_data:
            print('No assignments found.')
            continue
        for index, item in enumerate(master_data, 1):
            status = 'Completed' if item['completed'] else 'Pending'
            print(f"{index}. [{status}] {item['class_name']} - {item['date']} - {item['task']}")

        while True:
            try:
                task_number = int(input('Enter task number to complete: ').strip())
                if 1 <= task_number <= len(master_data):
                    selected = master_data[task_number - 1]
                    selected['completed'] = not selected['completed']
                    new_status = 'Completed' if selected['completed'] else 'Pending'
                    print(f'Updated {selected['task']} to {new_status}')
                    save_to_csv(master_data, 'master_schedule.csv')
                    break
                else:
                    print(f'Invalid option. Select from 1 to {len(master_data)}')
            except ValueError:
                print('Please enter a valid number')

    elif choice == 2:
        csv_data = read_schedule_from_csv('master_schedule.csv')
        if csv_data:
            print('Current Schedule')
            for class_name, assignments in csv_data.items():
                print(f'{class_name.upper()} {profile_info['Number']}')
                print(f'Professor: {profile_info['Professor']}')
                print(f'Building: {profile_info['Building']} | Room Number: {profile_info['Room']}')
                print(f'{'Due Date':<12} | {'Assignment':<{max_task_length}} | {'Status'}')
                for item in assignments:
                    status = 'Complete' if item['completed'] else 'Pending'
                    print(f'{item['date']:<12} | {item['task']:<{max_task_length}} | {status}')
    elif choice == 3:
        print('Schedule saved. Exit program')
        break
    else:
        print('Please enter a valid number')

