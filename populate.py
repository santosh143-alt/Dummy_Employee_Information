from faker import Faker
from random import randint
from tabulate import tabulate

faker = Faker()

def phonenumbergen(): 
	d1=randint(6,9)
	num="+91"
	num=num+str(d1) 
	for i in range(9): 
		num=num+str(randint(0,9)) 
	return num

def populate(n): 
    records = []
    for i in range(n): 
        feno = randint(1001, 9999) 
        fename = faker.name() 
        fesal = randint(10000, 20000) 
        feaddr = faker.city()
        fephone = phonenumbergen()
        feemail = faker.email()
        fedept = faker.job()
        fejoined = faker.date_this_decade()
        feage = randint(20, 60)
        records.append((feno, fename, fesal, feaddr, fephone, feemail, fedept, fejoined, feage)) #This script displays employee number, name, salary, address, mobile number, email, department, date of joning, age
    return records

n = int(input("Enter the number of records to insert into the database: "))
records = populate(n)

print(f"\n{n} Records displayed as follows:")
print(tabulate(records, headers=['Employee Number', 'Employee Name', 'Employee Salary', 'Employee Address', 'Phone', 'Email', 'Department', 'Joined', 'Age'], tablefmt='grid'))
