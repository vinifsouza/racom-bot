import sqlite3


class CoreDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('core.db')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def insert_faq_row(self, title, content):
        values = {
            'title': title,
            'content': content
        }

        self.cursor.execute('''
        INSERT INTO TFAQ
            (faq_title, faq_content)
        VALUES
            (:title, :content);
        ''', values
        )

        self.conn.commit()

        return None

    def create_faq_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS TFAQ (
            faq_cod INTEGER PRIMARY KEY,
            faq_title TEXT UNIQUE NOT NULL,
            faq_content TEXT NOT NULL,
            faq_dtcreate DATETIME NOT NULL DEFAULT (DATETIME('now')),
            faq_dtupdate DATETIME NOT NULL DEFAULT (DATETIME('now'))
        );
        ''')

        self.cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS DateUpdate
        AFTER UPDATE ON TFAQ
        FOR EACH ROW
        BEGIN
            UPDATE TFAQ
            SET faq_dtupdate = DATETIME('now')
            WHERE TFAQ.faq_cod = OLD.faq_cod;
        END;
        ''')

        return None

if __name__ == '__main__':
    CoreDatabase().create_faq_table()
    CoreDatabase().insert_faq_row('titulo', 'conteudo2')
