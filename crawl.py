import glob
import requests
from bs4 import BeautifulSoup
import os
import tqdm

file_list = glob.glob('solutions/*')

for file in tqdm.tqdm(file_list):
    # The URL of the specific LeetCode problem
    url = 'https://leetcode.com/problems/' + ('-'.join(file.lower().split(' ')[1:]))

    # Send a request to get the content of the page
    # Send a request to get the content of the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    meta_tags = soup.find_all('meta')
    question_string = ''
    # Search through the list of tags to find the one with the desired content.
    for tag in meta_tags:
        if 'name' in tag.attrs and tag.attrs['name'] == 'description':
            # If a "content" attribute is present, print its value
            if 'content' in tag.attrs:
                question_string += tag.attrs['content']
                break
    f = open(os.path.join(file, 'question.txt'), 'w')
    f.write(question_string)
    f.close()