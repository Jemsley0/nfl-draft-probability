# %% import packages
import pandas as pd
import numpy as np
import os
from pathlib import Path
from bs4 import BeautifulSoup
import requests

# set constants
export_path = Path.cwd() / "exports"

# %%
url = "https://www.pro-football-reference.com/years/2021/draft.htm"

page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.content, "html.parser")
draft_table = soup.find(id="drafts")
print(draft_table.prettify())

# %%
left_headers = list(
    [
        draft_table.find_all(class_="left")[0].get_text(),
        draft_table.find_all(class_="left")[1].get_text(),
        draft_table.find_all(class_="left")[2].get_text(),
    ]
)

for i in :
    team = draft_table.find_all(class_='left')[3*1].get_text()
    player = draft_table.find_all(class_='left')[4*1].get_text()
    pos = draft_table.find_all(class_='left')[5*1].get_text()

round = 1
pick = 1
age = 1
to = 1

# %%
