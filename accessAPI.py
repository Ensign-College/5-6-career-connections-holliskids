import requests
import json

while(True):
    base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

    print("Welcome to the Book of Mormon Summary Tool!")
    book = input("Which book of the Book of Mormon would you like? ")
    chapter = input(f"Which chapter of {book} are you interested in? ")

    req_url = base_url + (book.lower()).replace(" ", "") + '/' + chapter.replace(" ", "")
    # print(req_url)

    response = requests.get(req_url)  # Use the url string to ask for the content
    data = response.json()  #We want the data returned as json

    print(f"Summary of {book} chapter {chapter}:")
    print(data['chapter']['summary'],"\n")  # Within the 'chapter' value we have additional keys

    loop = input("Would you like to view another (Y/N)? ")
    if (loop.upper() == 'N'):
        break

