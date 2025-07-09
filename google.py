import requests
import pandas as pd
from datetime import datetime

url = "https://marketplace.visualstudio.com/_apis/public/gallery/publishers/Google/extensions/geminicodeassist/reviews"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

all_reviews = []
count = 100
before_date = None  # Start with None to get newest reviews

while True:
    params = {
        "count": count,
        "filterOptions": 3
    }
    if before_date:
        params["beforeDate"] = before_date

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"❌ Failed to fetch reviews with beforeDate={before_date}")
        break

    data = response.json()
    reviews = data.get("reviews", [])
    if not reviews:
        break

    all_reviews.extend([{
        "User": r.get("userDisplayName"),
        "Rating": r.get("rating"),
        "Date": r.get("updatedDate"),
        "Version": r.get("productVersion"),
        "Review Text": r.get("text", "").strip()
    } for r in reviews])

    print(f"✅ Fetched {len(reviews)} reviews before {before_date or 'now'}")

    # Update before_date to the oldest review’s updatedDate for next batch
    oldest_date = min(r["updatedDate"] for r in reviews)
    before_date = oldest_date

    # Stop if fewer than count reviews returned (last batch)
    if len(reviews) < count:
        break

# Save to Excel
df = pd.DataFrame(all_reviews)
df.to_excel("data/Gemini Code Assist [09.07.2025].xlsx", index=False)
print(f"✅ Finished. Total {len(all_reviews)} reviews saved to Gemini Code Assist [09.07.2025].xlsx")
