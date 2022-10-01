from typing import Dict, List

from magic_eden.api.base import MagicEdenOfficialApi
from magic_eden.api.utils.consts import MEAPITokensUrlBuilder
from magic_eden.api.utils.data import list_map
from magic_eden.api.utils.data import token_response_mapper, listing_response_mapper, \
    offer_response_mapper, activity_response_mapper
from magic_eden.api.utils.types import METoken, MEListingItem, MEOffer, MEActivity


class MagicEdenTokensApi(MagicEdenOfficialApi):
    url_builder_class = MEAPITokensUrlBuilder
    url_builder: MEAPITokensUrlBuilder

    def get_token_dirty(
            self,
            token: str,
            request_kwargs: dict = None
    ) -> Dict:
        url = self.url_builder.get_token(token)
        return self._get_request(url, request_kwargs=request_kwargs)

    def get_token(
            self,
            token: str,
            request_kwargs: dict = None
    ) -> METoken:
        dirty = self.get_token_dirty(token, request_kwargs=request_kwargs)
        if dirty:
            return token_response_mapper(dirty)

    def listings_dirty(
            self,
            token: str,
            request_kwargs: dict = None
    ) -> List[Dict]:
        url = self.url_builder.listings(token)
        return self._get_request(url, request_kwargs=request_kwargs)

    def listings(
            self,
            token: str,
            request_kwargs: dict = None
    ) -> List[MEListingItem]:
        dirty = self.listings_dirty(token, request_kwargs=request_kwargs)
        return list_map(listing_response_mapper, dirty)

    def offer_received_dirty(
            self,
            token: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[Dict]:
        url = self.url_builder.offer_received(token, offset, limit)
        return self._get_request(url, request_kwargs=request_kwargs)

    def offer_received(
            self,
            token: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[MEOffer]:
        dirty = self.offer_received_dirty(token, offset, limit, request_kwargs=request_kwargs)
        return list_map(offer_response_mapper, dirty)

    def activities_dirty(
            self,
            token: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[Dict]:
        url = self.url_builder.activities(token, offset, limit)
        return self._get_request(url, request_kwargs=request_kwargs)

    def activities(
            self,
            token: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[MEActivity]:
        dirty = self.activities_dirty(token, offset, limit, request_kwargs=request_kwargs)
        return list_map(activity_response_mapper, dirty)
