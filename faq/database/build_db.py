from pathlib import Path
import pymysql

from faq.config import (
    DATABASE_HOST,
    DATABASE_NAME,
    DATABASE_PASS,
    DATABASE_USER
)


class CoreDatabase:
    def __init__(self):
        print(
            DATABASE_HOST,
            DATABASE_NAME,
            DATABASE_PASS,
            DATABASE_USER,
            flush=True
        )
        self.conn = pymysql.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            passwd=DATABASE_PASS,
            database=DATABASE_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.conn.cursor()

    def build_schema(self):
        self.__create_category_table()
        self.__create_faq_table()
        self.__create_unrecognized_message_table()

        return None

    def insert_category_row(self, id, name):
        self.cursor.execute('''
        SELECT cat_id FROM TFAQCategory
        WHERE (cat_id = '{p1}' OR cat_name = '{p2}')
        '''.format(
            p1=id,
            p2=name
        ))

        query = self.cursor.fetchone()

        if not query:
            self.cursor.execute('''
            INSERT INTO TFAQCategory
                (cat_id, cat_name)
            VALUES
                ('{p1}', '{p2}')
            '''.format(
                p1=id,
                p2=name
            ))

            self.conn.commit()

        return None

    def insert_faq_row(self, question, answer, answer_html, category_id):
        self.cursor.execute('''
        INSERT INTO TFAQ
            (faq_question, faq_answer, faq_answer_html, faq_cat_id)
        VALUES
            ('{p1}', '{p2}', '{p3}', '{p4}');
        '''.format(
            p1=question,
            p2=answer,
            p3=answer_html,
            p4=category_id
        ))

        self.conn.commit()

        return None

    def __create_category_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS TFAQCategory (
            cat_id VARCHAR(512) PRIMARY KEY NOT NULL,
            cat_name VARCHAR(512) UNIQUE NOT NULL,
            cat_dtcreate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            cat_dtupdate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON
            UPDATE
                CURRENT_TIMESTAMP
        ) ENGINE = InnoDB AUTO_INCREMENT = 1
        CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
        ''')

        self.conn.commit()
        return None

    def __create_faq_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS TFAQ (
            faq_id INT PRIMARY KEY AUTO_INCREMENT,
            faq_question VARCHAR(512) UNIQUE NOT NULL,
            faq_answer TEXT NOT NULL,
            faq_answer_html TEXT NOT NULL,
            faq_cat_id VARCHAR(512) NOT NULL,
            faq_dtcreate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            faq_dtupdate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            CONSTRAINT faq_cat_id FOREIGN KEY (faq_cat_id) REFERENCES TFAQCategory(cat_id)
        ) ENGINE = InnoDB AUTO_INCREMENT = 1
        CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
        ''')

        self.conn.commit()
        return None

    def __create_unrecognized_message_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS TUnrecognizedMessage (
            ums_id INT PRIMARY KEY AUTO_INCREMENT,
            ums_text VARCHAR(512) UNIQUE NOT NULL,
            ums_dtcreate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            ums_dtupdate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
        ENGINE = InnoDB AUTO_INCREMENT = 1
        CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
        ''')

        return None
