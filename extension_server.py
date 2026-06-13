"""
File: extension_server.py
---------------------
Runs the optional Bajillion web interface at http://localhost:8000.
"""

import json

import SimpleServer
from searchengine import create_index, search, textfiles_in_dir


DIRECTORY = 'bbcnews'
MAX_RESPONSES_PER_REQUEST = 10


class SearchServer:
    def __init__(self):
        """
        Loads the HTML page and builds the search index once when the
        server starts.
        """
        with open('extension_client.html', encoding='utf-8') as html_file:
            self.html = html_file.read()

        filenames = textfiles_in_dir(DIRECTORY)
        self.index = {}
        self.file_titles = {}
        create_index(filenames, self.index, self.file_titles)

    def handle_request(self, request):
        """
        Handles requests from the browser.

        /                  -> returns the HTML search page
        /search?query=...  -> returns JSON search results
        """
        print(request)

        if request.command == '':
            return self.html

        if request.command == 'search':
            query = request.params.get('query', '').strip().lower()
            filenames = search(self.index, query)

            response = []
            for filename in filenames[:MAX_RESPONSES_PER_REQUEST]:
                response.append({
                    'title': self.file_titles[filename]
                })

            return json.dumps(response)

        return json.dumps([])


def main():
    handler = SearchServer()
    SimpleServer.run_server(handler, 8000)


if __name__ == '__main__':
    main()
