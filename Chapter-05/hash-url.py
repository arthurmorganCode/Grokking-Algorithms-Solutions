cache = dict()

def check(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
    

def get_data_from_server(url):
    return f"Data from {url}"