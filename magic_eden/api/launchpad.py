from typing import List, Dict

from magic_eden.api.base import MagicEdenOfficialApi
from magic_eden.api.utils.consts import MEAPILaunchpadUrlsBuilder
from magic_eden.api.utils.data import launchpad_collection_mapper
from magic_eden.api.utils.data import list_map
from magic_eden.api.utils.types import MELaunchpadCollection


class MagicEdenLaunchpadApi(MagicEdenOfficialApi):
    url_builder_class = MEAPILaunchpadUrlsBuilder
    url_builder: MEAPILaunchpadUrlsBuilder

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
    ) -> List[MELaunchpadCollection]:
        dirty = self.collections_dirty(offset, limit, request_kwargs=request_kwargs)
        return list_map(launchpad_collection_mapper, dirty)
