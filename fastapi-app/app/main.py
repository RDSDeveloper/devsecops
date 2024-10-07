from fastapi import FastAPI, HTTPException
from google.cloud import bigquery

app = FastAPI()

@app.get("/data")
async def get_data():
    try:
        client = bigquery.Client()
        query = """
            SELECT * FROM `devsecops-437822.analytics_dataset.data_table`
        """
        query_job = client.query(query)
        results = query_job.result()
        return [dict(row) for row in results]
    except Exception as e:
        # Log the error and raise an HTTP exception
        print(f"Error fetching data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")