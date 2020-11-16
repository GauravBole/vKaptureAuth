
from config import db_cursor as cursor, db_conn as conn

class StateDistrictDao:

    def add_states_district(self, state_id, district_id):
        add_states_qs = '''insert into state_district (state_id, district_id) values ('{state_id}', '{district_id}') RETURNING id'''
        cursor.execute(add_states_qs.format(state_id=state_id, district_id=district_id))
        row = cursor.fetchone()
        if row:
            conn.commit()
            return row['id']


