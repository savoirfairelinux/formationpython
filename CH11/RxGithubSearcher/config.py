import os

TOKEN = "e6cb09888f6a4a24d47d9a9f2da97cdc5bd3e531"
GITHUB_API_URL = "https://api.github.com"

headers = {"Content-Type": "application/json" }
headers["Authorization"] = "token " + TOKEN
orgs = [
    "/twitter/repos",
    "/auth0/repos",
    "/nasa/repos",
    "/mozilla/repos",
    "/adobe/repos",
]
