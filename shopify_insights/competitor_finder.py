
def get_competitor_urls(brand_url):

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