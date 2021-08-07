from lxml import html, etree
from lxml import *
import types
from threading import Thread
import requests
import urllib3
from custom_modules.DialogMessenger import DIALOG_MESSENGER_SWITCH as dms
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.ResourceDownloader import download_file, get_headers, download_media_file, download_media_meta, download_media_playlist, show_headers, get_raw_resource

# "http://www.howtowebscrape.com/examples/simplescrape1.html"
# http: // www.howtowebscrape.com/examples/simplescrape1.html
# https://www.youtube.com/results?search_query=wingsuits
# https://youtu.be/-DCkuvC28mE
# https://jsonplaceholder.typicode.com/todos
# https://jsonplaceholder.typicode.com/posts
# https://jsonplaceholder.typicode.com/comments
# https://jsonplaceholder.typicode.com/photos
# https://jsonplaceholder.typicode.com/albums

line = "-------------------------------------------------------------------------------------------------------------------"


def traverse(array, start=1):
    if type(array) == list:
        for i, a in enumerate(array, start=start):
            print("{}.\t{}".format(i, a))


def traverse_extra(array, start=1):
    if type(array) == list:
        for i, a in enumerate(array, start=start):
            print("{}.\t{}\nProps:\t{}\n{}\n".format(i, a, a.text_content(),
                                                     line))


def kind(arg):
    print("{}".format(type(arg)))


class Scraper:
    def __init__(this):
        this.url = None

    def set_url(this, url):
        this.url = url

    def get_url(this):
        return this.url

    def get_file(this, file):
        download_file(file)

    def download_thread(this, file):
        d_thread = Thread(target=this.get_file, args=(file, ))
        d_thread.start()
        d_thread = None

    def get_playlist(this, playlist_url):
        download_media_playlist(playlist_url)

    def get_playlist_thread(this, url):
        g_thread = Thread(target=this.get_playlist, args=(url, ))
        g_thread.start()
        g_thread = None

    def get_video(this, url):
        download_media_file(url)

    def get_video_thread(this, url):
        g_thread = Thread(target=this.get_video, args=(url, ))
        g_thread.start()
        g_thread = None

    def scrape_file(this):
        page = None
        extracted_html = None
        body_children = None
        domain = None
        domain_list = None
        element_list = None

        if not this.url:
            function = dms['warning']
            return function('oops!'.upper(), 'Missing URL')
        else:
            # page = requests.get(
            #     "http://www.howtowebscrape.com/examples/simplescrape1.html")

            try:
                page = requests.get(this.url)
                domain_list = this.url.rsplit('/', 1)
                domain = domain_list[0]
                extracted_html = html.fromstring(page.content)
                body_children = extracted_html.body[0].getchildren()
                element_list = extracted_html.xpath("//*")
                line = "----------------------------------------------------------------------------------------------------------------------------------------------------"
                tags = []
                tags_kv = {}
                for i, e in enumerate(element_list):
                    tag = e.tag
                    key = tag
                    value = 'empty'

                    if e.text:
                        if len(e.text.strip()):
                            value = e.text

                    tags.append(tag)
                    tags_kv.update({"{}".format(key): "{}".format(value)})

                return {
                    'status': True,
                    'domain_list': domain_list,
                    'domain': domain,
                    'elements': element_list,
                    'body_elements': body_children,
                    'extracted_html': extracted_html,
                    'element_tags': tags,
                    'element_tags_kv': tags_kv
                }

            except requests.exceptions.MissingSchema as ms:
                # print(ms)

                function = dms['warning']

                console_warning = cms['warning']

                print(console_warning("{}".format(ms)))

                return {'error': ms, 'status': False}
            except requests.exceptions.InvalidURL as iu:
                # print(iu)

                function = dms['warning']

                console_warning = cms['warning']

                print(console_warning("{}".format(iu)))

                return {'error': iu, 'status': False}
            except requests.exceptions.InvalidSchema as ins:
                # print(ins)

                function = dms['warning']

                console_warning = cms['warning']

                print(console_warning("{}".format(ins)))

                return {'error': ins, 'status': False}
            except requests.exceptions.ConnectionError as ce:
                print(ce)
                function = dms['warning']
                console_warning = cms['warning']
                print(console_warning("{}".format(ce)))
                return {'error': ce, 'status': False}
            except urllib3.exceptions.NewConnectionError as nce:
                # print(nce)
                function = dms['warning']

                console_warning = cms['warning']

                print(console_warning("{}".format(nce)))

                return {'error': nce, 'status': False}
            except etree.XPathEvalError as xer:
                function = dms['warning']

                console_warning = cms['warning']

                print(console_warning("{}".format(xer)))

                return {'error': xer, 'status': False}
