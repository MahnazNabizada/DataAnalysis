import pandas as pd
import requests
from io import StringIO

URL = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)

tables = pd.read_html(StringIO(response.text))

df = tables[2]
print(df)
