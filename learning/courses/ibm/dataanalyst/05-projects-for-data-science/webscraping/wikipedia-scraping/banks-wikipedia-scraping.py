import pandas as pd
import requests
from io import StringIO

URL = "https://en.wikipedia.org/wiki/List_of_largest_banks"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

tables = pd.read_html(StringIO(response.text))

df = tables[0]
print(df)