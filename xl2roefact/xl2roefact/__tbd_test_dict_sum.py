

def dict_sum_by_key(
    search_dict: dict,
    sum_key: str
) -> float:
    """Sum all dictionary items for a given key.
    
    Dictionary is traversed at all depth levels.
    """
    s = 0
    for k in search_dict:
        if isinstance(search_dict[k], dict):
            s += dict_sum_by_key(search_dict[k], sum_key)
        if k == sum_key:
            try: kval = float(search_dict[k])
            except: kval = 0
            s += kval    
    return float(s)


test_data = {
    "k1": 2.0,
    "set2": {
        "k1"; 2.0
    },
    "set3": {
        "k1": "nan"
    }
}


if __name__ == "__main__":
    x = dict_sum_by_key(test_data, "k1")
    print(x)


