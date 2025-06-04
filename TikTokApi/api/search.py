from __future__ import annotations
from urllib.parse import urlencode
from typing import TYPE_CHECKING, AsyncIterator, List, Tuple
from .user import User
from ..exceptions import InvalidResponseException

if TYPE_CHECKING:
    from ..tiktok import TikTokApi


class Search:
    """Contains static methods about searching TikTok for a phrase."""

    parent: TikTokApi

    @staticmethod
    async def users(
        search_term: str, count: int = 10, cursor: int = 0, **kwargs
    ) -> Tuple[List[User], int | None]:
        """
        Search for users matching the keyword.

        Args:
            search_term (str): Keyword to search for.
            count (int): Number of results.
            cursor (int): Pagination cursor.

        Returns:
            A tuple of (list of Users, next_cursor).
        """
        return await Search.search_type(
            search_term, "user", count=count, cursor=cursor, **kwargs
        )

    @staticmethod
    async def videos(
        search_term: str, count: int = 10, cursor: int = 0, **kwargs
    ) -> Tuple[List, int | None]:
        """
        Search for videos matching the keyword.

        Args:
            search_term (str): Keyword to search for.
            count (int): Number of results.
            cursor (int): Pagination cursor.

        Returns:
            A tuple of (list of Videos, next_cursor).
        """
        return await Search.search_type(
            search_term, "item", count=count, cursor=cursor, **kwargs
        )

    @staticmethod
    async def search_type(
        search_term: str,
        obj_type: str,
        count: int = 10,
        cursor: int = 0,
        **kwargs,
    ) -> Tuple[List, int | None]:
        """
        Core search function that hits the TikTok search API for either 'user' or 'item' (video).

        Args:
            search_term (str): The search keyword.
            obj_type (str): Either "user" or "item".
            count (int): Number of items to retrieve.
            cursor (int): Pagination cursor.

        Returns:
            Tuple of (results list, next_cursor or None)
        """
        params = {
            "keyword": search_term,
            "cursor": cursor,
            "count": count,
            "from_page": "search",
            "web_search_code": (
                """{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}"""
                if obj_type == "user"
                else None
            ),
        }

        # Remove keys with None values
        params = {k: v for k, v in params.items() if v is not None}

        resp = await Search.parent.make_request(
            url=f"https://www.tiktok.com/api/search/{obj_type}/full/",
            params=params,
            headers=kwargs.get("headers"),
            session_index=kwargs.get("session_index"),
        )

        if resp is None:
            raise InvalidResponseException(resp, "TikTok returned an invalid response.")

        results = []

        if obj_type == "user":
            for user in resp.get("user_list", []):
                user_info = user.get("user_info", {})
                results.append(
                    Search.parent.user(
                        sec_uid=user_info.get("sec_uid"),
                        user_id=user_info.get("user_id"),
                        username=user_info.get("unique_id"),
                    )
                )

        elif obj_type == "item":
            for video in resp.get("item_list", []):
                results.append(Search.parent.video(data=video))

        next_cursor = resp.get("cursor")
        has_more = resp.get("has_more", False)

        return results, next_cursor if has_more else None
