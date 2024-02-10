import requests
from bs4 import BeautifulSoup

def scrape_reddit(url):
    # Define headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    # Send a GET request to the subreddit URL with headers
    response = requests.get(url, headers=headers)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all the posts
    posts = soup.find_all('shreddit-post')
    print(soup)

    # Iterate through each post and extract relevant information
    for post in posts:
        # Extract title
        title = post.find('a', class_='block font-semibold text-neutral-content-strong m-0 visited:text-neutral-content-weak text-14 xs:text-18 grow  mb-xs ').text.strip()
        # Extract link
        link = post.find('a', class_='block font-semibold text-neutral-content-strong m-0 visited:text-neutral-content-weak text-14 xs:text-18 grow  mb-xs ')['href']
        # Extract subreddit name
        subreddit_name = post['subreddit-prefixed-name']
        # Extract author
        author = post.find('span', class_='whitespace-nowrap').text.strip()
        # Extract domain
        domain = post['domain']
        # Extract comment count
        comment_count = post['comment-count']
        # Extract score
        score = post['score']
        
        # Print extracted information
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Subreddit Name: {subreddit_name}")
        print(f"Author: {author}")
        print(f"Domain: {domain}")
        print(f"Comment Count: {comment_count}")
        print(f"Score: {score}")
        print("\n")

if __name__ == "__main__":
    # URL of the subreddit
    subreddit_url = "https://www.reddit.com/r/CryptoCurrency/"
    scrape_reddit(subreddit_url)
