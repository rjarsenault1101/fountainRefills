import psycopg2
import random
try:
    conn = psycopg2.connect("dbname='refills' user='postgres' host='localhost' password='1234'")
    cursor = conn.cursor()
    execute_string = "insert into data_datapoint (value, date, time, timestamp) values (%s, %s, %s, %s)"
    date_format="2020-04-{:0>2}"
    time_format="{:0>2}:{:0>2}:00.000000"
    start = 0
    for day in range(1, 30):
        for hour in range(7, 18):
            for minute in range(0, 59):
                if random.random() < .01:
                    start = start + random.randint(1, 10)
                    date = date_format.format(day)
                    time = time_format.format(hour, minute)
                    timestamp = date + " " + time
                    print(execute_string % ("value", date, time, timestamp))
                    try:
                        cursor.execute(execute_string, (start, date, time, timestamp))
                        conn.commit()
                    except(psycopg2.DatabaseError) as e:
                        print(e)
    
except(psycopg2.DatabaseError) as e:
    print(e)
finally:
    cursor.close()
    conn.close()
