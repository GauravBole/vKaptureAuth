import datetime
from config import db_cursor as cursor, db_conn as conn
import psycopg2

def create_query():
    try:
        today = (datetime.date.today())
        year = today.year
        month = today.month
        day = today.day
        query_date_data = {"year": year, "month": month, "day": day}
        query_number = ''' select * from query_number where day={} limit 1; '''
        cursor.execute(query_number.format(day))
        row = cursor.fetchone()
        if not row:
            new_query = '''insert into query_number (query, month, year, day) values({query}, {month}, {year}, {day});'''
            query_date_data['query'] = 1
            print(new_query.format(**query_date_data))
            cursor.execute(new_query.format(**query_date_data))
            # cursor.close()
            query_id = str(month) + str(year) + str(1).zfill(4)
            return query_id

        if row['year'] != year or row['month'] != month or row['day'] != day:
            query = 1
        else:
            query = row['query']+1
            
        update_query = ''' update query_number set query={query}, month={month}, year={year}, day={day} where id = {row_id};'''

        query_date_data['query'] = query
        query_date_data['row_id'] = row['id']

        cursor.execute(update_query.format(**query_date_data))
        
        # cursor.close()
        query_id = str(month) + str(year) + str(query).zfill(4)
        print(query_id)
        return query_id
    except psycopg2.ProgrammingError as exc:
        print(exc.message)
        conn.rollback()
    except Exception as e:
        print(e, '--->')
        cursor.close()

