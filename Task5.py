import csv
def write_csv(info_list):
    with open("Student_info.csv",'a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact Number","Email id"])
        writer.writerow(info_list)

if _name_ == '_main_':
    condition=True
    student_num=1
    while(condition):
        student_info=input((f"Enter information for student {student_num} in the following format (Name Age Contact_Number Email_id) \n"))
            
        student_info_list=student_info.split()
        print(f"The entered information is:\nName:{student_info_list[0]}\nAge:{student_info_list[1]}\nContact Number:{student_info_list[2]}\nEmail id:{student_info_list[3]}")
        choice_check=input(("Is the entered information correct? Enter Yes or No \n"))
        if choice_check=='Yes':
            write_csv(student_info_list)
            condition_check=input("Do you want to enter information for another student?Enter Yes/No \n")
            if condition_check=='Yes':
                condition=True
                student_num+=1
            elif condition_check=='No':
                condition=False
            elif choice_check=='No':
                print("Please re enter the values")
