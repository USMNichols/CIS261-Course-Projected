#Brandon Nichols
#CIS261 Jay Gaines Course Project


def time_card():
    Name = input("Please input employee name\n")
    print(Name + " TimeCard")
 
time_card()

def total_hours():
   Total_Hours = int(input("Total Amount of hours worked?\n"))
   for Total_Hours in range(0,1):
      return Total_Hours

total_hours()

def hourly_rate():
    Hourly_Rate = int(input("Hourly Rate\n"))
    for Hourly_Rate in range(0,1):
       return Hourly_Rate

hourly_rate()

def employee_incometax():
    Employee_incometax = int(input("Employee Income Tax Deduction\n"))
    for Employee_incometax in range(0,1):
        return Employee_incometax
    print(Employee_incometax)

employee_incometax()

def employee_database():
    print("Employee Database\n has been Updated have a greatday")

employee_database()



if __name__=="__main__":
    time_card()
    total_hours()
    hourly_rate()
    employee_incometax()
    employee_database()




