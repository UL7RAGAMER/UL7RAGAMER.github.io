details = [
    ("student name", "Enter student name: "),
    ("Roll No", "Enter Roll No: "),
    ("Class", "Enter Class: "),
    ("Section", "Enter Section: "),
    ("Address Line 1", "Enter Address Line 1: "),
    ("Address Line 2", "Enter Address Line 2: "),
    ("City", "Enter City: "),
    ("Postal Code", "Enter Postal Code: "),
    ("Parent's/ Guardians's Contact No", "Enter Parent's/ Guardians's Contact No: ")
]

input_values = [input(prompt) for _, prompt in details]

formatted_details = [f"{label}: {value}" for (label, _), 
                     value in zip(details, input_values)]

max_length = max(len(detail) for detail in formatted_details)
print('-' * (max_length + 5))
print('|',' ' * (int(max_length / 2)),"Vydehi", ' ' * (int(max_length / 2) - 6),'|')
print('-' * (max_length + 5))
for detail in formatted_details:
    print('|',detail, " " * (max_length - len(detail)), '|')
print('-' * (max_length + 5))
