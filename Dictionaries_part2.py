# This is for dictionaries part 2


user_info = {
    "name": "Anoop",
    "last_name": "Singh",
    "age": 37,
    "fav_movies": ["coco", "kimi no na wa"],
    "fav_tunes": ["awakening", "fairy tale"]
}

#how to add data

user_info["fav_song"] = ["song1", "song2"]
print(user_info)

# pop() method

user_info.pop("fav_tunes")
print(user_info)


## popitem () method, this will delete random item from this given dictionary


popped_item = user_info.popitem()
print(user_info)
print(popped_item)
## update() method


user_info3 = {
    "name": "Anoop",
    "last_name": "Singh",
    "age": 37,
    "fav_movies": ["coco", "kimi no na wa"],
    "fav_tunes": ["awakening", "fairy tale"]
}

more_info = {"state": "Haryana", "hobbies": ["coding", "dancing", ], "name": "Anoop Singh"}

user_info3.update(more_info)
print(user_info3)


