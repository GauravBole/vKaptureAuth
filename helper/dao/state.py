
from config import db_cursor as cursor, db_conn as conn

class StateDao:

    def add_states(self, name, code):
        # values = ', '.join(map(str, address_data))
        try:
            add_states_qs = '''insert into state (name, code) values ('{name}', '{code}') on conflict (code) DO UPDATE SET name='{name}' RETURNING id'''
            cursor.execute(add_states_qs.format(name=name, code=code))
            row = cursor.fetchone()
            if row:
                conn.commit()
                return row['id']
        except Exception as e:
            print(e)


