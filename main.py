from ohmysportsfeedspy import MySportsFeeds

def main():
    # Request

    print("Sending request")

    api_key = "6d3ad11f-3056-4129-89e0-51b18b"
    season = "2024-regular"
    format = "csv"

    msf = MySportsFeeds(version="2.0")

    msf.authenticate(api_key, "MYSPORTSFEEDS")

    output = msf.msf_get_data(league="mlb", season=season, feed="seasonal_games", format=format)

    print(output)


if __name__ == '__main__':
    main()