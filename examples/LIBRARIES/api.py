import requests

def main():
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search"
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        return
    
    json_res = response.json()

    for artwork in json_res["data"]:
        print(f"* {artwork["title"]}")

if __name__ == "__main__":
    main()