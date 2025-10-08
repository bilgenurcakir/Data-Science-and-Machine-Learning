import os
import sqlite3



def create_database():
    if os.path.exists("student.db"): ##bilgisayarımda varsa(her yerde çalışabilmesi için os)
        os.remove("student.db") # sil

    conn = sqlite3.connect("student.db") # bağlantıyı kurar
    cursor=conn.cursor()  # komutları çalıştırmamıza yarar
    return conn,cursor

def create_tables(cursor):

    cursor.execute('''
    CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    age INTEGER,
    email VARCHAR UNIQUE,
    city TEXT) 
    ''')


    cursor.execute('''
    CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    course name VARCHAR(30) NOT NULL,
    instructor VARCHAR,
    credits INTEGER ) 
    ''')







def insert_sample_data(cursor):

    students=[
        (1,'Alice Jhonson',20,'alice@gmail.com','New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]
    cursor.executemany("INSERT INTO students VALUES (?,?,?,?,?)",students )

    courses=[
        (1,'Python Programming','Dr. Anderson',3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2),

    ]
    cursor.executemany("INSERT INTO courses VALUES(?,?,?,?)",courses)

    print("sample data inserted successfully")



def basic_sql_operations(cursor):

    #SELECT all
    print("\n-----------select all---------")
    cursor.execute("SELECT * FROM students")
    records=cursor.fetchall()
    print(records) #tamamını bir liste halinde göster
    for row in records:
        #print(row)
        print(f"ID:{row[0]} ,Name:{row[1]} ,Age:{row[2]} ,email:{row[3]} ,City{row[4]}")

    #SELECT columns
    print("\n-----------select columns---------")
    cursor.execute("SELECT name,age FROM students")
    records=cursor.fetchall()
    print(records)

    # WHERE clause (filtreleme yapmak)
    print("\n-----------where clause---------")
    cursor.execute("SELECT * FROM students WHERE age= 20")
    records=cursor.fetchall()
    print(records)


    # WHERE with string
    print("\n-----------where with string---------")
    cursor.execute("SELECT * FROM students WHERE  city= 'New York' ")
    records=cursor.fetchall()
    print(records)

    #ORDER BY
    print("\n-----------order by---------")
    cursor.execute("SELECT * FROM students ORDER BY age")
    records=cursor.fetchall()
    print(records)

    #LIMIT
    print("\n-----------limit---------")
    cursor.execute("SELECT * FROM students LIMIT 3") #ilk üçü getir
    records=cursor.fetchall()
    print(records)
    




def sql_update_delete_insert_oparations(conn,cursor):
    #INSERT
    cursor.execute("INSERT INTO students VALUES (6,'Frank Miller',23,'frank@gmail.com','Miami')")
    conn.commit() #  conn.commit(), veritabanında yapılan geçici değişiklikleri kalıcı hale getirmek için kullanılır.


    #UPDATE
    cursor.execute("UPDATE students SET age=24 WHERE id=6")
    conn.commit()

    #DELETE
    cursor.execute("DELETE FROM students WHERE id=6")
    conn.commit()


def aggregate_functions(cursor):
    # COUNT
    print("\n----------aggregate func. COUNT-------------")
    cursor.execute("SELECT COUNT(*) FROM students")
    result=cursor.fetchall() #fetchall liste verir, tuple şeklinde ,fetchone() dersek sadece bir tane tuple verir
    print(result[0][0])

    #AVERAGE
    print("\n----------aggregate func. AVERAGE-------------")
    cursor.execute("SELECT AVG(age) FROM students")
    result=cursor.fetchone()
    print(result[0])

    #MAX_MİN
    print("\n----------aggregate func. MAX-MİN-------------")
    cursor.execute("SELECT MAX(age),MIN(age) FROM students ")
    result=cursor.fetchone()
    max_age, min_age= result
    print(max_age)
    print(min_age)

    #GROUP BY
    print("\n----------aggregate func. GROUP BY-------------")
    cursor.execute("SELECT city, COUNT(*) FROM students GROUP BY city")
    result=cursor.fetchall()
    print(result)





def main():
  conn,cursor=create_database()

  try:
    create_tables(cursor)
    insert_sample_data(cursor)
    basic_sql_operations(cursor)
    sql_update_delete_insert_oparations(conn,cursor)
    aggregate_functions(cursor)
    conn.commit() # cursor'ın yaptıgı isleri uygula

  except sqlite3.Error as e:
      print(e)

  finally:
      conn.close()



if __name__=="__main__":
    main()