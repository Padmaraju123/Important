
import requests

def test_collecting_details_get_api():
    get_res = requests.get("https://reqres.in/api/users?page=2")

    """
        validations
        --------------
        1) status code
        2) time taken
        3) size of the data
        4) response body
        5) cookies
        6) headers
    """

    # time taken in milliseconds
    print("Response Time (seconds):", get_res.elapsed.total_seconds() * 1000)

    # Size in bytes
    size_bytes = len(get_res.content)

    # Convert to KB
    size_kb = size_bytes / 1024

    print(size_kb)

    print(get_res)
    print(type(get_res))

    print(get_res.text)
    print(type(get_res.text))

    # .json() will convert the response into dictionary format
    print(get_res.json())
    print(type(get_res.json()))

    # printing the current url
    print(get_res.url)

    # printing the status code like 200
    print(get_res.status_code)
    print(type(get_res.status_code))

    # Returns the raw response body in bytes.
    print(get_res.content)
