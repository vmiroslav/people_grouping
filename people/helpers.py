from fuzzywuzzy import fuzz

def group_people_by_address(data):
    if not data:
        return []
    
    grouped_people = {}
    all_names = []
    for person in data:
        name, address = person.name, person.address
        matched = False
        for grouped_address in grouped_people.keys():
            similarity_score = fuzz.token_set_ratio(address, grouped_address)
            if similarity_score > 70:
                grouped_people[grouped_address].append(name)
                matched = True
                break
        if not matched:
            grouped_people[address] = [name]

    for address in grouped_people:
        all_names.append(sorted(grouped_people[address]))

    return sorted(all_names)