import base64
from google.cloud import bigquery

def process_data(event, context):
    client = bigquery.Client()
    dataset_id = 'analytics_dataset'
    table_id = 'data_table'
    table_ref = client.dataset(dataset_id).table(table_id)

    data = base64.b64decode(event['data']).decode('utf-8')
    # Assuming data is a JSON string, parse it
    import json
    parsed_data = json.loads(data)

    # Process data as needed
    rows_to_insert = [
        {
            "column_name_1": parsed_data.get("column_name_1"),
            "column_name_2": parsed_data.get("column_name_2"),
            "column_name_3": parsed_data.get("column_name_3")
        }
    ]

    errors = client.insert_rows_json(table_ref, rows_to_insert)
    if errors:
        print(f"Encountered errors while inserting rows: {errors}")