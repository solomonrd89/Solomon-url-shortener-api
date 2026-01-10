import string
import random
import pymysql
from . import get_db_connection


def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def create_short_url(original_url):
    conn = get_db_connection()
    cursor = conn.cursor()

    for _ in range(5):
        short_code = generate_short_code()
        try:
            # Try to insert directly
            cursor.execute(
                "INSERT INTO urls (original_url, short_code) VALUES (%s, %s)",
                (original_url, short_code),
            )
            conn.commit()
            return short_code
        except pymysql.err.IntegrityError:
            # Collision detected! Loop again.
            continue
        finally:
            cursor.close()
            conn.close()

    raise Exception("Failed to generate unique code")


def get_original_and_track(short_code):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT original_url FROM urls WHERE short_code = %s", (short_code,))
    result = cursor.fetchone()

    if result:
        try:
            cursor.execute(
                "INSERT INTO analytics (short_code) VALUES (%s)", (short_code,)
            )
            conn.commit()
        except Exception as e:
            print(f"Analytics Error: {e}")

        cursor.close()
        conn.close()
        return result[0]

    cursor.close()
    conn.close()
    return None
