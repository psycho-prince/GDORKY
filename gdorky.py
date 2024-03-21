import requests
import subprocess
import sys
from bs4 import BeautifulSoup

# Install dependencies
def install_dependencies():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google", "beautifulsoup4"])

# Check if dependencies are installed
def check_dependencies():
    try:
        import googlesearch
        import beautifulsoup4
    except ImportError:
        return False
    return True

# Function to perform Google dorking
def perform_google_dorking(query, site=None):
    search_query = query
    if site:
        search_query += f" site:{site}"
    try:
        from googlesearch import search
        results = search(search_query, num=100, stop=100, pause=2)
        return results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to search Ahmia
def search_ahmia(query):
    url = f"https://ahmia.fi/search/?q={query}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('li', class_='result')
            formatted_results = []
            for result in results:
                title = result.find('a').text.strip()
                link = result.find('a')['href']
                onion_address = result.find('cite').text.strip()
                last_seen = result.find('span', class_='lastSeen').text.strip()
                formatted_results.append({
                    'title': title,
                    'link': link,
                    'onion_address': onion_address,
                    'last_seen': last_seen
                })
            return formatted_results
        else:
            print(f"Failed to fetch search results. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to search Bing
def search_bing(query):
    url = f"https://www.bing.com/search?q={query}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('li', class_='b_algo')
            formatted_results = []
            for result in results:
                title = result.find('a').text.strip()
                link = result.find('a')['href']
                formatted_results.append({
                    'title': title,
                    'link': link,
                })
            return formatted_results
        else:
            print(f"Failed to fetch search results. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    if not check_dependencies():
        print("Installing dependencies...")
        install_dependencies()
        print("Dependencies installed successfully.")

    print("\n\x1b[31;1m█▀█ █▀█ █▀▀ █▀▀ █▄░█ █░░ █▀█ █▀▀ █▀█ █░█   █▄█ █▀█ █▀▀ █▀▀ █▀▄▀█ █▀█ ▄▀█ █▀█\x1b[0m")
    print("\x1b[31;1m█▀▄ █▄█ █▄█ █▄▄ █░▀█ █▄▄ █▀▄ ██▄ █▀▄ █▀█   ░█░ █▀▄ ██▄ █▀░ █░▀░█ █▄█ █▀█ █▀▄\x1b[0m")
    
    print("\nWelcome to Gdorky!\n")
    print("Gdorky is a tool for performing Google, Bing, and Ahmia searches.")

    while True:
        print("\nSelect a search engine:")
        print("1. Google")
        print("2. Bing")
        print("3. Ahmia")
        choice = input("Enter the number of your choice (1/2/3): ")

        if choice == '1':
            search_query = input("Enter your search query: ")
            print("\nPerforming Google Dorking...\n")
            results = perform_google_dorking(search_query)
            if results:
                print("Search Results:")
                for index, result in enumerate(results, start=1):
                    print(f"{index}. {result}")
            else:
                print("No results found.")

        elif choice == '2':
            search_query = input("Enter your search query: ")
            print("\nPerforming Bing Search...\n")
            results = search_bing(search_query)
            if results:
                print("Search Results:")
                for index, result in enumerate(results, start=1):
                    print(f"{index}. {result['title']}")
                    print(f"   Link: {result['link']}")
            else:
                print("No results found.")

        elif choice == '3':
            search_query = input("Enter your search query: ")
            print("\nPerforming Ahmia Search...\n")
            search_results = search_ahmia(search_query)
            if search_results:
                print("Search Results:")
                for index, result in enumerate(search_results, start=1):
                    print(f"{index}. {result['title']}")
                    print(f"   Link: {result['link']}")
                    print(f"   Onion Address: {result['onion_address']}")
                    print(f"   Last Seen: {result['last_seen']}")
            else:
                print("No results found.")

        choice = input("\nDo you want to perform another search? (yes/no): ")
        if choice.lower() != 'yes':
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
