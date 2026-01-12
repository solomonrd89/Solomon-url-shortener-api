# services.py
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

    try:
        # We attempt 5 times to generate a unique code
        for _ in range(5):
            short_code = generate_short_code()
            try:
                cursor.execute(
                    "INSERT INTO urls (original_url, short_code) VALUES (%s, %s)",
                    (original_url, short_code),
                )
                conn.commit()
                # If successful, we return immediately.
                # The 'finally' block below will handle closing.
                return short_code
            except pymysql.err.IntegrityError:
                # Collision detected! The loop continues to the next iteration.
                # We DO NOT close the connection yet.
                continue

    except Exception as e:
        # Catch unexpected errors to ensure connection closes
        conn.rollback()
        raise e

    finally:
        # This runs when we return OR when the loop finishes
        cursor.close()
        conn.close()

    # If we exit the loop without returning, we failed to find a unique code
    raise Exception("Failed to generate unique code after 5 attempts")


def get_original_and_track(short_code):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT original_url FROM urls WHERE short_code = %s", (short_code,)
        )
        result = cursor.fetchone()

        if result:
            original_url = result[0]
            # Track the visit (Analytics)
            try:
                cursor.execute(
                    "INSERT INTO analytics (short_code) VALUES (%s)", (short_code,)
                )
                conn.commit()
            except Exception as e:
                print(f"Analytics Error: {e}")  # Log it, but don't stop the redirect

            return original_url

        return None

    finally:
        cursor.close()
        conn.close()
