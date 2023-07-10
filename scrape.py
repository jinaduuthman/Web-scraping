import sys
import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

if len(sys.argv) < 3:
    print("Usage: python3 scrape.py <date> <xslx>")
    exit(1)

desired_date = sys.argv[1]
outpath = sys.argv[2]

url = "https://discoveratlanta.com/events/all/"

## Your code here
result = rq.get(url)
src = result.content
soup = bs(src, "html.parser")

all_listings = soup.find("div", class_="all-listings")
all_articles = soup.find_all("article", class_="listing")

# datesearch = "2022-10-02"
titles = []
urls = []
for all_article in all_articles:
    datelists = all_article.attrs["data-eventdates"]

    if desired_date in datelists:
        links = all_article.find_all("a")
        for link in links:
            link_url = link["href"]
        title = link.text.strip()
        titles.append(title)
        urls.append(link_url)

event_data = {"Title": titles, "Link": urls}
df_events = pd.DataFrame(event_data)

with pd.ExcelWriter(outpath) as writer:
    df_events.to_excel(writer, sheet_name="Events", index=False)

    # Auto-adjust columns' width
    for column in df_events:
        column_width = max(df_events[column].astype(str).map(len).max(), len(column))
        col_idx = df_events.columns.get_loc(column)
        writer.sheets["Events"].set_column(col_idx, col_idx, column_width)
