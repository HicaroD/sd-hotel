import sqlite3


class DBConnection:
    def __init__(self) -> None:
        self._db_name = "hotel.db"
        self.db_connection = sqlite3.connect(
            self._db_name,
            check_same_thread=False,
        )

    def get_all_rooms(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM Rooms WHERE NOT occupied ORDER BY id")
        rooms = cursor.fetchall()
        cursor.close()
        return rooms

    def check_in(self, id):
        cursor = self.db_connection.cursor()
        cursor.execute(f"UPDATE Rooms SET occupied = TRUE WHERE id = {id}")
        self.db_connection.commit()
        cursor.close()

    def check_out(self, id):
        cursor = self.db_connection.cursor()
        cursor.execute(f"UPDATE Rooms SET occupied = FALSE WHERE id = {id}")
        self.db_connection.commit()
        cursor.close()
