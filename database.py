import sqlite3

def init_db():
    conn = sqlite3.connect('db/hireme.db')
    cursor = conn.cursor()

    # write your create table statements  of students here
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            usn TEXT PRIMARY KEY NOT NULL,
            student_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            college_name TEXT NOT NULL,
            branch TEXT NOT NULL,
            skills TEXT,
            email_id TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    # write your create table statements  of recruiters  here
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recruiters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            company TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email_id TEXT NOT NULL
        )
    ''')

    # write your create table statements  of jobs here
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_role TEXT NOT NULL,
            company TEXT NOT NULL,
            package TEXT NOT NULL,
            job_description TEXT NOT NULL
        )
    ''')


    # write your create table statements  of student_applications here
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usn TEXT NOT NULL,
            job_id INTEGER NOT NULL,
            status TEXT DEFAULT 'applied',
            FOREIGN KEY(usn) REFERENCES students(usn),
            FOREIGN KEY(job_id) REFERENCES jobs(id),
            UNIQUE(usn, job_id) -- Ensure a student can only apply once for a job
        )
    ''')


    
    
    # Insert dummy records
    cursor.execute('''
        INSERT OR IGNORE INTO students (usn, student_name, contact_number, college_name, branch, skills, email_id, password)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', ('USN123', 'John Doe', '1234567890', 'Sample College', 'Computer Science', 'Java, Python', 'john.doe@example.com', 'password123'))
    cursor.execute('''
        INSERT OR IGNORE INTO students (usn, student_name, contact_number, college_name, branch, skills, email_id, password)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', ('USN321', 'John Doe', '1234567890', 'Sample College', 'Computer Science', 'Java, Python', 'john.doe@example.com', 'password123'))

    # cursor.execute('''
    #     INSERT OR IGNORE INTO recruiters (username, password, first_name, last_name, company, phone_number, email_id)
    #     VALUES (?, ?, ?, ?, ?, ?, ?)
    # ''', ('recruiter1', 'password123', 'Jane', 'Doe', 'Sample Company', '0987654321', 'jane.doe@example.com'))

        # Delete jobs with specified IDs
    # cursor.execute('DELETE FROM jobs WHERE id = 8')
    # cursor.execute('DELETE FROM jobs WHERE id = 9')
    # cursor.execute('DELETE FROM jobs WHERE id = 10')
    # cursor.execute('DELETE FROM recruiters WHERE username = "recruiter1"')

    # jobsdata = cursor.execute('select * from jobs').fetchall()
    # appliedData = cursor.execute('select * from student_applications').fetchall()
    # studentData = cursor.execute('select * from students').fetchall()
    # print(jobsdata,appliedData,studentData)
    conn.commit()
    conn.close()
