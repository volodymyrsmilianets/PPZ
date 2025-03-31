import sqlite3


def create_database():
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Articles (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_article():
    title = input("Введіть заголовок статті: ")
    content = input("Введіть вміст статті: ")
    author = input("Введіть автора статті: ")

    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Articles (title, content, author) VALUES (?, ?, ?)", (title, content, author))
        conn.commit()
        print("Стаття успішно додана!")
    except sqlite3.IntegrityError:
        print("Помилка: автор має бути унікальним!")
    conn.close()


def delete_article():
    article_id = int(input("Введіть ID статті для видалення: "))
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Articles WHERE id = ?", (article_id,))
    conn.commit()
    conn.close()
    print("Стаття видалена!")


def view_article():
    article_id = int(input("Введіть ID статті для перегляду: "))
    conn = sqlite3.connect("articles.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Articles WHERE id = ?", (article_id,))
    article = cursor.fetchone()
    conn.close()
    if article:
        print(f"ID: {article[0]}\nTitle: {article[1]}\nContent: {article[2]}\nAuthor: {article[3]}")
    else:
        print("Стаття не знайдена!")


# Приклад використання
if __name__ == "__main__":
    create_database()
    while True:
        print("\nМеню:")
        print("1. Додати статтю")
        print("2. Переглянути статтю")
        print("3. Видалити статтю")
        print("4. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            add_article()
        elif choice == "2":
            view_article()
        elif choice == "3":
            delete_article()
        elif choice == "4":
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")
