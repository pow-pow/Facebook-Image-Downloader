'''
Created on 13 May 2017

@author: pow-pow
'''

from urllib.request import urlopen, Request
import ssl
import json
import time
import os

class PageAccess:

    def __init__(self, page_name, album_name, img_dir, min_likes, access_token):
        # Page info
        self.page = page_name
        self.album = album_name
        self.min_likes = min_likes

        # Image store
        self.img_dir = img_dir
        if not self.img_dir.endswith("/"):
            self.img_dir += "/"

        # Facebook app info
        self.token = access_token

    def printConfig(self):
        print("PageAccess Configuration")
        print("\t> %s" % self.page)
        print("\t> %s" % self.album)
        print("\t> %s" % self.img_dir)
        print("\t> %s" % self.token)

    def start(self):
        self.printConfig()
        print()
        print("Starting...")

        print("\t> Finding id for album \'%s\'..." % self.album)
        resp = self.getNodeData(self.page, "albums", 0, ["id", "name"], None)

        if resp != -1:
            album_id = self.getAlbum(resp)

            if int(album_id) > -1:
                print("\t> Album found! Downloading images... (id: %s)" % str(album_id))
                resp = self.getNodeData(album_id, "photos", 0, ["images"], None)
                count = self.processAlbum(self.page, resp)

                print("\t> Finished! (%s images downloaded)" % str(count))
            else:
                print("\t> ERROR: Album not found!")

        else:
            print("\t> ERROR: No response!")

        print("Done!")


    def getNodeData(self, node, edge, limit, fields, summary):
        """Calls upon Facebook for data and returns a JSON string."""

        b = "https://graph.facebook.com/v2.6/%s/%s" % (node, edge)
        p = "/?access_token=%s" % self.token
        f = ""
        s = ""
        l = ""

        if fields is not None:
            f += "&fields=%s" % ",".join(fields)

        if summary is not None:
            s += "&summary=%s" % ",".join(summary)

        if limit > 0:
            l += "&limit=%s" % limit

        req = self.makeRequest(b + p + f + s + l, True)
        if req != -1:
            return json.loads(req)
        return req


    def makeRequest(self, url, ignoreFailure):
        """Takes Facebook URL and requests data."""

        success = False

        while success is False:
            try:
                resp = urlopen(Request(url), context=ssl._create_unverified_context())
                success = resp.getcode() == 200
            except Exception as e:
                print("ERROR (url: %s)" % url)
                print("\t> %s" % e)

                if ignoreFailure:
                    return -1
                else:
                    print("\t> Retrying...")
                    time.sleep(3)

        return resp.read()


    def getAlbum(self, resp):
        """Looks through the page's albums and returns the id of the album, if available."""

        for album in resp['data']:
            if album['name'] == self.album:
                return album['id']
        return -1 # no album with chosen name


    def processAlbum(self, page, resp):
        """Walks through album and extracts all of its images."""

        hasNextPage = True
        count = 0

        if not os.path.isdir(self.img_dir):
            os.mkdir(self.img_dir)

        while hasNextPage:
            for image in resp['data']:
                if len(image['images']) > 0:

                    resp_likes = self.getNodeData(image["id"], "likes", 0, None, ["total_count"])
                    if resp_likes != -1:
                        likes = resp_likes["summary"]["total_count"]
                        file_name = str(self.img_dir + str(likes) + "_" + image["id"] + ".jpg")
                        if likes >= self.min_likes and self.processImage(image['images'][0]['source'], file_name) != -1:
                            count += 1
                            if count % 50 == 0:
                                print("\t\t> %s downloaded..." % str(count))

            hasNextPage = 'paging' in resp.keys() and 'next' in resp['paging'].keys()
            if hasNextPage:
                resp = json.loads(self.makeRequest(resp['paging']['next'], False))

        return count


    def processImage(self, url, file_name):
        """Downloads image at URL and stores to save_dir as <url hash>.jpg"""

        f = open(file_name, "ab")

        try:
            resp = urlopen(Request(url), context=ssl._create_unverified_context())
            f.write(resp.read())
        except Exception as e:
            print(e)
            return -1
