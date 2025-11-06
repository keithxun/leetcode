import time, uuid, random, requests

def make_idempotent_request(url, data, max_retries=5):
    idem = str(uuid.uuid4())
    headers = {'Authorization': 'Bearer {api_key}',
               "Content-Type": "application/json",
                'Idempotency-Key': idem,
                "User-Agent": 'IdempotentClient/1.0'}
    backoff = 0.2

    for attempt in range(max_retries):
        try:
            r = requests.post(url, json=data, headers=headers)
            if r.status_code == 200:
                return r.json()
            else:
                print(f"Request failed with status {r.status_code}: {r.text}")
        except requests.RequestException as e:
            print(f"Request error: {e}")
        time.sleep(backoff)
        backoff *= 2
    return {"error": "Max retries exceeded"}