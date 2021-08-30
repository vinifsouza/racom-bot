from pathlib import Path
import sqlite3

from faq.config import DATABASE_PATH


class CoreDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(Path(DATABASE_PATH))
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def build_schema(self):
        self.__create_category_table()
        self.__create_faq_table()
        self.__create_unrecognized_message_table()

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

    def insert_faq_row(self, question, answer, answer_html, category_id):
        values = {
            'question': question,
            'answer_html': answer_html,
            'answer': answer,
            'category_id': category_id
        }

        self.cursor.execute('''
        INSERT INTO TFAQ
            (faq_question, faq_answer, faq_answer_html, faq_cat_id)
        VALUES
            (:question, :answer, :answer_html, :category_id);
        ''', values)

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
            faq_answer_html TEXT NOT NULL,
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

    def __create_unrecognized_message_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS TUnrecognizedMessage (
            ums_id INTEGER PRIMARY KEY,
            ums_text TEXT UNIQUE NOT NULL,
            ums_dtcreate DATETIME NOT NULL DEFAULT (DATETIME('now')),
            ums_dtupdate DATETIME NOT NULL DEFAULT (DATETIME('now'))
        );
        ''')

        self.cursor.execute('''
        CREATE TRIGGER IF NOT EXISTS UnrecognizedMessageDateUpdate
        AFTER UPDATE ON TUnrecognizedMessage
        FOR EACH ROW
        BEGIN
            UPDATE TUnrecognizedMessage
            SET ums_dtupdate = DATETIME('now')
            WHERE TUnrecognizedMessage.ums_id = OLD.ums_id;
        END;
        ''')

        return None
