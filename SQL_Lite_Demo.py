import sqlite3
from employee import Employee

# conn = sqlite3.connect('employee.db')
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
			 first text,
			 last text,
			 pay integer
			)""")


def insert_emp(emp):
	with conn:
		c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
		return c.fetchall()


def get_emps_by_name(lastname):
	c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})


def update_pay(emp, pay):
	with conn:
		c.execute("""UPDATE employees SET pay = :pay
					WHERE first =:first AND last =:last""", {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
	with conn:
		c.execute("DELETE from employees WHERE first= :first AND last= :last", {'first': emp.first, 'last': emp.last})


emp_1 = Employee('Manju', 'Subramanyam', 90000)
emp_2 = Employee('Harshan', 'Subramanyam', 100000)

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)

c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))

conn.commit()

c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})

conn.commit()

c.execute("SELECT * FROM employees WHERE last='Gopala'")

c.execute("SELECT * FROM employees WHERE last=?", ('Gopala',))
print(c.fetchall())

c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Subramanyam'})
print(c.fetchall())

#print(c.fetchone())
# print(c.fetchall())

conn.commit()

conn.close()