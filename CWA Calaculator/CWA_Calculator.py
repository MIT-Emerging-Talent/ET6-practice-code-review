class Student:
    
    
  def __init__(self, name, index_number,reference_number, email, age, gender, program_of_study, year_of_study, university_name, num_of_courses):
        self.name = name
        self.age = age
        self.index_number = index_number
        self.reference_number = reference_number
        self.email = email
        self.gender = gender
        self.program_of_study = program_of_study
        self.year_of_study = year_of_study
        self.university_name = university_name
        self.num_of_courses = num_of_courses
        self.courses = []
        self.CWA = 0
        
def get_grade(score):
  
         
  if 70 <= score <= 100:
    grade = "A"
  elif 60 <= score < 70:
    grade = "B"
  elif 50 <= score < 60:
    grade = "C"
  elif 40 <= score < 50:
    grade = "D"
  elif 0 <= score < 40:
    grade = "F"
  else:
          return "Invalid score"
  return grade    


def calculate_cwa(courses):
        
        grade_points = 0
        credits_obtained = 0
        for course in courses:
         grade_points += course['score'] * course['credit_hours']
        credits_obtained += course['credit_hours']
        
        if grade_points == 0:
          return 0
    
        return grade_points/credits_obtained



def collect_student_data():
        
    student_data = {}
        student_data['name'] = input("Enter the name of the student: ")
        student_data['age'] = input("Enter the age of the student: ")
        student_data['index_number'] = input("Enter the index number: ")
        student_data['reference_number'] = input("Enter the reference number: ")
        student_data['email'] = input("Enter the student email")
        student_data['gender'] = input("Enter the gender of the student: ")
        student_data['program_of_study'] = input("Enter the program of study: ")
        student_data['year_of_study'] = input("Enter the year of study: ")
        student_data['university_name']= input("Enter the University name")

        num_of_courses = int(input("Enter the number of courses: "))
        courses = []

        for _ in range(num_of_courses):
          course_name = input("Enter the course name: ")
          credit_hours = int(input(f"Enter the credit hours for {course_name}: "))
          score = float(input(f"Enter the score for {course_name}: "))
          grade = get_grade(score)
        
        
        courses.append({
            'name': course_name,
            'credit_hours': credit_hours,
            'score': score,
            'grade': grade,
        })

        student_data['courses'] = courses
        student_data['CWA'] = calculate_cwa(courses)

        return student_data   
  
student = collect_student_data():


print("\nStudent Details:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"index number: {student['index_number']}")
print(f"reference number: {student['reference_number']}")
print(f"email: {student['email']}")
print(f"Gender: {student['gender']}")
print(f"Program of Study: {student['program_of_study']}")
print(f"year of study: {student['year_of_study']}")
print(f"university name:{student['university_name']}")

print(f"CWA: {student['CWA']:.2f}")


print("\nCourse Details:")
for course in student['courses']:
    print(f"Course Name: {course['name']}")
    print(f"Credit Hours: {course['credit_hours']}")
    print(f"Score: {course['score']}")
    print(f"Grade: {course['grade']}")
    print("-" * 30)   