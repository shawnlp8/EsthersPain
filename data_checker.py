# ---------- Imports ----------
import sqlite3

# ------------ Variables ------------ 
connection = sqlite3.connect("scriptingdb.sqlite")
c = connection.cursor()
dictionary = {}


# ------------ Helper Functions ------------
def ConvertToDict(tup, di):
    for a, b, c, d in tup:
        di.setdefault(a, []).append(b)
    return di

# -----------------------------------  Display Original Tables ----------------------------------- 

print("-------------- Master Table --------------\n")
master_temp_list = []
rows = c.execute("SELECT * FROM master_table").fetchall()
for r in rows:
    print('master_full_name:' + r[3].lower().replace(" ", "") + ' master_date: ' + r[0])
    master_temp_list.append(r)

print("-------------- Modified Table --------------\n")
modified_temp_list = []
rows = c.execute("SELECT * FROM modified_table").fetchall()
for r in rows:
    print('modified_full_name:' + r[0].lower().replace(" ", "") + ' modified_date: ' + r[5])
    modified_temp_list.append(r)

counter = 0


# -----------------------------------  Data Filtering and Cross Checking ----------------------------------- 
for i in master_temp_list:
    for j in modified_temp_list:
        if (i[3].lower().replace(" ", "") == j[0].lower().replace(" ", "")) and (i[0] == 'apr_2021'):
            counter += 1
            print('!MATCHED! ('+str(counter)+') i: '+ i[3].lower().replace(" ", "") +'\tj: ' + j[0].lower().replace(" ", ""))
            update_statement = "UPDATE modified_table SET apr_2021 = '1' WHERE full_name = '" + j[0] + "';"
            print(update_statement)
            c.execute(update_statement)
            connection.commit()