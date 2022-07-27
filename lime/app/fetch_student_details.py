import csv



from student import Student


class FetchStudentDetails:
    student_list = None
    headers = None

    def __init__(self):
        self.headers = []
        self.student_list = []

    @staticmethod
    def clean_input(row):
        """
        Clean and sanitize the input so that it does not contain leading and trailing spaces
        """
        return [r.strip() for r in row]

    @staticmethod
    def map_csv_to_class(row):
        """
        Convert the input row into a Student class
        """
        return Student(*row)

    def get_data(self, file_name="./app/data/student_details.csv"):
        """
        Fetch the data from the given csv file and construct the list of Student objects
        """
        with open(file_name, newline="") as _file:
            reader = csv.reader(
                _file,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_ALL,
                skipinitialspace=True,
            )
            # set here self.headers (first row)
            self.headers=next(reader)
            
            # set here self.student_list consider using clean_input() and map_csv_to_class()
            for row in reader:
                self.student_list.append(self.map_csv_to_class(self.clean_input(row)))

            # print(self.student_list[0].average_score)
        return self.student_list

    def get_super_student(self):
        """
        Get super student
        """
        self.super_student=""
        pointsmax=0
        
        for i in range (len(self.student_list)):
            points=0
            for x in range(len(self.student_list[i].subjects)):
                if self.student_list[i].subjects[x:].startswith("computer science"): points+=5
                if self.student_list[i].subjects[x:].startswith("maths"): points+=10


            if self.student_list[i].name.startswith("y"): points+=15
            if int(self.student_list[i].id)%2==0: points+=20
            if self.student_list[i].grade=="A+": points+=25


            if pointsmax<points: 
                self.super_student=self.student_list[i].name
                pointsmax=points
            # print(points)
        
        return self.super_student

    def get_attendance(self, attendance_file_name="./app/data/attendance.csv"):
        """
        Fetch data from given csv file and update students attendance
        """
        with open(attendance_file_name, newline="") as _file:
            reader = csv.reader(
                _file,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_ALL,
                skipinitialspace=True,
            )
            for row in reader:
                    n=0
                    for i in row:
                        
                        if n==0:nr=int(i)
                        else:
                            if str(i)=="Y":
                                
                                for j in range(len(self.student_list)):
                                    if int(self.student_list[j].id)==nr:
                                        self.student_list[j].attendance+=1
                                        break
                        n+=1
        
    

d= FetchStudentDetails()
d.get_data()
print(d.get_super_student())
d.get_attendance()
for i in range (len(d.student_list)):
    print(d.student_list[i].attendance)
