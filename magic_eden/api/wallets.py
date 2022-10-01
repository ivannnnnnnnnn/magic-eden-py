from typing import List, Dict

from magic_eden.api.base import MagicEdenOfficialApi
from magic_eden.api.utils.consts import MEAPIWalletUrlsBuilder
from magic_eden.api.utils.data import list_map
from magic_eden.api.utils.data import token_response_mapper, activity_response_mapper, \
    offer_response_mapper, \
    escrow_balance_response_mapper
from magic_eden.api.utils.types import MEActivity, METoken, MEOffer, MEEscrowBalance


class MagicEdenWalletsApi(MagicEdenOfficialApi):
    url_builder_class = MEAPIWalletUrlsBuilder
    url_builder: MEAPIWalletUrlsBuilder

    def tokens_dirty(
            self,
            wallet_address: str,
            offset: int = 0,
            limit: int = 100,
            listed_only: bool = False,
            request_kwargs: dict = None
    ) -> List[Dict]:
        url = self.url_builder.tokens(wallet_address, offset, limit, listed_only)
        return self._get_request(url, request_kwargs=request_kwargs)

    def tokens(
            self,
            wallet_address: str,
            offset: int = 0,
            limit: int = 100,
            listed_only: bool = False,
            request_kwargs: dict = None
    ) -> List[METoken]:
        dirty = self.tokens_dirty(wallet_address, offset, limit, listed_only, request_kwargs=request_kwargs)
        return list_map(token_response_mapper, dirty)

    def activities_dirty(
            self,
            wallet_address: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[Dict]:
        url = self.url_builder.activities(wallet_address, offset, limit)
        return self._get_request(url, request_kwargs=request_kwargs)

    def activities(
            self,
            wallet_address: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[MEActivity]:
        dirty = self.activities_dirty(wallet_address, offset, limit, request_kwargs=request_kwargs)
        return list_map(activity_response_mapper, dirty)

    def offers_made_dirty(
            self,
            wallet_address: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[Dict]:
        url = self.url_builder.offers_made(wallet_address, offset, limit)
        return self._get_request(url, request_kwargs=request_kwargs)

    def offers_made(
            self,
            wallet_address: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[MEOffer]:
        dirty = self.offers_made_dirty(wallet_address, offset, limit, request_kwargs=request_kwargs)
        return list_map(offer_response_mapper, dirty)

    def offers_received_dirty(
            self,
            wallet_address: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[Dict]:
        url = self.url_builder.offers_received(wallet_address, offset, limit)
        return self._get_request(url, request_kwargs=request_kwargs)

    def offers_received(
            self,
            wallet_address: str,
            offset: int = 0,
            limit: int = 100,
            request_kwargs: dict = None
    ) -> List[MEOffer]:
        dirty = self.offers_received_dirty(wallet_address, offset, limit, request_kwargs=request_kwargs)
        return list_map(offer_response_mapper, dirty)

    def escrow_balance_dirty(
            self,
            wallet_address: str,
            request_kwargs: dict = None
    ) -> Dict:
        url = self.url_builder.escrow_balance(wallet_address)
        return self._get_request(url, request_kwargs=request_kwargs)

    def escrow_balance(
            self,
            wallet_address: str,
            request_kwargs: dict = None
    ) -> MEEscrowBalance:
        dirty = self.escrow_balance_dirty(wallet_address, request_kwargs=request_kwargs)
        if dirty:
            return escrow_balance_response_mapper(dirty)
