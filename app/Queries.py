
QUERY_REPOS = "https://github.com/search?o={ORDER}&p={PAGE}&q={QUERY}&s={STATE}&type={TYPE}"
QUERY_REPOS_JSON = "https://api.github.com/search/repositories?o=desc&p=1&q=Discord+bot&s=updated&type=Repositories"

QUERY_REPO = "https://github.com/{USER}/{REPO}"
QUERY_REPO_FOLDER = QUERY_REPO + "/tree/{BRANCH}/{PATH}"
QUERY_REPO_FILE = QUERY_REPO + "/blob/{BRANCH}/{PATH}"
QUERY_REPO_FILE_RAW = "https://raw.githubusercontent.com/{USER}/{REPO}/blob/{BRANCH}/{PATH}"