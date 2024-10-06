import base64
from google.cloud import bigquery

def process_data(event, context):
    client = bigquery.Client()
    dataset_id = 'analytics_dataset'
    table_id = 'data_table'
    table_ref = client.dataset(dataset_id).table(table_id)

    data = base64.b64decode(event['data']).decode('utf-8')
    # Process data as needed
    rows_to_insert = [
        {u"column_name": data}  # Adjust according to your schema
    ]

    errors = client.insert_rows_json(table_ref, rows_to_insert)
    if errors:
        print(f"Encountered errors while inserting rows: {errors}")