**GitHub Project Description: Employee Information Display Script**

**Overview:**
This Python script, part of a GitHub project, serves as an Employee Information Display System. Leveraging the Faker module, Random module, and Tabulate library, it generates realistic employee data and presents it in a tabulated format. The script enables users to view essential details of employees, including their employee number, name, salary, address, mobile number, email, department, date of joining, and age. The project aims to provide a simple yet effective tool for showcasing randomly generated employee information.

**Features:**

1. **Randomly Generated Employee Data:**
   - Using both the Faker module and the Random module, the script generates diverse and realistic employee data, ensuring authenticity and variability in the information presented.

2. **Tabulated Display:**
   - Utilizing the Tabulate library, the script organizes the employee data into a clear and structured table format, enhancing readability and ease of interpretation for users.

3. **Comprehensive Employee Details:**
   - Users can access a comprehensive list of employee details, including employee number, name, salary, address, mobile number, email, department, date of joining, and age, facilitating a thorough understanding of each employee's profile.

**Usage:**
1. **Execute Script:**
   - Users can execute the script to generate and display a tabulated view of randomly generated employee information. The generated data encompasses various employee attributes, providing a rich and diverse dataset.

**Dependencies:**
- Faker module: A Python library for generating fake data, used to simulate employee information.
- Random module: A Python module for generating random numbers, used in conjunction with the Faker module to introduce variability in the generated data.
- Tabulate library: A Python library for formatting tabular data, employed to present the generated employee data in a structured manner.

**Note:** 
- This script focuses solely on displaying randomly generated employee information and does not include functionalities for modifying or deleting records.
- Users are encouraged to explore and contribute to the project, providing feedback, suggesting enhancements, or extending its functionality to suit their specific requirements.

---

This description emphasizes the usage of both the Faker module and Random module in generating simulated employee data, providing users with a comprehensive overview of the script's capabilities within the GitHub project.

Usage:
--------
Microsoft Windows [Version 10.0.19045.4291]
(c) Microsoft Corporation. All rights reserved.

E:\myfolder>py populate.py
Enter the number of records to insert into the database: 30 

30 Records displayed as follows:
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|   Employee Number | Employee Name      |   Employee Salary | Employee Address   |         Phone | Email
         | Department                                            | Joined     |   Age |
+===================+====================+===================+====================+===============+==============================+=======================================================+============+=======+
|              7018 | Madeline Logan     |             18241 | Torreshaven        | +916184507543 | vrose@example.com   
         | Personnel officer                                     | 2022-01-09 |    47 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              1695 | Glen Jennings      |             11578 | New Nathaniel      | +919070806879 | lopezanne@example.org        | Arts development officer                              | 2023-11-18 |    50 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              7231 | Corey Peterson     |             13321 | North Angela       | +919505911086 | heathjeremiah@example.org    | Energy manager                                        | 2021-11-02 |    47 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              1062 | Julie Stone        |             11995 | Port Kevin         | +916704063584 | barnettjoseph@example.org    | Administrator, education                              | 2022-01-13 |    53 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              6451 | Joseph Lopez       |             18936 | Petersshire        | +918722648806 | debbie42@example.net         | Accommodation manager                                 | 2022-01-29 |    26 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              8822 | Lisa Chandler      |             13956 | New Michaelland    | +919129584358 | luisjones@example.com        | Lawyer                                                | 2022-06-12 |    58 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              5988 | Alicia Warner      |             14666 | South Jennifer     | +918031417879 | jeffrey64@example.org        | Copy                                                  | 2023-04-08 |    41 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              2983 | Mr. Jose Hicks     |             11598 | Alyssamouth        | +919198213821 | julielynch@example.com       | Teacher, special educational needs                    | 2020-08-20 |    53 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              6515 | Amy Dominguez MD   |             18754 | Tammyborough       | +919103782024 | aimee48@example.org 
         | Archaeologist                                         | 2022-12-22 |    42 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              8367 | Jenny Flynn        |             15717 | Thomasburgh        | +917196160114 | hendersonmichael@example.com | Horticultural therapist                               | 2020-12-15 |    57 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              6431 | Jane Small         |             11489 | Jonesfurt          | +916244728422 | robert75@example.org         | Graphic designer                                      | 2022-10-22 |    31 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              9781 | Lisa Davis         |             17048 | Lake Elizabeth     | +917696172372 | whitephillip@example.org     | Accountant, chartered management                      | 2021-07-30 |    47 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              2062 | Julie Bond         |             12086 | Russellview        | +917135431008 | sullivanandrew@example.net   | Adult guidance worker                                 | 2022-09-22 |    31 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              8305 | Jennifer Jones     |             16249 | Jessicaborough     | +919935509531 | tbarrett@example.org         | Ophthalmologist                                       | 2023-06-18 |    48 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              1298 | Anthony Webb       |             14481 | New Robert         | +919877934053 | williamsvalerie@example.com  | Community development worker                          | 2020-07-21 |    54 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              2993 | Christopher Parker |             16603 | Martinezton        | +919850677571 | reidlori@example.net         | Chiropodist                                           | 2022-08-18 |    32 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              1584 | Julie Reynolds     |             16006 | Port Kristenburgh  | +919019431587 | djohnson@example.org         | Doctor, general practice                              | 2022-09-05 |    43 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              8024 | Paula Phillips     |             14248 | North Danielle     | +919991758840 | smithmatthew@example.com     | Pharmacist, hospital                                  | 2022-12-28 |    35 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              3689 | Jeremy Sutton      |             14200 | Lake Sylvia        | +918351193630 | kwang@example.org   
         | Scientist, biomedical                                 | 2023-03-12 |    29 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              7549 | Jenna Singh        |             10858 | South Yvonne       | +916633006414 | julie92@example.org 
         | Outdoor activities/education manager                  | 2022-06-26 |    45 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              7897 | Yvette Carter      |             11414 | Ericville          | +918223267409 | bli@example.com     
         | Conference centre manager                             | 2024-04-30 |    43 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              5815 | Mary Turner        |             18708 | East Darylside     | +918734990359 | amanda44@example.org         | Legal executive                                       | 2020-12-05 |    50 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              8039 | Kenneth Riley      |             13168 | West Stephanie     | +916734130209 | smithtammy@example.com       | Armed forces logistics/support/administrative officer | 2020-11-28 |    59 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              2290 | Mark Barber PhD    |             12821 | South Melissaview  | +916742973162 | scott14@example.org 
         | Hydrogeologist                                        | 2024-01-17 |    37 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              1800 | Deborah Patton     |             10214 | West Allen         | +918874613716 | jillwilson@example.org       | Scientific laboratory technician                      | 2022-12-28 |    49 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              5138 | David Cooper       |             18150 | West Michelle      | +917124865988 | amy88@example.com   
         | Tour manager                                          | 2021-06-10 |    35 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              7176 | Ashlee Huber       |             19672 | North Amymouth     | +917983084422 | kimhannah@example.org        | Research scientist (medical)                          | 2021-07-28 |    28 |
