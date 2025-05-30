# TikTokApi

The Unofficial TikTok API Wrapper In Python

This is an unofficial api wrapper for TikTok.com in python. With this api you are able to call most trending and fetch specific user information as well as much more.

## Important Information

- This API is unofficial, use at your own risk
- This API is not affiliated with TikTok in any way
- If you abuse this API TikTok may block your IP address
- Some features may be removed or changed without notice
- This API is not guaranteed to be up to date 100% of the time

[![DOI](https://zenodo.org/badge/188710490.svg)](https://zenodo.org/badge/latestdoi/188710490) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&style=flat-square)](https://www.linkedin.com/in/davidteather/) [![Sponsor Me](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub)](https://github.com/sponsors/davidteather) [![GitHub release (latest by date)](https://img.shields.io/github/v/release/davidteather/TikTok-Api)](https://github.com/davidteather/TikTok-Api/releases) [![GitHub](https://img.shields.io/github/license/davidteather/TikTok-Api)](https://github.com/davidteather/TikTok-Api/blob/main/LICENSE) [![Downloads](https://pepy.tech/badge/tiktokapi)](https://pypi.org/project/TikTokApi/) ![](https://visitor-badge.laobi.icu/badge?page_id=davidteather.TikTok-Api) [![Support Server](https://img.shields.io/discord/783108952111579166.svg?color=7289da&logo=discord&style=flat-square)](https://discord.gg/yyPhbfma6f)

This api is designed to **retrieve data** TikTok. It **can not be used post or upload** content to TikTok on the behalf of a user. It has **no support for any user-authenticated routes**, if you can't access it while being logged out on their website you can't access it here.

## Sponsors

These sponsors have paid to be placed here or are my own affiliate links which I may earn a commission from, and beyond that I do not have any affiliation with them. The TikTokAPI package will always be free and open-source. If you wish to be a sponsor of this project check out my [GitHub sponsors page](https://github.com/sponsors/davidteather).

<div align="center">
    <a href="https://tikapi.io/?ref=davidteather" target="_blank">
        <img src="https://raw.githubusercontent.com/davidteather/TikTok-Api/main/imgs/tikapi.png" width="100" alt="TikApi">
        <div>
            <b>TikAPI</b> is a paid TikTok API service providing a full out-of-the-box solution, making life easier for developers — trusted by 500+ companies.
        </div>
    </a>
    <br>
    <a href="https://www.ensembledata.com/?utm_source=github&utm_medium=githubpage&utm_campaign=david_thea_github&utm_id=david_thea_github" target="_blank">
        <img src="https://raw.githubusercontent.com/davidteather/TikTok-Api/main/imgs/EnsembleData.png" width="100" alt="Ensemble Data">
        <b></b>
        <div>
         <b>EnsembleData</b> is the leading API provider for scraping Tiktok, Instagram, Youtube, and more. <br> Trusted by the major influencer marketing and social media listening platforms.
        </div>
    </a>
    <br>
    <a href="https://www.sadcaptcha.com?ref=davidteather" target="_blank">
        <img src="https://raw.githubusercontent.com/davidteather/TikTok-Api/main/imgs/tiktok_captcha_solver.png" width="100" alt="TikTok Captcha Solver">
        <b></b>
        <div>
         <b>TikTok Captcha Solver: </b> Bypass any TikTok captcha in just two lines of code.<br> Scale your TikTok automation and get unblocked with SadCaptcha.
        </div>
    </a>
    <br>
    <a href="https://www.webshare.io/?referral_code=3x5812idzzzp" target="_blank">
        <img src="https://raw.githubusercontent.com/davidteather/TikTok-Api/main/imgs/webshare.png" width="100" alt="TikTok Captcha Solver">
        <b></b>
        <div>
         <b>Cheap, Reliable Proxies: </b> Supercharge your web scraping with fast, reliable proxies. Try 10 free datacenter proxies today!
        </div>
    </a>
</div>

## Table of Contents

- [Documentation](#documentation)
- [Getting Started](#getting-started)
  - [How to Support The Project](#how-to-support-the-project)
  - [Installing](#installing)
  - [Common Issues](#common-issues)
- [Quick Start Guide](#quick-start-guide)
  - [Examples](https://github.com/davidteather/TikTok-Api/tree/main/examples)

[**Upgrading from V5 to V6**](#upgrading-from-v5-to-v6)

## Documentation

You can find the full documentation [here](https://davidteather.github.io/TikTok-Api)

## Getting Started

To get started using this api follow the instructions below.

**Note:** If you want to learn how to web scrape websites check my [free and open-source course for learning everything web scraping](https://github.com/davidteather/everything-web-scraping)

### How to Support The Project

- Star the repo 😎
- Consider [sponsoring](https://github.com/sponsors/davidteather) me on GitHub
- Send me an email or a [LinkedIn](https://www.linkedin.com/in/davidteather/) message telling me what you're using the API for, I really like hearing what people are using it for.
- Submit PRs for issues :)

### Installing

If you run into an issue please check the [Closed Pull Requests](https://github.com/davidteather/TikTok-Api/pulls?q=is%3Apr+is%3Aclosed) and [Closed Issues](https://github.com/davidteather/TikTok-Api/issues?q=is%3Aissue+is%3Aclosed) before creating a new one. There may be an answer there.

```bash
# Install TikTokApi
pip install TikTokApi
# Install Chrome for Patchright
patchright install chrome
```

### Docker

```bash
# Build the container
docker build -t tiktokapi .

# Run the container
docker run -it tiktokapi
```

### Common Issues

Please don't open an issue if you're experiencing one of these...

- **Browser Has no Attribute** - make sure you ran `patchright install chrome`, if your error persists try the [patchright-python](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-python) quickstart guide and diagnose issues from there.

## Quick Start Guide

Here's a quick bit of code to get the most recent trending videos on TikTok. There's more examples in the [examples](https://github.com/davidteather/TikTok-Api/tree/main/examples) directory.

**Note:** If you want to learn how to web scrape websites check my [free and open-source course for web scraping](https://github.com/davidteather/web-scraping-with-reverse-engineering)

```py
from TikTokApi import TikTokApi
import asyncio
import os

ms_token = os.environ.get("ms_token", None) # get your own ms_token from your cookies on tiktok.com

async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, browser=os.getenv("TIKTOK_BROWSER", "chromium"))
        async for video in api.trending.videos(count=30):
            print(video)
            print(video.as_dict)

if __name__ == "__main__":
    asyncio.run(trending_videos())
```

To directly run the example scripts from the repository root, use the `-m` option on python.

```sh
python -m examples.trending_example
```

You can access the full data dictionary the object was created from with `.as_dict`. On a video this may look like
[this](https://gist.github.com/davidteather/7c30780bbc30772ba11ec9e0b909e99d). TikTok changes their structure from time to time so it's worth investigating the structure of the dictionary when you use this package.
