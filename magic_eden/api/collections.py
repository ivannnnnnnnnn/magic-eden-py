from typing import List, Dict

from magic_eden.api.base import MagicEdenOfficialApi
from magic_eden.api.utils.consts import MEAPICollectionsUrlsBuilder
from magic_eden.api.utils.data import listing_response_mapper, activity_response_mapper, \
    collection_stats_mapper, list_map, collections_response_mapper
from magic_eden.api.utils.types import MECollection, MEActivity, MECollectionStats, MEListingItem


class MagicEdenCollectionsApi(MagicEdenOfficialApi):
    url_builder_class = MEAPICollectionsUrlsBuilder
    url_builder: MEAPICollectionsUrlsBuilder

    def collections_dirty(
            self,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[Dict]:
        url = self.url_builder.collections(offset, limit)
        return self._get_request(url, request_kwargs=request_kwargs)

    def collections(
            self,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[MECollection]:
        dirty = self.collections_dirty(offset, limit, request_kwargs=request_kwargs)
        return list_map(collections_response_mapper, dirty)

    def listings_dirty(
            self,
            symbol: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[Dict]:
        url = self.url_builder.listings(symbol, offset, limit)
        return self._get_request(url, request_kwargs=request_kwargs)

    def listings(
            self,
            symbol: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[MEListingItem]:
        dirty = self.listings_dirty(symbol, offset, limit, request_kwargs=request_kwargs)
        return list_map(listing_response_mapper, dirty)

    def activities_dirty(
            self,
            symbol: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[Dict]:
        url = self.url_builder.activities(symbol, offset, limit)
        return self._get_request(url, request_kwargs=request_kwargs)

    def activities(
            self,
            symbol: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[MEActivity]:
        dirty = self.activities_dirty(symbol, offset, limit, request_kwargs=request_kwargs)
        return list_map(activity_response_mapper, dirty)

    def stats_dirty(
            self,
            symbol: str,
            request_kwargs: dict = None
    ) -> Dict:
        url = self.url_builder.stats(symbol)
        return self._get_request(url, request_kwargs=request_kwargs)

    def stats(
            self,
            symbol,
            request_kwargs: dict = None
    ) -> MECollectionStats:
        dirty = self.stats_dirty(symbol, request_kwargs=request_kwargs)
        return None if dirty is None else collection_stats_mapper(dirty)
