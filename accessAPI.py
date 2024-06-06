import requests


def get_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return None


def main():
    while True:
        print("Welcome to the Book of Mormon Summary Tool!")
        book = input("Which book of the Book of Mormon would you like? ")
        chapter_API = input(f"Which chapter of {book.title()} are you interested in? ")
        book_API = book.lower().replace(" ", "")
        json_data = get_json(
            f"https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/{book_API}/{chapter_API}"
        )

        if json_data is not None:
            print(f"Here is a summary of {book.title()} chapter {chapter_API}: ")
            print(json_data["chapter"]["summary"])
        else:
            print("Failed to retrieve JSON data from the API.")

        again = input("Would you like to view another (Y/N)? ")
        if again.lower() == "n":
            break


if __name__ == "__main__":
    main()
