import wikipedia


def main():

    page_title = input("Input the page title: ")
    while page_title != " ":
        try:
            page = wikipedia.page(page_title, auto_suggest=False)
            print(page.title)
            print(page.summary.strip())
            print(page.url)

        except wikipedia.DisambiguationError:
            # Disambiguation
            print("We need a more specific title. Try one of the following, or a new search:")
            print(wikipedia.search(page_title))




main()
