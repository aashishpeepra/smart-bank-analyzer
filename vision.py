from pydoc import cli
from google.cloud import storage

client = storage.Client.from_service_account_json('credentials.json')

buckets = list(client.list_buckets())

print(buckets)