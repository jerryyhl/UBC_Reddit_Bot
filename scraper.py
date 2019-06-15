import requests
from bs4 import BeautifulSoup

course_schedule_page = requests.get("https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-all-departments")

soup = BeautifulSoup(course_schedule_page.text, "html.parser")

subject_table = soup.find(id="mainTable")

all_subjects = subject_table.find_all(class_=["section1", "section2"])

print(all_subjects)