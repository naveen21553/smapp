Assumptions - 

1. Have not normalized the student table - possible multi-attribute column 'books', assuming only one book is read by a student
2. changed school and book name to school_id and book_id in student_table
3. in search function using both id and name to verify the results, both id and name is checked


Bug - 
1. Added the given records with help of python script and pandas which re-writes the original schema and hence the auto-increment student_id is broken  


Django admin credentials - 
username - admin
password - django@123