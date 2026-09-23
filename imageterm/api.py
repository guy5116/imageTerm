import requests
from .display import display

BASE = "https://safebooru.donmai.us"
HEADERS = {"User-Agent": "imageTerm/0.1 (https://github.com/guy5116)"}

def lookup_tag(query):
    r = requests.get(f"{BASE}/autocomplete.json",
                     params={"search[query]": query,
                             "search[type]": "tag_query",
                             "limit": 5},
                     headers=HEADERS)
    r.raise_for_status()
    results = r.json()
    return results[0]["value"] if results else None

def random_post(tag):
    r = requests.get(f"{BASE}/posts.json",
                     params={"tags": f"order:random {tag}", "limit": 1},
                     headers=HEADERS)
    r.raise_for_status()
    posts = r.json()
    return posts[0] if posts else None

def api(query):
    tag = lookup_tag(query)
    if tag is None:
        return None
    post = random_post(tag)
    if post is None:
        return None
    url = post.get("large_file_url") or post.get("file_url")
    print(url)
    display(url)
