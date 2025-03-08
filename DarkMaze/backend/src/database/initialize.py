import sqlite3

def initialize() -> None:
    """Initialize the database and create required tables if they do not exist."""
    try:
        conn = sqlite3.connect("game.db")
        cursor = conn.cursor()

        # Create game_state table (with username column)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_state (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            current_level_name TEXT NOT NULL,
            map_size TEXT NOT NULL,
            health INTEGER NOT NULL,
            path TEXT NOT NULL,
            current_position TEXT NOT NULL
        )
        """)

        conn.commit()
    except sqlite3.Error as e:
        print(f"Database initialization failed: {e}")
    finally:
        conn.close()
