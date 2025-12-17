import time
import threading
import urllib.request
import urllib.error
import sys

# URL of your deployed application
URL = "https://rental-app.livelyrock-fd1cd27a.westeurope.azurecontainerapps.io/apidocs/"

# Number of concurrent threads (users)
CONCURRENT_USERS = 50

def send_request(user_id):
    print(f"User {user_id} started sending requests...")
    count = 0
    while True:
        try:
            # Send GET request
            with urllib.request.urlopen(URL) as response:
                # Read response to ensure request completes
                response.read()
                count += 1
                if count % 10 == 0:
                    print(f"User {user_id}: {count} requests sent. Status: {response.status}")
        except urllib.error.HTTPError as e:
            print(f"User {user_id}: HTTP Error {e.code}")
        except urllib.error.URLError as e:
            print(f"User {user_id}: URL Error {e.reason}")
        except Exception as e:
            print(f"User {user_id}: Error {e}")
            time.sleep(1)

if __name__ == "__main__":
    print(f"Starting load test on {URL}")
    print(f"Simulating {CONCURRENT_USERS} concurrent users.")
    print("Press Ctrl+C to stop.")
    
    threads = []
    try:
        for i in range(CONCURRENT_USERS):
            t = threading.Thread(target=send_request, args=(i,))
            t.daemon = True # Allow threads to be killed when main exits
            t.start()
            threads.append(t)
            time.sleep(0.1) # Stagger start slightly
        
        # Keep main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping load test...")
        sys.exit(0)
