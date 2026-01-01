import requests
import json
import sys

def main():
    
    if len(sys.argv) != 2:
        sys.exit()

    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
    
    json_res = response.json()

    for result in json_res["results"]:
        print(result["trackName"])

main()