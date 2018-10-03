# -*- coding: utf-8 -*-
import io
import requests
import tqdm
from PIL import Image

BASE_URL = 'https://api.nosconecta.com.ar/'
PATH = 'eform/thumbnail/{}'
BASE_PARAMS = {
    'resize': 'full',
    'page': '0',
}


class DocumentDownloader:
    def __init__(self, hash, pages=1, filename='./output.pdf'):
        self.hash = hash
        self.pages = pages + 1  # In case your count is off
        self.filename = filename
        self.url = BASE_URL + PATH.format(self.hash)

    def download(self):
        pages = self.get_pages()
        self.save_as_pdf(pages)

    def get_pages(self):
        """
        Downloads all the pages and returns them as an ordered list of images
        loaded in memory
        """
        session = requests.session()
        params = BASE_PARAMS.copy()
        pages = []
        for page in tqdm.trange(self.pages):
            params.update({'page': '{}'.format(page)})
            req = session.get(self.url, params=params)
            if req.headers.get('Content-Type').startswith('application/json'):
                # This is probably an error message, we are most likely
                # out of bounds. Continue trying to get pages though
                continue
            img = Image.open(io.BytesIO(req.content))
            pages.append(img)

        return pages

    def save_as_pdf(self, pages):
        first_page, pages = pages[0], pages[1:]
        first_page.save(
            self.filename, "PDF", resolution=100.0,
            save_all=True, append_images=pages
        )