+-------------------+--------------------+-------------------+--------------------+---------------+------------------------------+-------------------------------------------------------+------------+-------+
|              4830 | Kristina Evans     |             13392 | Kariville          | +918018527191 | rgutierrez@example.com       | Legal secretary                                       | 2020-09-14 |    42 |
+-------------------+--------------------+-------------------+--------------------+---------------+---------------------

E:\myfolder>py populate.py
Enter the number of records to insert into the database: 10

10 Records displayed as follows:
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+
|   Employee Number | Employee Name      |   Employee Salary | Employee Address   |         Phone | Email                       | Department                            | Joined     |   Age |
+===================+====================+===================+====================+===============+=============================+=======================================+============+=======+
|              6350 | William Green      |             19131 | South Brandonport  | +917658096311 | istein@example.net          | Scientist, research (life sciences)   | 2021-04-10 |    44 |
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+
|              2680 | John Hernandez     |             11080 | West Jason         | +916865023542 | qbrown@example.org          | Accountant, chartered                 | 2021-07-25 |    37 |
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+
|              4553 | Christopher French |             18026 | West Alexismouth   | +917555027506 | patrickjohnson@example.net  | Academic librarian                    | 2020-11-11 |    46 |
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+
|              9016 | Joshua Meyer       |             16716 | Lake Benjaminmouth | +917957387239 | marthamorgan@example.org    | Occupational psychologist             | 2022-04-27 |    58 |
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+
|              7775 | Kayla Gutierrez    |             19065 | Brooksburgh        | +916197570519 | todd70@example.com          | Broadcast journalist                  | 2020-05-06 |    23 |
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+
|              9087 | Michelle Sanchez   |             18985 | Victoriamouth      | +916201580498 | cooperjoseph@example.com    | Emergency planning/management officer | 2023-08-21 |    21 |
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+
|              8004 | Amy Montgomery     |             12980 | South Kenneth      | +919711104959 | allendanielle@example.org   | Banker                                | 2020-08-06 |    35 |
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+
|              5889 | John Shaw          |             15412 | Parkerhaven        | +917321802572 | smunoz@example.org          | Armed forces technical officer        | 2021-05-21 |    35 |
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+
|              1146 | Tammy Hart         |             13510 | Kathleenburgh      | +919483667715 | johnanderson@example.com    | Chartered loss adjuster               | 2022-12-21 |    54 |
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+
|              8434 | Carla Hunt         |             18148 | Kennethstad        | +916197692914 | cassiehenderson@example.com | Engineer, energy                      | 2020-11-08 |    46 |
+-------------------+--------------------+-------------------+--------------------+---------------+-----------------------------+---------------------------------------+------------+-------+

E:\myfolder>
