from Queries import *
from bs4 import BeautifulSoup
from urllib import request

def get_urls_from_search(order, page, query, state, lookup_type):
    url = QUERY_REPOS.format(ORDER=order, PAGE=page, QUERY=query, STATE=state, TYPE=lookup_type)
    result = request.urlopen(url)
    if result is None:
        return
    result = result.read()
    bs = BeautifulSoup(result)
    repo_list = bs.find_all("li", {"class": "repo-list-item"})
    return [item.find("a", {"class": "v-align-middle"})["href"] for item in repo_list]

def get_abs_urls(urls):
    gen = (url.split("/")[1:] for url in urls)
    return [ QUERY_REPO.format(USER=item[0], REPO=item[1]) for item in gen]

def crawl ():
    pass

def main():
    urls = sample()
    print("-----")
    print(get_abs_urls(urls))

def sample():
    url = QUERY_REPOS.format(ORDER= "desc", PAGE= "1", QUERY= "Discord+bot", STATE="updated", TYPE= "Repositories")
    result = request.urlopen(url)
    if result is None:
        return
    result = result.read()
    bs = BeautifulSoup(result)
    repo_list = bs.find_all("li", {"class": "repo-list-item"})
    urls = [item.find("a", {"class": "v-align-middle"})["href"] for item in repo_list]
    print("Relative Repo URL Found in Document: {}".format(urls))
    return urls

if __name__ == "__main__":
    main()