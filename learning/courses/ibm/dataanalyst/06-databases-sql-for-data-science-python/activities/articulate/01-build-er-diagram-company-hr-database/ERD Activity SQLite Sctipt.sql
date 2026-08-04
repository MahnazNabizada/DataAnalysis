-- Department
CREATE TABLE Department (
	Department_ID INTEGER PRIMARY KEY,
	Code TEXT UNIQUE NOT NULL,
	Name TEXT NOT NULL
);

-- Employee
CREATE TABLE Employee ( 
    Employee_ID INTEGER PRIMARY KEY, 
    First_Name TEXT NOT NULL, 
    Last_Name TEXT NOT NULL, 
    Email TEXT UNIQUE NOT NULL, 
    Phone_Number TEXT UNIQUE, 
    Job_Title TEXT NOT NULL, 
    Salary REAL CHECK(Salary > 0), 
    Hire_Date DATE DEFAULT CURRENT_DATE, 
    Employment_Status TEXT DEFAULT 'Active'  
        CHECK(Employment_Status IN ('Active', 'Inactive')), 
    Department_ID INTEGER, 
    Manager_ID INTEGER, 

    FOREIGN KEY (Department_ID)  
        REFERENCES Department(Department_ID), 
    FOREIGN KEY (Manager_ID)  
       REFERENCES Employee(Employee_ID) 
); 

-- Project
CREATE TABLE Project (
	Project_ID INTEGER PRIMARY KEY,
	Name TEXT UNIQUE,
	Budget REAL CHECK(Budget > 0)
);

-- Employee Project Assignments
CREATE TABLE Employee_Project (
	Employee_ID INTEGER NOT NULL,
	Project_ID INTEGER NOT NULL,	
	Hours_Worked REAL NOT NULL CHECK (Hours_Worked >=0),
	
	PRIMARY KEY (Employee_ID, Project_ID),	
	FOREIGN KEY (Employee_ID)
		REFERENCES Employee(Employee_ID),	
	FOREIGN KEY (Project_ID)
		REFERENCES Project(Project_ID)
);

-- Insert 3 Departmens
INSERT INTO Department values (1,'HR','Human Resources');
INSERT INTO Department values (2,'IT','Information Technology');
INSERT INTO Department values (3,'CS','Career Services');

-- Or you can add at once like

-- INSERT INTO Department values 
-- 	(1,'IT', 'Information Technology'),
-- 	(2,'HR', 'Human Resources'),
-- 	(3,'CS', 'Career Services'); 

 -- Insert 5 Employees
INSERT INTO Employee values (1,'Belkacem','Belferar','belkacem.belferar@npowercanada.ca','(111)111-1111','Manager Program Coordinator',180000,'01-01-2016','Active',3,NULL);
INSERT INTO Employee values (2,'Geethu','Sodhi','geetu.sodhi@npowercanada.ca','(222)222-2222','Instructor',120000,'01-01-2018','Active',2,1);
INSERT INTO Employee values (3,'Shivan','Pillay','shivan.pillay@npowercanada.ca','(333)333-3333','Instructor',120000,'03-28-2024','Active',2,1);
INSERT INTO Employee values (4,'Mahwish','Nasrullah','mahwish.nasrullah@npowercanada.ca','(444)444-4444','Career Coordinator',90000,'09-04-2019','Active',3,1);
INSERT INTO Employee values (5,'Roop','Fatima','roop.fatima@npowercanada.ca','(555)555-5555','Career Coordinator',90000,'06-15-2017','Active',3,1);
INSERT INTO Employee values (6,'Yvonne','Oji','yvonne.oji@npowercanada.ca','(666)666-6666','Career Coordinator',90000,'06-15-2017','Active',3,1);

-- Insert 3 Projects
INSERT INTO Project values (1, 'JUNIOR IT ANALYST', 50000);
INSERT INTO Project values (2, 'AI & DATA ANALYTICS', 60000);
INSERT INTO Project values (3, 'NETWORK SECURITY', 45000);

-- Employees Assignments 
INSERT INTO Employee_Project values (2,2,600);
INSERT INTO Employee_Project values (4,2,450);
INSERT INTO Employee_Project values (5,2,450);

-- Retireve Departments and Managers
SELECT 
	d.Department_ID, 
	d.Name as Department_Name,
	m.Employee_ID as Manager_ID,
	m.First_Name || ' ' || m.Last_Name as Manager_Name
FROM Department d LEFT JOIN Employee m 
	ON d.Department_ID = m.Department_ID
	AND m.Employee_ID IN ( 
		SELECT DISTINCT Manager_ID
		FROM Employee
		WHERE Manager_ID IS NOT NULL
	);
	

