import json
import hmac
import hashlib
import base64

print("Starting script...") # Debug line

# Your JSON object
data = {
    "event": {
        "name": "Event System Metrics Test It Out Log",
        "description": "Triggers when the user successfully records their results from the Test It Out page. ",
        "type": "event-system-metrics-test-it-out-log",
        "created_at": "2025-01-29T05:53:45.776Z",
        "comment": None
    },
    "test_taker": {
        "first_name": "Jenni",
        "last_name": "Currell",
        "email": "testing.emails+home794690@cisi.org",
        "username": "67eb8cc5",
        "student_id": None,
        "links": {
            "show": "https://demo.proctoru.com/institutions/958428164/users/925962063"
        }
    },
    "system_metrics": {
        "operating_system": "Windows",
        "browser": "Meazure Learning Secure Browser",
        "proctoru_browser_extension_version": "Guardian Browser v1.20.0",
        "display": "Monitor 1 Resolution: 1281 x 720",
        "cpu_information": "N/A",
        "cpu_usage": "4%",
        "memory_information": "N/A",
        "memory_usage": "85%",
        "download_speed": "8711 Kb/s",
        "upload_speed": "36693 Kb/s"
    }
}

# Secret key for HMAC
secret_key = "f658619579cdca778d45453432fca"

try:
    # Step 1: Convert JSON to string
    json_string = json.dumps(data, separators=(',', ':'), sort_keys=False)
    print("\nJSON string created successfully")
    
    # Step 2: Compute HMAC-SHA1 signature
    hmac_signature = hmac.new(secret_key.encode(), json_string.encode(), hashlib.sha1).digest()
    print("HMAC signature computed successfully")
    
    # Step 3: Base64 encode the signature
    base64_signature = base64.b64encode(hmac_signature).decode()
    print("Base64 encoding completed successfully")
    
    # Print results
    print("\nResults:")
    print("Stringified JSON:", json_string)
    print("HMAC-SHA1 Signature:", base64_signature)

except Exception as e:
    print(f"An error occurred: {e}")