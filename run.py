print("DEBUG: Run.py is starting...")  # 1. Check if script starts

from app import create_app  # 2. Check if import works

print("DEBUG: Import successful")

app = create_app()  # 3. Check if app creation works

if __name__ == "__main__":
    print("DEBUG: Starting Server...")
    app.run(debug=True)
