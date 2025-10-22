from sqlalchemy import text

with app.app_context():
    try:
        # Add the new columns
        with db.engine.connect() as conn:
            conn.execute(text('ALTER TABLE habit ADD COLUMN is_archived BOOLEAN DEFAULT 0'))
            conn.execute(text('ALTER TABLE habit ADD COLUMN archived_at DATETIME'))
            conn.commit()
        print("✅ Database updated successfully!")
    except Exception as e:
        print(f"Error: {e}")
        print("Columns might already exist or there's another issue.")