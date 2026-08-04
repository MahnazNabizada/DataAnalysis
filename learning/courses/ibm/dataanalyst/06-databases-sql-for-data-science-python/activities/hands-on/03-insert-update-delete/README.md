# Practice exercises INSERT, UPDATE, and DELETE

## INSERT

### 1. Insert a new instructor record with id 4 for Sandip Saha who lives in Edmonton, CA into the "Instructor" table.

```sql
INSERT INTO Instructor(ins_id, lastname, firstname, city, country)
VALUES(4, 'Saha', 'Sandip', 'Edmonton', 'CA');
```

### 2. Insert two new instructor records into the "Instructor" table. First record with id 5 for John Doe who lives in Sydney, AU. Second record with id 6 for Jane Doe who lives in Dhaka, BD.

```sql
INSERT INTO Instructor(ins_id, lastname, firstname, city, country)
VALUES (5, 'Doe', 'John', 'Sydney', 'AU'), (6, 'Doe', 'Jane', 'Dhaka', 'BD');
```

### 3. Insert a new instructor record with id 7 for Antonio Cangiano who lives in Vancouver, CA into the "Instructor" table.

```sql
INSERT INTO Instructor(ins_id, lastname, firstname, city, country)
VALUES(7, 'Cangiano', 'Antonio', 'Vancouver', 'CA');
```

### 4. Insert two new instructor records into the "Instructor" table. First record with id 8 for Steve Ryan who lives in Barlby, GB. Second record with id 9 for Ramesh Sannareddy who lives in Hyderabad, IN.

```sql
INSERT INTO Instructor(ins_id, lastname, firstname, city, country)
VALUES(8, 'Ryan', 'Steve', 'Barlby', 'GB'), (9, 'Sannareddy', 'Ramesh', 'Hyderabad', 'IN');
```

## UPDATE

### 1. Update the city for Sandip to Toronto.

```sql
UPDATE Instructor
SET city='Toronto'
WHERE firstname="Sandip";
```

### 2. Update the city and country for Doe with id 5 to Dubai and AE respectively.

```sql
UPDATE Instructor
SET city='Dubai', country='AE'
WHERE ins_id=5;
```

### 3. Update the city of the instructor record to Markham whose id is 1.

```sql
UPDATE Instructor
SET city='Markham'
WHERE ins_id=1;
```

### 4. Update the city and country for Sandip with id 4 to Dhaka and BD respectively.

```sql
UPDATE Instructor
SET city='Dhaka', country='BD'
WHERE ins_id=4;
```

## DELETE

### 1. Remove the instructor record of Doe whose id is 6.

```sql
DELETE FROM instructor
WHERE ins_id = 6;
```

### 2. Remove the instructor record of Hima.

```sql
DELETE FROM instructor
WHERE firstname = 'Hima';
```
