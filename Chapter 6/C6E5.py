import json

def get_student_details():
    name = input("Enter student name: ")
    student_id = int(input("Enter student ID: "))
    course = input("Enter student course: ")
    return {"Name": name, "ID": student_id, "course": course}

def write_to_json(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)

def read_from_json(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
        print("\nDetails of the Student are")
        print(f"Name: {data['Name']}")
        print(f"ID: {data['ID']}")
        print(f"course: {data['course']}")
        if 'CourseDetails' in data:
            print(f"Group: {data['CourseDetails']['Group']}")
            print(f"Year: {data['CourseDetails']['Year']}")

student_data = get_student_details()
write_to_json('StudentJson.json', student_data)

read_from_json('StudentJson.json')

with open('StudentJson.json', 'r') as file:
    existing_data = json.load(file)

existing_data['CourseDetails'] = {
    "Group": "A",
    "Year": 2
}

write_to_json('StudentJson.json', existing_data)

read_from_json('StudentJson.json')
