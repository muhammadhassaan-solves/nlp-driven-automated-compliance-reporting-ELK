from elasticsearch import Elasticsearch
import json

# Connect to Elasticsearch
es = Elasticsearch(
    hosts=["https://localhost:9200"],
    http_auth=("elastic", "password"),
    verify_certs=False
)

# Define the search query
query = {
    "query": {
        "match_all": {}
    }
}

# Execute the search
response = es.search(index="compliance-logs", body=query)

# Generate report
report = []
for hit in response["hits"]["hits"]:
    report.append(hit["_source"])

# Save report to file
with open("/home/ubuntu/compliance_report.json", "w") as f:
    f.write(json.dumps(report, indent=4))

print("Report generated: compliance_report.json")
