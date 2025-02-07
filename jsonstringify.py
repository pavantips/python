import json
import hmac
import hashlib
import base64

# Your JSON object
data = {
  "event": {
    "name": "Reservation Cancelled",
    "description": "Reservation Cancelled",
    "type": "event-reservation-cancelled",
    "created_at": "2025-01-31T00:51:12.481Z",
    "comment": "test"
  },
  "exam": {
    "name": "Second Camera Experience",
    "id": "380e360f-4cf0-4003-b91c-096a64a650ad",
    "external_id": "",
    "course_number":"",
    "term": "60min",
    "department": "Default",
    "links": {
      "show": "https://go.proctoru.com/institutions/2099/iterations/13829352"
    }
  },
  "reservation": {
    "status": "cancelled",
    "campus_name": "",
    "id": "307ab0c8-5f76-46aa-b4b3-3959c655d82f",
    "number": 38504370,
    "external_id": "",
    "service_line": "live_plus",
    "starts_at": "2025-01-31T18:50:00.000Z",
    "ends_at": "2025-01-31T19:50:00.000Z",
    "links": {
      "show": "https://go.proctoru.com/reservations/307ab0c8-5f76-46aa-b4b3-3959c655d82f"
    }
  },
  "test_taker": {
    "first_name": "test",
    "last_name": "test",
    "email": "nbroom+yd@proctoru.com",
    "username": "6bd4d0ae",
    "student_id": "2005537",
    "links": {
      "show": "https://go.proctoru.com/institutions/2099/users/12732949"
    }
  },
  "cancellation": {
    "reason": "Advance Cancellation",
    "explanation": "test",
    "credit": "student",
    "created_at": "2025-01-31T00:51:12.476Z",
    "links": {
      "show": "https://go.proctoru.com/reservations/307ab0c8-5f76-46aa-b4b3-3959c655d82f"
    }
  },
  "content_type": "application/json"
}


# Secret key for HMAC (replace with your actual secret key)
secret_key = "eb49d5e5-9792-464d-85f0-99be84239e95"

# Step 1: Convert JSON to string (no extra spaces, sorted keys for consistency)
json_string = json.dumps(data, separators=(',', ':'), sort_keys=False)

# Step 2: Compute HMAC-SHA1 signature
hmac_signature = hmac.new(secret_key.encode(), json_string.encode(), hashlib.sha1).digest()

# Step 3: Base64 encode the signature
base64_signature = base64.b64encode(hmac_signature).decode()

# Print results
print("Stringified JSON:", json_string)
print("HMAC-SHA1 Signature:", base64_signature)
