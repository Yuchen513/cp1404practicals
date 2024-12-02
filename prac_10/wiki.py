import wikipedia


def main():

    page_title = input("Input the page title: ")
    while page_title != " ":
            page = wikipedia.page(page_title, auto_suggest=False)
            print(page.title)
            print(page.summary.strip())
            print(page.url)
main()
