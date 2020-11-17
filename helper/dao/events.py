
from config import db_cursor as cursor, db_conn as conn

class EventsDao:

    def add_events(self, name, code):
        # values = ', '.join(map(str, address_data))
        try:
            add_evenys_category_qs = '''insert into event_category (name, code) values ('{name}', '{code}') on conflict (code) DO UPDATE SET name='{name}' RETURNING id'''
            print(add_evenys_category_qs.format(name=name, code=code))
            cursor.execute(add_evenys_category_qs.format(name=name, code=code))
            
            row = cursor.fetchone()
            if row:
                conn.commit()
                return row['id']
        except Exception as e:
            print(e)


