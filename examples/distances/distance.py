distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}

def main():
    print(distances.keys()) # dict_keys(['Voyager 1', 'Voyager 2', 'Pioneer 10', 'New Horizons', 'Pioneer 11'])
    
    for distance_key in distances: # by default, iterating over a dict iterates over its keys, so it prints the keys in new lines
        print(distance_key);
    for name in distances.keys(): # same as above
        print(f"{name} is {distances.get(name, 'Unknown')} AU from Earth.");

    # I want to try and change the values of distances in the dictionary to meters
    # to change the value of a key in a dictionary, you can do:
    # distances[key_name] = value;

    for name in distances:
        distances[name] = convert_to_meters(distances[name]);
    print(distances)

def convert_to_meters(au):
    return au * 149597870700;

if __name__ == "__main__":
    main()