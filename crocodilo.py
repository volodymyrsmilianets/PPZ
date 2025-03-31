import sqlite3

# Підключення до бази даних (створиться, якщо її нема)
conn = sqlite3.connect("trains.db")
cursor = conn.cursor()

# Створення таблиці, якщо вона не існує
cursor.execute("""
CREATE TABLE IF NOT EXISTS trains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    destination TEXT
)
""")

# Додавання тестових записів
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Express 101', 'Rivne')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Fast 202', 'Dnipro')")

# Збереження змін
conn.commit()
conn.close()

print("✅ Дані успішно додані!")