#!/usr/bin/python3
"""This script queries the Reddit API
parses title of all hot articles, & prints sorted count of given keywords"""
import requests
from collections import Counter
import re


def count_words(subreddit, word_list, after=None, word_count=None):
    """recursive function that queries the Reddit API,
    parses title of all hot articles, prints sorted count of given keywords"""
    if word_count is None:
        word_count = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyRedditApp/0.1)'}
    params = {'limit': 100}

    # adding 'after' param.
    if after:
        params['after'] = after

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            # counting occurrences of each keyword
            for post in posts:
                title = post['data']['title'].lower()
                words_in_title = re.findall(r'\b\w+\b', title)
                for word in word_list:
                    word_lower = word.lower()
                    word_count[word_lower] += words_in_title.count(word_lower)

            # Check for a next page
            if data['data']['after']:
                return count_words(
                    subreddit, word_list, data['data']['after'], word_count)
            else:
                # Sort
                sorted_word_count = sorted(
                    word_count.items(), key=lambda item: (-item[1], item[0]))
                for word, count in sorted_word_count:
                    if count > 0:
                        print('{}: {}'.format(word[0], word[1]))
                return
        else:
            return
    except requests.RequestException:
        return

count_words("python", ["Python", "javascript", "java", "C++", "Go"])
