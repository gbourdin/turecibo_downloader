# -*- coding: utf-8 -*-

"""Console script for turecibo_downloader."""
import sys
import click

from .turecibo_downloader import DocumentDownloader

@click.argument('hash')
@click.option(
    '--output', '-o',
    help='Where should the resulting pdf be saved to (default=output.pdf)'
)
@click.option(
    '--pages', '-p',
    help='How many pages does the original document have'
)
@click.command()
def main(hash, pages=1, output='output.pdf'):
    """
    Download and save the document identified by HASH. See details on how to get
    hashes from turecibo.com files in the README.md file
    """
    downloader = DocumentDownloader(
        hash=hash, pages=int(pages), filename=output)
    downloader.download()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
