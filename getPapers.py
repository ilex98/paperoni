import re
from habanero import Crossref
from datetime import date, timedelta

# Helper functions
def clean_abstract(abstract):
    if not abstract:
        return None
    text = abstract

    # Remove section title tags AND their content entirely
    text = re.sub(r'<jats:title>.*?</jats:title>', ' ', text, flags=re.DOTALL)

    # Drop italic tags but keep the species names inside
    text = re.sub(r'</?jats:italic>', '', text)

    # Strip any remaining tags
    text = re.sub(r'<[^>]+>', ' ', text)

    # Collapse ALL whitespace into single spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


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

    print("> ", item.get('title'), '-', item.get('container-title'), "\n")

    abstract = clean_abstract(item.get('abstract'))

    if abstract:
        print(abstract, "\n")
        print("-----------------------------------------------------------------------")
    else:
        print('No abstract available\n')
        print("-----------------------------------------------------------------------")

