# Facebook Image Downloader

##### *For Python 3.6.*

## What is it?
A Python script which takes a Facebook Page and downloads all images from a particular album of the page. It uses [Facebook Graph API](https://developers.facebook.com/docs/graph-api) to call upon the page, locate the desired album (if it exists), and download all of the images in the album.

## How do I use it?
In `main.py`:
- Change `PAGE` to the name of the Facebook page you want. Page names can be found within the URL when on the page, for example: *facebook.com/__PAGE NAME__/*
- Change `ALBUM` to the page's album you want to download from.
- Change `IMG_DIR` to the local directory you want to download images to.
- Change Facebook credentials to those found in your [Facebook App](https://developers.facebook.com/).

Run `main.py` and wait for download to be complete.

Images are named like so: `[NUM_LIKES]_[IMAGE_ID].jpg`

## Example
File `old_friends.zip` shows 40 images from [Old Friends Senior Dog Sanctuary](https://www.facebook.com/pg/OldFriendsSeniorDogSanctuary/) which have 10000 likes or more (as of 13 May 2017).
