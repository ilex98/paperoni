from habanero import Crossref
from datetime import date, timedelta

# Access polite pool
cr = Crossref(mailto="theo.driftmann@proton.me")

# Get yesterday in iso format
yesterday = (date.today() - timedelta(days=1)).isoformat()

# Query to API
results = cr.works(
    query = "ecology",
    filter={
        "from-pub-date": yesterday,
        "until-pub-date": date.today().isoformat(),
        "type": "journal-article",
    },
    sort = "indexed",
    order = "desc",
    select = "DOI,title,author,container-title,published,abstract",
    limit = 100
)

for item in results['message']['items']:
    print(item.get('title'), '-', item.get('container-title'))
