from typing import Type

from .utils.api import BaseApi
from .utils.consts import MEUrlBuilder
from .utils.types import MagicEdenAPIEnvironment


class MagicEdenOfficialApi(BaseApi):
    url_builder_class: Type[MEUrlBuilder]
    url_builder: MEUrlBuilder

    def __init__(self, environment: MagicEdenAPIEnvironment = 'MAINNET', request_kwargs: dict = None):
        default_headers = {'ME-Pub-API-Metadata': '{"paging":true}'}
        super(MagicEdenOfficialApi, self).__init__(request_kwargs={
            "headers": default_headers,
            **(request_kwargs or {})
        })
        self.url_builder = self.url_builder_class(environment)
