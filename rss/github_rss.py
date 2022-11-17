from urllib.parse import urlparse, urljoin

def fixup_github_link(log, url):
    try:
        parsed_uri = urlparse(url)
        hostname = '{uri.netloc}'.format(uri=parsed_uri)
        if hostname.endswith("github.com") and not "tags.atom" in url:
            return urljoin(f"{url}/", "tags.atom")
    except:
        log.exception(f"Processing GitHub URL '{url}' failed")
    return url
