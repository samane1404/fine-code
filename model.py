import sqlite3

class ToDoModel:
    def __init__(self, db_name="todos.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER,
                                task TEXT NOT NULL,
                                status TEXT DEFAULT 'Pending',
                                FOREIGN KEY(user_id) REFERENCES users(user_id))''')
        self.conn.commit()

    def add_user(self, username):
        self.cursor.execute('INSERT INTO users (username) VALUES (?)', (username,))
        self.conn.commit()

    def get_user_id(self, username):
        self.cursor.execute('SELECT user_id FROM users WHERE username = ?', (username,))
        user = self.cursor.fetchone()
        return user[0] if user else None

    def add_task(self, user_id, task):
        self.cursor.execute('INSERT INTO tasks (user_id, task) VALUES (?, ?)', (user_id, task))
        self.conn.commit()

    def get_tasks(self, user_id):
        self.cursor.execute('SELECT task_id, task, status FROM tasks WHERE user_id = ?', (user_id,))
        return self.cursor.fetchall()

    def update_task(self, task_id, new_status):
        self.cursor.execute('UPDATE tasks SET status = ? WHERE task_id = ?', (new_status, task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        self.cursor.execute('DELETE FROM tasks WHERE task_id = ?', (task_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
