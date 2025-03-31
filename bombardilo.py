import sqlite3

# Підключення до бази
conn = sqlite3.connect("trains.db")
cursor = conn.cursor()

# Отримання списку таблиць
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📌 Таблиці у базі даних:")
for table in tables:
    print(table[0])

print("\n🔍 Перевіряємо дані у таблиці 'trains':")

# Зчитування всіх даних із таблиці trains
cursor.execute("SELECT * FROM trains")
rows = cursor.fetchall()

if rows:
    print("📝 Дані у таблиці:")
    for row in rows:
        print(row)
else:
    print("⚠️ Таблиця порожня!")

# Закриття з'єднання
conn.close()