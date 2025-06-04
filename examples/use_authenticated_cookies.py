import asyncio
from TikTokApi import TikTokApi


async def main():
    async with TikTokApi() as api:
        await api.create_sessions(
            num_sessions=1,
            headless=False,  # safer for stability
            sleep_after=5,
        )

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "referer": "https://www.tiktok.com/",
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "cookie": (
                "tt_chain_token=...; "
                "odin_tt=...; "
                "passport_csrf_token=...; "
                "tt_csrf_token=...; "
                "msToken=...; "
                "locale=en-US; "
                "ttwid=..."
            ),
        }

        print("Searching for videos with the term 'funny cats':")
        async for video in api.search.search_type(
            "Strike King Lure Company", obj_type="item", count=3, headers=headers
        ):
            print(
                f"Video ID: {video.id}, "
                f"Author: {video.author.username}, "
                f"Description: {video.as_dict.get('desc', '')}"
            )


if __name__ == "__main__":
    asyncio.run(main())
