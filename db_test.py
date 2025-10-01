import psycopg2

try:
    conn = psycopg2.connect(
        dbname="myproject",       # tumhare database ka naam
        user="postgres",          # tumhara username
        password="@Ayushi1610", # jo password install ke time set kiya tha
        host="localhost",
        port="5432"
    )
    print("Connected successfully!")

    # Cursor create karo aur simple query run karo
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    print("Database version:", db_version)

    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)
