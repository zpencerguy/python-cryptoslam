# CryptoSlam NFT API Python 3 wrapper
This an API wrapper library for the [CryptoSlam API](https://cryptoslam.gitbook.io/api-documentation/) written in Python 3.

The library provides a simplified interface to get NFT data indexed by CryptoSlam.

## Supported endpoints
The wrapper covers the following CryptoSlam API endpoints:

* Blockchains ([/blockchains](https://cryptoslam.gitbook.io/api-documentation/blockchains/get-blockchain-id))
* Collections ([/collections](https://cryptoslam.gitbook.io/api-documentation/collections/get-all-nft-collections))


## Prerequisite
You need to have an **API key** to use the full set of endpoints, but some endpoints are free. [You can request a key here.](https://developer.cryptoslam.io/) <br><br>


## Installation
Install with pip:
```bash
virtualenv env && source env/bin/activate
pip install .
```


## Usage examples

```python
# import the CryptoslamAPI object from the cryptoslam module
from cryptoslam import CryptoslamAPI

# create an object to interact with the CryptoSlam API (need an api key)
api = CryptoslamAPI(api_key="my-api-key")

# fetch supported blockchains
blockchain_ids = api.get_blockchain_ids()

# fetch supported collections
collection_ids = api.get_collection_ids()

```


## Documentation
* [CryptoSlam API documentation](https://cryptoslam.gitbook.io/api-documentation/)

