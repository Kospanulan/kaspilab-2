import psycopg2


def export_from_csv_to_db(path, table_name):
    f = open(path, 'r')
    cursor.copy_from(f, table_name, sep=',', null="")
    f.close()


if __name__ == '__main__':

    conn = psycopg2.connect(dbname='Kaspilab', user='postgres',
                            password='postgres', host='localhost')
    cursor = conn.cursor()

    export_from_csv_to_db("data/Data.csv", "data")
    export_from_csv_to_db("data/Info.csv", "info")
    export_from_csv_to_db("data/Processed.csv", "processed")

    cursor.close()
    conn.commit()
    conn.close()
