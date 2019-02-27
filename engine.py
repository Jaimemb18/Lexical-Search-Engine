import sys

# mysql connector and error
import mysql.connector
from mysql.connector import Error


log = False

def search(lang, search_for):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='reserved_words',
            user='',
            password='')

        if log:
            print("Established connection")

        query = ("""
                SELECT *, SUM(MATCH(keyword, description) AGAINST ('"""+search_for+"""' IN BOOLEAN MODE)) as rank
                FROM descriptions
                WHERE MATCH(keyword, description) AGAINST ('"""+search_for+"""' IN BOOLEAN MODE) AND lang = '"""+lang+"""'
                ORDER BY rank desc
                LIMIT 0,10
                """)

        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()

        print(records)

        for row in records:
            print(row[3], "    ", row[1],'\t:', row[2])

        cursor.close()

    except Error as e:
        error(e)

    finally:
        if connection.is_connected():
            connection.close()
            if log:
                print("Closed Connection to database")

def usage():
    print("Usage: python3 engine.py language [-v] term...")
    print("\t- language:\tprogramming language to search in (CSS, React, etc.)")
    print("\t- -v\t\tverbose")
    print("\t- term:\t\tterm to search for")
    exit(1)

def error(msg):
    print("ERROR: ",msg)
    exit(1)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        usage()

    lang = sys.argv[1]
    log = '-v' in sys.argv
    terms = set([arg.lower() for arg in sys.argv[2:] if arg not in '-v'])

    if len(terms) is 0:
        usage()

    search_for = "+"+str(" +".join(terms))

    search(lang, search_for)

