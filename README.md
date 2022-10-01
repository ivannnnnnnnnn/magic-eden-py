# Python wrap for api solana NFT marketplace MagicEden

```pip install magic-eden-py```

#### Api classes have methods corresponded to endpoints from official [docs](https://api.magiceden.dev/)


## How to use?

1. Import api class
2. Create class instance
3. Use methods of class

### Important

##### Method ended with ```_dirty``` its clear answer from marketplace

##### Other methods, contain processed data and correspond to type annotations

### Constructor of api class parameters

```environment```:

- description: Define environment for api (api-devnet.magiceden.dev, api-mainnet.magiceden.dev)
- values: 'MAINNET' | 'DEVNET'
- default: 'MAINNET'

```request_kwargs```:

- description: For make requests used python [requests](https://pypi.org/project/requests/) package,
  its parameter for add additional kwargs to requests
- values: dict
- default: ```{'headers': {'ME-Pub-API-Metadata': '{"paging":true}'}}```

```
>>> wallet_api = MagicEdenWalletsApi(
        environment = 'DEVNENT'
        requests_kwargs: dict = None
      )
```

### Also api class instance have ```request``` attribute with last request instance


## Example

```
>>> from magic_eden.api import MagicEdenCollectionsApi

>>> magic_eden_api = MagicEdenCollectionsApi()

>>> collections = magic_eden_api.collections()

>>> magic_eden_api.request   
<Response [200]>

```

### You can also import types for annotation

```
>>> from magic_eden.api.utils.types import MECollectionInfo
>>> from typings import List

>>> collections: List[MECollectionInfo] = []
```

### Official MagicEden api python wrapper classes

```
>>> from magic_eden.api import (
  MagicEdenTokensApi, 
  MagicEdenWalletsApi, 
  MagicEdenCollectionsApi, 
  MagicEdenLaunchpadApi
)  
```



