import requests
import json
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample log messages
log_messages = [
    "User data encrypted successfully with AES256",
    "System audit completed for GDPR compliance",
    "Access denied due to security policy"
]

# Compliance keywords
compliance_keywords = ["user data", "PII", "encryption", "GDPR", "security", "audit"]

# Process logs
processed_logs = []
for log in log_messages:
    doc = nlp(log)
    extracted_terms = [token.text.lower() for token in doc if token.text.lower() in compliance_keywords]
    processed_logs.append({"message": log, "compliance_terms": extracted_terms})

# Save processed logs
with open("processed_logs.json", "w") as f:
    json.dump(processed_logs, f, indent=2)

print("Processed logs saved at /home/ubuntu/processed_logs.json")

~
