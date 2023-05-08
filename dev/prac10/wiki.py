import wikipedia

while True:
    search_phrase = input("Enter a page title or search phrase (blank to quit): ")
    if search_phrase == "":
        break

    try:
        page = wikipedia.page(search_phrase, auto_suggest=False)
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation Error: {e}")
