import sqlite3


connection = sqlite3.connect(____)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""
    SELECT
""")

rows = cursor.fetchall()

{% for flight in flights %}
    {{ flight.duration }}
{% endfor %}