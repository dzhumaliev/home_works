
# Эти библиотеки нужны:
# requests — качает данные из интернета.
# Например, можно получить данные с любого сайта или сервиса.

# random — делает что-то случайным.
# Например, выбрать случайный элемент из списка или перемешать его.


# 1

import requests
import random


random_url = random.choice(["https://online.geeks.kg/", "https://www.google.com/", "https://www.youtube.com/"])

def response_handler(random_url):
    response = requests.get(random_url)
    code = response.status_code

    if 200 <= code <= 299:
        return "Success"
    elif 400 <= code <= 499:
        return "Not found"
    elif code == 500:
        return "Server"
    else:
        return "Unknonw error"


print(f"{random_url} is {response_handler(random_url)}")



# 2


nums = [2, 7, 11, 15]
target = 9

def twoSum(nums: list[int], target: int) -> list[int]:

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [ i, j]
            else:
                continue

print(twoSum(nums=nums, target=target))