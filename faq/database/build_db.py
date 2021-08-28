import sqlite3


class CoreDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('./database/core.db')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def build_schema(self):
        self.__create_category_table()
        self.__create_faq_table()

        return None

    def insert_category_row(self, id, name):
        values = {
            'id': id,
            'name': name
        }

        query = self.cursor.execute('''
        SELECT cat_id FROM TFAQCategory
        WHERE (cat_id = :id OR cat_name = :name)
        ''', values)

        query = query.fetchone()

        if not query:
            self.cursor.execute('''
            INSERT INTO TFAQCategory
                (cat_id, cat_name)
            VALUES
                (:id, :name)
            ''', values)

            self.conn.commit()

        return None

    def insert_faq_row(self, question, answer, category_id):
        values = {
            'question': question,
            'answer': answer,
            'category_id': category_id
        }

        self.cursor.execute('''
        INSERT INTO TFAQ
            (faq_question, faq_answer, faq_cat_id)
        VALUES
            (:question, :answer, :category_id);
        ''', values
        )

        self.conn.commit()

        return None

    def __create_category_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS TFAQCategory (
            cat_id TEXT PRIMARY KEY,
            cat_name TEXT UNIQUE NOT NULL,
            cat_dtcreate DATETIME NOT NULL DEFAULT (DATETIME('now')),
            cat_dtupdate DATETIME NOT NULL DEFAULT (DATETIME('now'))
        );
        ''')

        self.cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS CategoryDateUpdate
        AFTER UPDATE ON TFAQCategory
        FOR EACH ROW
        BEGIN
            UPDATE TFAQCategory
            SET faq_dtupdate = DATETIME('now')
            WHERE TFAQCategory.cat_id = OLD.cat_id;
        END;
        ''')

        return None

    def __create_faq_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS TFAQ (
            faq_id INTEGER PRIMARY KEY,
            faq_question TEXT UNIQUE NOT NULL,
            faq_answer TEXT NOT NULL,
            faq_cat_id TEXT NOT NULL,
            faq_dtcreate DATETIME NOT NULL DEFAULT (DATETIME('now')),
            faq_dtupdate DATETIME NOT NULL DEFAULT (DATETIME('now')),
            CONSTRAINT faq_cat_id
            FOREIGN KEY (faq_cat_id)
            REFERENCES TFAQCategory(cat_id)
        );
        ''')

        self.cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS FAQDateUpdate
        AFTER UPDATE ON TFAQ
        FOR EACH ROW
        BEGIN
            UPDATE TFAQ
            SET faq_dtupdate = DATETIME('now')
            WHERE TFAQ.faq_id = OLD.faq_id;
        END;
        ''')

        return None