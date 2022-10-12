import requests


class CryptoslamAPI:
    API_NAME = "CryptoSlam"

    def __init__(self, api_key: str = None,
                 api_url: str = "https://api.cryptoslam.io/dhcugckmn134lzcp",
                 version: str = "v1",
                 auth_type: str = "X-BLOBR-KEY"):
        self.HOST = api_url
        self.KEY = api_key
        self.VERSION = version
        self.AUTH_TYPE = auth_type

    def _get_headers(self):
        return {
            self.AUTH_TYPE: self.KEY,
        }

    def _request(self, request_method: str, url: str, payload=None):
        if request_method == "get":
            return requests.get(url, headers=self._get_headers(), params=payload)
        else:
            return requests.post(url, headers=self._get_headers(), json=payload)

    def _validate_call(self, request):
        if request.status_code == 400:
            raise ValueError(request.text)
        elif request.status_code == 401:
            raise requests.exceptions.HTTPError(request.text)
        elif request.status_code == 403:
            raise ConnectionError("The server blocked access.")
        elif request.status_code == 495:
            raise requests.exceptions.SSLError("SSL certificate error")
        elif request.status_code == 504:
            raise TimeoutError("The server reported a gateway time-out error.")
        if request.status_code != 200:
            raise Exception(500, f"{self.API_NAME} responded with error code.")
        return request.json()

    def get(self, url: str, params=None):
        return self._validate_call(self._request("get", url, params))

    def post(self, url: str, payload=None):
        return self._validate_call(self._request("post", url, payload))

    def get_blockchain_ids(self):
        url = f"{self.HOST}/{self.VERSION}/blockchains"
        return self.get(url)

    def get_collection_ids(self):
        url = f"{self.HOST}/{self.VERSION}/collections"
        return self.get(url)

    def get_daily_blockchain_summary(self, blockchain_id: str, params: dict):
        """
        :blockchain_id: name of blockchain (e.g. ethereum, polygon, flow, immutablex, etc.)
        :params: dictionary of dates with keys startAt, endAt
        :return:
        """
        url = f"{self.HOST}/{self.VERSION}/blockchains/{blockchain_id}/daily-sales-summary"
        return self.get(url, params=params)

    def get_top_100_collections(self, time_range: str = 'day'):
        """
        :param time_range: day, week, month, all
        :return: top 100 collections
        """
        url = f"{self.HOST}/{self.VERSION}/collections/top-100?timeRange={time_range}"
        return self.get(url)

    def get_global_blockchain_index(self, time_range: str = 'day'):
        """
        :param time_range: time_range: day, week, month, all
        :return: global blockchain NFT stats
        """
        url = f"{self.HOST}/{self.VERSION}/global-indexes/sales-summary?timeRange={time_range}"
        return self.get(url)

    def get_collection_sales_summary(self, collection_id: str):
        """
        :param collectionid: id of collections returned from collection_ids endpoint (e.g. "azuki")
        :return: Sales stats 24hr
        """
        url = f"{self.HOST}/{self.VERSION}/collections/{collection_id}/sales-summary"
        return self.get(url)
