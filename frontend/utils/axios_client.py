import requests

class Axios:
    """
    Custom axios-like HTTP client using the requests library.
    Supports GET, POST, PUT, PATCH, and DELETE requests.
    """

    def __init__(self, base_url="", headers=None, timeout=10):
        """
        Initialize with optional base_url, headers, and timeout.
        """
        self.base_url = base_url
        self.headers = headers or {}
        self.timeout = timeout

    def request(self, method, url, **kwargs):
        """
        Make an HTTP request with the given method and URL.
        """
        full_url = self.base_url + url
        kwargs.setdefault('headers', self.headers)
        kwargs.setdefault('timeout', self.timeout)
        try:
            response = requests.request(method=method, url=full_url, **kwargs)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"HTTP request failed: {e}")
            return None

    def get(self, url, params=None, **kwargs):
        """
        Shortcut for making GET requests.
        """
        return self.request("GET", url, params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        """
        Shortcut for making POST requests.
        """
        return self.request("POST", url, data=data, json=json, **kwargs)

    def put(self, url, data=None, json=None, **kwargs):
        """
        Shortcut for making PUT requests.
        """
        return self.request("PUT", url, data=data, json=json, **kwargs)

    def patch(self, url, data=None, json=None, **kwargs):
        """
        Shortcut for making PATCH requests.
        """
        return self.request("PATCH", url, data=data, json=json, **kwargs)

    def delete(self, url, **kwargs):
        """
        Shortcut for making DELETE requests.
        """
        return self.request("DELETE", url, **kwargs)