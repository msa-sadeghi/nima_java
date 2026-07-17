import sqlite3

connection = sqlite3.connect("task_manager_db.db")
cursor = connection.cursor()
query = """
DELETE FROM notes WHERE id = 2
"""
cursor.execute(query)
connection.commit()

