# comma-separated values

import csv


def write_info(info_list):
    with open('Student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(['Name', 'Age', 'Contact No.', 'E-mail ID'])

        writer.writerow(info_list)


if __name__ == '__main__':
    Condition = True
    Student_No = 1

    while Condition:
        Student_info = input('Enter Info for Student {} [Name Age Contact_No. E-mail_ID]: '.format(Student_No))

        Student_info_List = Student_info.split(' ')

        print('\nEntered Info is-\n> Name: {}\n> Age: {}\n> Contact No.: {}\n> E-mail ID: {} '
              .format(Student_info_List[0], Student_info_List[1], Student_info_List[2], Student_info_List[3]))

        Choice_check = input('Is the Entered Info correct? (Y/N) ')

        if Choice_check.upper() == 'Y':
            write_info(Student_info_List)

            Condition_Check = input('Enter info for another student(Y/N): ')
            if Condition_Check.upper() == 'Y':
                Condition = True
                Student_No = Student_No + 1
            elif Condition_Check.upper() == 'N':
                Condition = False
                print('Thank You ! ! ! ')
            else:
                print('Invalid Value! ')
        elif Choice_check.upper() == 'N':
            print('\nPlease Re-Enter the Info!!! ')
