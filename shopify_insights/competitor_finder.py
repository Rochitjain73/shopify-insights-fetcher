# competitor_finder.py

def get_competitor_urls(brand_url):
    # This is a basic mock; in production, you'd use an API like SerpAPI or scrape search engines.
    mock_competitors = {
        "https://memy.co.in": [
            "https://hairoriginals.com",
            "https://nolabels.in",
            "https://snitch.co.in"
        ],
        "https://hairoriginals.com": [
            "https://memy.co.in",
            "https://urbanic.com",
            "https://styched.in"
        ]
    }
    return mock_competitors.get(brand_url, [])