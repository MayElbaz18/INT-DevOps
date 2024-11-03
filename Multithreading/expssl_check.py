import requests
import json
import concurrent.futures
from queue import Queue
import time
import ssl
import socket
from datetime import datetime


# Measure start time
start_time = time.time()

urls_queue = Queue()
analyzed_urls_queue = Queue()

# Load URLs into the queue
with open('Multithreading/120.domains.txt', 'r') as infile:
    for line in infile:
        urls_queue.put(line.strip())

print(f"Total URLs to check: {urls_queue.qsize()}")

def check_certificate(url):
    result = {'expiration_status': 'None', 'expiration_date': 'None'}
    try:
        # Remove "https://", "http://", "www." from the URL if present
        hostname = url.replace("https://", "").replace("http://", "").replace("www.", "").split("/")[0]
        
        # Establish a secure connection to fetch the SSL certificate
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
        # Get the certificate's expiration date
        expiry_date_str = cert['notAfter']
        expiry_date = datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
        
        # Convert expiration date to a readable string format
        expiry_date_formatted = expiry_date.strftime("%Y-%m-%d %H:%M:%S")
        
        # Check if the certificate is expired
        if expiry_date < datetime.now():
            result['expiration_status'] = 'expired'
        else:
            result['expiration_status'] = 'valid'

        result['expiration_date'] = expiry_date_formatted

    except Exception as e:
        result['expiration_status'] = 'None'
        result['expiration_status'] = str(e)
    
    return result
 
    # Define the URL checking function with a timeout and result storage
def check_url():
    while not urls_queue.empty():
        url = urls_queue.get()
        result = {'url': url,
                  'status_code': 'FAILED',
                  'expiration_status': 'None',
                  'expiration_date': 'None'}  
        
        try:
            response = requests.get(f'http://{url}', timeout=1)
            if response.status_code == 200:
                cert_result = check_certificate(url)
                result['status_code'] = 'OK'
                result['expiration_status'] = cert_result['expiration_status']
                result['expiration_date'] = cert_result['expiration_date']

        except requests.exceptions.RequestException:
            pass

        finally:
            analyzed_urls_queue.put(result)  # Add result to analyzed queue
            urls_queue.task_done()

# Generate report after all URLs are analyzed
def generate_report():
    results = []
    urls_queue.join()  # Wait for all URL checks to finish

    # Collect results from analyzed queue
    while not analyzed_urls_queue.empty():
        results.append(analyzed_urls_queue.get())
        analyzed_urls_queue.task_done()
    
    # Write results to JSON file
    with open('Multithreading/report.json', 'w') as outfile:
        json.dump(results, outfile, indent=4)
    print("Report generated in report.json")

# Run URL checks in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as liveness_threads_pool:
    # Submit URL check tasks
    futures = [liveness_threads_pool.submit(check_url) for _ in range(20)]
    # Generate report after tasks complete
    liveness_threads_pool.submit(generate_report)

urls_queue.join()  # Ensure all URLs are processed

# Measure end time
end_time = time.time()
elapsed_time = end_time - start_time

print(f"URL liveness check complete in {elapsed_time:.2f} seconds.")