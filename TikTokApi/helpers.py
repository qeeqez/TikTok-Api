from .exceptions import *

import requests
import random


def extract_video_id_from_url(url, headers={}, proxy=None):
    url = requests.head(
        url=url, allow_redirects=True, headers=headers, proxies=proxy
    ).url
    if "@" in url and "/video/" in url:
        return url.split("/video/")[1].split("?")[0]
    else:
        raise TypeError(
            "URL format not supported. Below is an example of a supported url.\n"
            "https://www.tiktok.com/@therock/video/6829267836783971589"
        )


def random_choice(choices: list):
    """Return a random choice from a list, or None if the list is empty"""
    if choices is None or len(choices) == 0:
        return None
    return random.choice(choices)

def requests_cookie_to_playwright_cookie(req_c):
    c = {
        'name': req_c.name,
        'value': req_c.value,
        'domain': req_c.domain,
        'path': req_c.path,
        'secure': req_c.secure
    }
    if req_c.expires:
        c['expires'] = req_c.expires
    return c

def shuffle_ms_token(ms_token: str) -> str:
    """
    Shuffles symbols in a msToken string.

    Args:
      ms_token: The msToken string to shuffle.

    Returns:
      The shuffled msToken string.
    """
    try:
        # Split the msToken into three parts
        part1, part2 = ms_token.split("-")
        part2 = part2.replace("=", "")

        # Shuffle the characters in the first and second parts
        part1 = list(part1)
        random.shuffle(part1)
        part1 = ''.join(part1)  # Join the list back into a string

        part2 = list(part2)
        random.shuffle(part2)
        part2 = ''.join(part2)  # Join the list back into a string

        # Reconstruct the shuffled msToken
        shuffled_ms_token = f"{part1}-{part2}="
        return shuffled_ms_token
    except ValueError:
        print("Invalid msToken format. Please provide a valid msToken.")
        return ms_token
