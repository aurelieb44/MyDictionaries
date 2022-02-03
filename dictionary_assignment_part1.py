room_no = {
    "CS101": "3004",
    "CS102": "4501",
    "CS103": "6755",
    "NT110": "1244",
    "CM241": "1411",
}

instructor = {
    "CS101": "Haynes",
    "CS102": "Alvarado",
    "CS103": "Rich",
    "NT110": "Burke",
    "CM241": "Lee",
}

meeting_time = {
    "CS101": "8:00am",
    "CS102": "9:00am",
    "CS103": "10:00am",
    "NT110": "11:00am",
    "CM241": "1:00pm",
}

course_info = input("Please enter a course number: ")

while course_info not in room_no:
    print(
        "The course number entered doesn't exist, please enter a valid course number. "
    )
    course_info = input("Please enter a course number: ")

print("Room number: ", room_no[course_info])
print("Instructor: ", instructor[course_info])
print("Meeting Time: ", meeting_time[course_info])
