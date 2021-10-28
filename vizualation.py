import psycopg2
from psycopg2 import sql
import numpy as np
from ProcessedData import ProcessedData
import plotly.graph_objects as go


def get_list_regions():
    with conn.cursor() as cursor:
        conn.autocommit = True

        query = sql.SQL('SELECT DISTINCT ON (region) region FROM v_processed;')

        cursor.execute(query)

        regions = np.array(cursor.fetchall())
        np.concatenate(regions, axis=None)
        print(regions.T[0])

    return regions.T[0]


def get_data_from_bd(region='Europe',
                     date_from='2010-01-01',
                     date_to='2010-02-01'):
    with conn.cursor() as cursor:
        conn.autocommit = True
        res = []
        query = sql.SQL('SELECT * FROM v_processed WHERE region=\'{}\' \
                        and date between \'{}\' and \'{}\';'.format(region, date_from, date_to))

        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            res.append(ProcessedData(row))
            print(row)

    return res


if __name__ == '__main__':
    conn = psycopg2.connect(dbname='Kaspilab', user='postgres',
                            password='postgres', host='localhost')

    for_date = np.vectorize(lambda x: x.get_dm_date())
    for_region = np.vectorize(lambda x: x.get_region())
    for_high = np.vectorize(lambda x: x.get_high())
    for_low = np.vectorize(lambda x: x.get_low())
    # for_year = np.vectorize(lambda x: x.get_year())
    # for_month = np.vectorize(lambda x: x.get_month())
    # for_day = np.vectorize(lambda x: x.get_day())

    region = 'Europe'

    proc_d = get_data_from_bd(region=region)
    proc_d = np.array(proc_d)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=for_date(proc_d), y=for_high(proc_d),
                             mode='lines+markers',
                             name='High Costs'))
    fig.add_trace(go.Scatter(x=for_date(proc_d), y=for_low(proc_d),
                             mode='lines+markers',
                             name='Low Costs'))

    fig.update_layout(
        title="High and Low costs",
        xaxis_title="Date year {}".format(proc_d[0].get_year()),
        yaxis_title="Costs [{}]".format(proc_d[0].get_currency()),
        legend_title="Region: {}".format(region),
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )

    fig.show()

    conn.close()
