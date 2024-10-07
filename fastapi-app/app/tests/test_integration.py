import httpx
import pytest
from google.cloud import bigquery
from google.cloud.bigquery import DatasetReference, TableReference


@pytest.mark.asyncio
async def test_get_data():
    url = "https://fastapi-service-m4hco5opeq-uc.a.run.app/data"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert "column_name_1" in data[0]

# Propose additional integration tests
# 1. Test data ingestion by publishing a message to the Pub/Sub topic and verifying it is processed and stored in BigQuery.
# 2. Test data retrieval with different query parameters to ensure the API handles them correctly.
# 3. Test the system's behavior under load by simulating multiple concurrent requests to the API.

@pytest.fixture(scope="module")
def bigquery_client():
    return bigquery.Client()


@pytest.fixture(scope="module")
def test_data():
    return {
        "column_name_1": "test_string",
        "column_name_2": 456,
        "column_name_3": "2023-10-07T12:00:00Z",
    }


@pytest.fixture(scope="module")
def insert_test_data(bigquery_client, test_data):
    dataset_id = "analytics_dataset"
    table_id = "data_table"
    dataset_ref = DatasetReference(bigquery_client.project, dataset_id)
    table_ref = TableReference(dataset_ref, table_id)

    # Insert test data into BigQuery
    errors = bigquery_client.insert_rows_json(table_ref, [test_data])
    assert not errors, f"Errors occurred while inserting test data: {errors}"

    yield

    # Clean up test data
    query = f"""
        DELETE FROM `devsecops-437822.analytics_dataset.data_table`
        WHERE column_name_1 = '{test_data["column_name_1"]}'
    """
    bigquery_client.query(query).result()

# Identify critical points and propose testing or measurement methods
# 1. Pub/Sub message processing latency: Measure the time taken from message publication to data storage.
# 2. API response time: Monitor and log response times to identify performance bottlenecks.
# 3. BigQuery query performance: Analyze query execution times and optimize as needed.

# Propose system robustness improvements
# 1. Implement retries and exponential backoff for Pub/Sub message processing to handle transient errors.
# 2. Use caching mechanisms to reduce load on BigQuery for frequently accessed data.
# 3. Implement monitoring and alerting for critical metrics such as API response time and error rates.
