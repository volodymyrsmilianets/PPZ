import sqlite3


def read_database():
    try:
        # Підключення до бази даних
        conn = sqlite3.connect("trains.db")
        cursor = conn.cursor()

        # Отримання списку таблиць у базі
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        print("Список таблиць у базі даних:")
        for table in tables:
            print(table[0])

            # Отримання всіх даних із таблиці
            cursor.execute(f"SELECT * FROM {table[0]}")
            rows = cursor.fetchall()

            print(f"\nДані з таблиці {table[0]}:")
            for row in rows:
                print(row)

    except sqlite3.Error as e:
        print("Помилка при роботі з базою даних:", e)

    finally:
        # Закриття з'єднання
        conn.close()
        print("З'єднання з базою закрито.")


if __name__ == "__main__":
    read_database()
