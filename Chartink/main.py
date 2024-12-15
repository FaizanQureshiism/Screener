import requests

# URL to send the POST request
url = "https://chartink.com/screener/process"



# The body for the POST request
data = {
    "scan_clause": "(+%7B33492%7D+(+%5B0%5D+1+minute+rsi(+3+)+%3E+%5B0%5D+1+minute+rsi(+6+)+and+%5B0%5D+1+minute+rsi(+6+)+%3E+%5B0%5D+1+minute+rsi(+9+)+and+%5B0%5D+1+minute+rsi(+9+)+%3E+%5B0%5D+1+minute+rsi(+13+)+and+%5B0%5D+1+minute+rsi(+13+)+%3E+%5B0%5D+1+minute+rsi(+20+)+and+%5B0%5D+1+minute+rsi(+20+)+%3E+%5B0%5D+1+minute+rsi(+50+)+)+)+",
    "debug_clause": "groupcount(+1+where+%5B0%5D+1+minute+rsi(+3+)+%3E+%5B0%5D+1+minute+rsi(+6+))%2Cgroupcount(+1+where+%5B0%5D+1+minute+rsi(+6+)+%3E+%5B0%5D+1+minute+rsi(+9+))%2Cgroupcount(+1+where+%5B0%5D+1+minute+rsi(+9+)+%3E+%5B0%5D+1+minute+rsi(+13+))%2Cgroupcount(+1+where+%5B0%5D+1+minute+rsi(+13+)+%3E+%5B0%5D+1+minute+rsi(+20+))%2Cgroupcount(+1+where+%5B0%5D+1+minute+rsi(+20+)+%3E+%5B0%5D+1+minute+rsi(+50+))"
}

# Send the POST request
response = requests.post(url, headers=headers, data=data)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON and print the data
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
