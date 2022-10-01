import abc
import logging
from http import HTTPStatus
from json.decoder import JSONDecodeError
from typing import Optional, Dict, Union, List

import requests

logger = logging.getLogger(__name__)


class BaseApi(abc.ABC):
    def __init__(self, request_kwargs: dict = None):
        self._request_kwargs = request_kwargs
        self.request = None

    def _get_request(self, url: str, request_kwargs: dict = None) -> Union[Optional[Dict], Optional[List]]:
        req = requests.get(url, **{
            **self._request_kwargs,
            **(request_kwargs or {})
        })
        try:
            if req.status_code == HTTPStatus.OK:
                return req.json()
            logger.error(f'Request error. Status code: {req.status_code}')
        except JSONDecodeError as je:
            logger.error(f'Request error. Failed to parse json data. {str(je)}')
            return None
        except Exception as e:
            logger.error(f'Request error. {str(e)}')
        finally:
            self.request = req
