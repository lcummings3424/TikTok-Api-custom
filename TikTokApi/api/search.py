from __future__ import annotations
from urllib.parse import urlencode
from typing import TYPE_CHECKING, AsyncIterator
from .user import User
from ..exceptions import InvalidResponseException

if TYPE_CHECKING:
    from ..tiktok import TikTokApi


class Search:
    """Contains static methods about searching TikTok for a phrase."""

    parent: TikTokApi

    @staticmethod
    async def users(search_term, count=10, cursor=0, **kwargs) -> AsyncIterator[User]:
        """
        Searches for users.

        Note: Your ms_token needs to have done a search before for this to work.
        """
        async for user in Search.search_type(
            search_term, "user", count=count, cursor=cursor, **kwargs
        ):
            yield user

    @staticmethod
    async def videos(search_term, count=10, cursor=0, **kwargs) -> AsyncIterator:
        """
        Searches for videos matching a keyword.

        Args:
            search_term (str): Search keyword.
            count (int): Number of videos to retrieve.
            cursor (int): Cursor for pagination.

        Yields:
            TikTokApi.video objects
        """
        async for video in Search.search_type(
            search_term, "item", count=count, cursor=cursor, **kwargs
        ):
            yield video

    @staticmethod
    async def search_type(
        search_term, obj_type, count=10, cursor=0, **kwargs
    ) -> AsyncIterator:
        """
        Searches for a specific type of object ("user" or "item").

        Args:
            search_term (str): The search keyword.
            obj_type (str): "user" or "item".
            count (int): Number of results.
            cursor (int): Pagination cursor.

        Yields:
            TikTokApi.user or TikTokApi.video objects.
        """
        found = 0
        while found < count:
            params = {
                "keyword": search_term,
                "cursor": cursor,
                "count": 12,
                "from_page": "search",
                "web_search_code": (
                    """{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}"""
                    if obj_type == "user"
                    else None
                ),
            }

            # Remove None keys
            params = {k: v for k, v in params.items() if v is not None}

            resp = await Search.parent.make_request(
                url=f"https://www.tiktok.com/api/search/{obj_type}/full/",
                params=params,
                headers=kwargs.get("headers"),
                session_index=kwargs.get("session_index"),
            )

            if resp is None:
                raise InvalidResponseException(
                    resp, "TikTok returned an invalid response."
                )

            if obj_type == "user":
                for user in resp.get("user_list", []):
                    sec_uid = user.get("user_info").get("sec_uid")
                    uid = user.get("user_info").get("user_id")
                    username = user.get("user_info").get("unique_id")
                    yield Search.parent.user(
                        sec_uid=sec_uid, user_id=uid, username=username
                    )
                    found += 1

            elif obj_type == "item":
                for video in resp.get("item_list", []):
                    yield Search.parent.video(data=video)
                    found += 1

            if not resp.get("has_more", False):
                return

            cursor = resp.get("cursor", cursor + 12)
