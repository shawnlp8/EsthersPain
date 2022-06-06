# ---------- Imports ----------
import sqlite3


# ------------ Variables ------------ 
connection = sqlite3.connect("scriptingdb.sqlite")
c = connection.cursor()

# -----------------------------------  SQL ----------------------------------- 
print(connection.total_changes)

c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='master_table'")

if c.fetchone()[0] == 1:
	c.execute("DROP TABLE master_table")

c.execute("CREATE TABLE master_table (date TEXT, first_name TEXT, last_name TEXT, full_name TEXT)")

c.execute("CREATE TABLE modified_table (full_name TEXT, dec_2020 TEXT, jan_2021 TEXT, feb_2021 TEXT, mar_2021 TEXT, apr_2021 TEXT, may_2021 TEXT, jun_2020 TEXT, jul_2021 TEXT, aug_2021 TEXT, sep_2021 TEXT, oct_2021 TEXT)")

c.close()