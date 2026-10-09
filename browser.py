import webbrowser


def open_website(command):

    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    return "Website not found"


def google_search(query):
    
    search = query.replace("search", "")
    url = "https://www.google.com/search?q=" + search

    webbrowser.open(url)

    return f"Searching Google for {search}"