# Copyright (c) 2024 Mike Chambers
# https://github.com/mikechambers/dispatch
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import argparse
import requests
import re
import subprocess
import sys

BASE_URL = "https://www.economist.com"
WEEKLY_URL = f"{BASE_URL}/weeklyedition/"

#User agent for the request to the economist
USER_AGENT = "Dispatch/1.0"

should_print_urls = False
verbose = False

SECTIONS = [
    "/the-world-this-week/",
    "/leaders/",
    "/letters/",
    "/by-invitation/",
    "/briefing/",
    "/united-states/",
    "/the-americas/",
    "/china/",
    "/middle-east-and-africa/",
    "/europe/",
    "/britain/",
    "/international/",
    "/special-report/",
    "/business/",
    "/finance-and-economics/",
    "/science-and-technology/",
    "/culture/",
    "/economic-and-financial-indicators/s",
    "/obituary/"
]

def main():
    content = load_url_content(WEEKLY_URL)

    if content is None:
        print("Could not load weekly edition info from the Economist. Aborting")
        sys.exit(1)

    urls = []

    for section in SECTIONS:
        pattern = fr'href="({section}[^\"]+)"'
        found_urls = re.findall(pattern, content)
        urls.extend(found_urls)

    if should_print_urls:
        print_urls(urls)
        sys.exit()

    add_urls_to_reader(urls)

def add_urls_to_reader(urls):

    reversed_urls = urls[::-1]

    for url in reversed_urls:

        u = f"{BASE_URL}{url}"

        script = f'tell application "Safari" to add reading list item "{u}"'

        if verbose:
            print(script)

        try:
            subprocess.run(["osascript", "-e", script], check=True)
        except Exception as e:
            print(f"Failed to add url to Reader. Skipping. : {u}")

def print_urls(urls):
    for url in urls:
        u = f"{BASE_URL}{url}"
        print(u)

def load_url_content(url):
    headers = {
        'User-Agent': USER_AGENT
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

if __name__ == "__main__":
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Add current weeks articles in The Economist to Safari reader mode.")

    parser.add_argument('--print', dest='print_urls', 
                        action='store_true', 
                        help='Runs in print mode and will only print out the urls for current issue.')
    
    parser.add_argument('--verbose', dest='verbose', 
                        action='store_true', 
                        help='Runs in print mode and will only print out the urls for current issue.')

    #pass in user_agent

    args = parser.parse_args()

    should_print_urls = args.print_urls
    verbose = args.verbose

    main()