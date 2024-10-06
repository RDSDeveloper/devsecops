from fastapi import FastAPI
from google.cloud import bigquery

app = FastAPI()

@app.get("/data")
async def get_data():
    client = bigquery.Client()
    query = """
        SELECT * FROM `project_id.analytics_dataset.data_table`
    """
    query_job = client.query(query)
    results = query_job.result()
    return [dict(row) for row in results]