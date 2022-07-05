CREATE TABLE Authors(
    LastName VARCHAR2(25),
    FirstName VARCHAR2(25),
    ID Number(4) Primary KEY,
    Birthdate VARCHAR2(30)
);

CREATE TABLE Publishers(
    Name VARCHAR2(40),
    PubNumber Number(4) Primary KEY,
    Address VARCHAR2(75)
);

CREATE TABLE Books(
    ISBN VARCHAR2(25) Primary KEY,
    Title VARCHAR2(50),
    PubID Number(4),
    
    CONSTRAINT Publisher_FK
        Foreign KEY(PubID)
        REFERENCES Publishers(PubNumber)
);

CREATE TABLE Dual_Authors(
    AuthID Number(4),
    ISBNNUM VARCHAR2(25),
    AuthRank Number(4),
    
    CONSTRAINT Author2_FK
        Foreign KEY(AuthID)
        REFERENCES Authors(ID),
    
    CONSTRAINT Publisher2_FK
        Foreign KEY(ISBNNUM)
        REFERENCES Books(ISBN)
);
    
    
    
INSERT INTO Authors VALUES('King', 'Stephen', 2, 'September 9 1947');
INSERT INTO Authors VALUES('Asimov', 'Isaac', 4, 'January 2 1921');
INSERT INTO Authors VALUES('Verne', 'Jules', 7, 'February 8 1828');
INSERT INTO Authors VALUES('Rowling', 'Joanne', 37, 'July 31 1965');

INSERT INTO Publishers VALUES('Bloomsbury Publishing', 17, 'London Borough of Camden');
INSERT INTO Publishers VALUES('Arthur A Levine Books', 18, 'New York City');

INSERT INTO Books VALUES('1111-111','Databases from Outer Space',17);
INSERT INTO Books VALUES('2222-232','Revenge of SQL',17);
INSERT INTO Books VALUES('3333-323','The Night of the Living Databases',18);

INSERT INTO Dual_Authors VALUES(2, '1111-111', 1);
INSERT INTO Dual_Authors VALUES(4, '1111-111', 2);
INSERT INTO Dual_Authors VALUES(4, '2222-232', 1);
INSERT INTO Dual_Authors VALUES(7, '2222-232', 1);
INSERT INTO Dual_Authors VALUES(37, '3333-323', 1);
INSERT INTO Dual_Authors VALUES(2, '3333-323', 2);

SELECT *FROM Authors;
SELECT * FROM Publishers;
SELECT * FROM Books;
Select * FROM Dual_Authors;


CREATE TABLE Students(
    StudentID Number(7) Primary KEY,
    FirstName VarChar2(15),
    LastName VarChar2(15),
    DOB VarChar2(25),
    Telephone VarChar2(10),
    AdvisorID Number(4),
    
    Constraint Advisor_FK
        Foreign Key(AdvisorID)
        REFERENCES Advisor(ID)
);

CREATE TABLE Advisor(
    ID Number(4) Primary Key,
    Name VARCHAR2(30),
    ResearchArea VARCHAR2(25),
    Department VarChar2(25),
    
    Constraint Dept_FK
        Foreign Key(Department)
        REFERENCES Departments(Name)
);

CREATE TABLE Departments(
    Name VARCHAR2(25) Primary KEY,
    Chair VARCHAR2(45),
    Endowment Number(15)
);
