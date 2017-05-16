# Facebook Image Downloader

##### *For Python 3.6.*

## What is it?
A Python script which takes a Facebook Page and downloads all images from a particular album of the page. It uses [Facebook Graph API](https://developers.facebook.com/docs/graph-api) to call upon the page, locate the desired album (if it exists), and download all of the images in the album.

## How do I use it?
For each row in `batch.csv`, put values in the following order:
- Name of the Facebook page from which to download images. This can be found in the URL when on a page e.g. `facebook.com/[PAGE_NAME]/`.
- Name of page's image album from which to download images.
- Directory to output downloaded images to.
- Minimum number of likes an image must have in order to download it. Putting `0` will download all images.
An example is provided in `batch.csv` as default.

Run program `runme.py`. Output images are named like so: `[NUM_LIKES]_[IMAGE_ID].jpg`.

## Example
File `old_friends.zip` shows 40 images from [Old Friends Senior Dog Sanctuary](https://www.facebook.com/pg/OldFriendsSeniorDogSanctuary/) which have 10000 likes or more.
