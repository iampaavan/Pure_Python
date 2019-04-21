import datetime
"""Write a Python program to display the examination schedule. (extract the date from exam_st_date)"""

exam_st_date = (11, 12, 2014)
print(f'***********************************************************')
print("The examination will start from : %i / %i / %i" %exam_st_date)
print(f'***********************************************************')

today = datetime.datetime.today()
c = today.strftime("%d-%m-%Y %H:%M:%S")
print(f"Today's Date and Current Time: {c}")
print(f'***********************************************************')
