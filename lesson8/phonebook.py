# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных

FILEPATH = 'phonebook.txt'
FILEENC = "utf-8"

def handle_input(greeting, skip = False):
    input_str = input(greeting)
    while (input_str == "" and skip == False):
        return input('Please enter the string or "n" to escape: ')
    if input_str == "n":
        return False
    return input_str

def records_list():
    try:
        with open(FILEPATH, 'r+', encoding=FILEENC) as pb:
            records = [line.strip("\n") for line in pb.readlines() if line != '\n']
            records.sort()
    except:
        print(f"Файла нет, поэтому создадим.")
        records = []
    return records

def line_search(search_line):
    records = records_list()
    return [line for line in records if not search_line or search_line.lower() in line.lower()]

def line_write(line, records=[]):
    records = records_list()
    records.append(line)
    records.sort()
    with open(FILEPATH, 'w+', encoding=FILEENC) as pb:
        pb.write("\n".join(records))

def line_remove(line_del):
    records = [line for line in records_list() if line != line_del]
    with open(FILEPATH, 'w', encoding=FILEENC) as pb:
        pb.write("\n".join(records))

def line_replace(line_del, line_append):
    records = [line for line in records_list() if line != line_del]
    records.append(line_append)
    records.sort()
    with open(FILEPATH, 'w', encoding=FILEENC) as pb:
        pb.write("\n".join(records))

def main():
    action = handle_input("What to do: \nr(read)\nw(write)\ne(edit)\nd(delete): ")
    while (action and action not in ['r', 'w', 'd', 'e']):
        action = input('Please tell what to do (r/w/d/e)?: ')
    match action:
        case "r":
            action_read()
        case "w":
            action_write()
        case "d":
            action_delete()
        case "e":
            action_edit()

def action_read(greeting = "Searching for something? (Skip to view all): "):
    if search_str := handle_input(greeting, True):
        print('\n'.join(line_search(search_str)))
        action_read('Something else (print "n" to escape)?: ')

def action_write(greeting = "What to add: "):
    if new_line := handle_input(greeting):
        line_write(new_line)
        if len(line_search(new_line)) > 0:
            print(f"{new_line} added")
        action_write('Want to add something else ("n" to finish)? ')

def action_delete(greeting = "What to delete: "):
    if line := handle_input(greeting):
        to_del = line_search(line)
        if len(to_del) > 0:
            list_to_del = '\n'.join(to_del)
            confirm = handle_input\
                (f"The following records will be deleted, print 'y' to confirm:\n{list_to_del}\n")
            if (confirm == 'y'):
                for line in to_del:
                    line_remove(line)
            else:
                action_delete('Change the search word or press "n" to escape: ')
        else:
            action_delete('Nothing found, please try again: ')

def action_edit(greeting = "What to edit: "):
    if line := handle_input(greeting):
        if len(lines_found := line_search(line)) > 1:
            action_edit(f'A few records found, please narrow the search ("n" to escape)\n{list(lines_found)}: ')
        elif len(lines_found) > 0:
            if replacement := handle_input(f"{list(lines_found)}\n Replace with: "):
                line_replace(lines_found[0], replacement)
            action_edit("Something else ('n' if no): ")

main()
