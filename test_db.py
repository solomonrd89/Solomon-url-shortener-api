import os
from dotenv import load_dotenv
import pymysql  # <--- CHANGED THIS

print("--- 1. Testing .env File ---")
load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
pw = os.getenv("DB_PASSWORD")
db = os.getenv("DB_NAME")

if not host or not user or not pw:
    print(
        f"❌ ERROR: Missing variables! \nHost: {host}, User: {user}, Pass: {'Found' if pw else 'Missing'}"
    )
else:
    print("✅ Variables loaded successfully.")

print("\n--- 2. Testing Database Connection (PyMySQL) ---")
try:
    # PyMySQL Connection
    conn = pymysql.connect(host=host, user=user, password=pw, database=db)
    print("✅ Database Connection SUCCESS!")
    conn.close()
except Exception as e:
    print(f"❌ Connection FAILED: {e}")
