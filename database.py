import aiosqlite

from config import DATABASE_NAME


class Database:

    def __init__(self):
        self.db = DATABASE_NAME

    async def connect(self):
        return await aiosqlite.connect(self.db)

    async def setup(self):

        async with await self.connect() as db:

            await db.execute("""

            CREATE TABLE IF NOT EXISTS users(

                user_id INTEGER PRIMARY KEY,

                full_name TEXT,

                username TEXT,

                coins INTEGER DEFAULT 0,

                warns INTEGER DEFAULT 0,

                joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )

            """)

            await db.execute("""

            CREATE TABLE IF NOT EXISTS groups(

                group_id INTEGER PRIMARY KEY,

                title TEXT,

                welcome TEXT,

                rules TEXT,

                force_join INTEGER DEFAULT 0,

                force_channel TEXT,

                personality TEXT DEFAULT 'normal'

            )

            """)

            await db.execute("""

            CREATE TABLE IF NOT EXISTS admins(

                group_id INTEGER,

                user_id INTEGER,

                PRIMARY KEY(group_id,user_id)

            )

            """)

            await db.execute("""

            CREATE TABLE IF NOT EXISTS replies(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                group_id INTEGER,

                keyword TEXT,

                answer TEXT

            )

            """)

            await db.execute("""

            CREATE TABLE IF NOT EXISTS logs(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                group_id INTEGER,

                admin_id INTEGER,

                action TEXT,

                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )

            """)

            await db.commit()


database = Database()
