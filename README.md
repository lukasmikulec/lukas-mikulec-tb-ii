# Activities ReadMe

## What are *Activities*?
Activities app is trying to solve the problem of bubble creation among immigrants in Germany. The mechanism of the app is to connect people based on activities they like to do or would like to try. The connection always happens between German(s) and non-German(s) which should help with the integration process in Germany and spark genuine connections across cultural divides.

## How can I use the app?
The app is currently built as a MVP demo for a coding assignment. Its architecture stores the user and activity data locally in a csv file, meaning that the app cannot be currently by multiple users which would connect to a central server. However, you are welcome to clone my repository and run the app yourself locally by running the [app.py file]([https://docs.python.org/3/library/tkinter.html](https://github.com/lukasmikulec/lukas-mikulec-tb-ii/blob/main/app.py)) in a Python interpreter. The app was designed on Windows, so some parts might not work as intented on other operating systems.

## What are technical details of the app?
The app was built using the [tkinter library](https://docs.python.org/3/library/tkinter.html). Most of the widgets, however, use a modified version of tkinter called [CustomTkinter](https://customtkinter.tomschimansky.com/), which is a library that modernizes the look of tkinter. I also used the [TkinterMapView](https://github.com/TomSchimansky/TkinterMapView) to run the map widget. Other libraries used include [pandas](https://pandas.pydata.org/) (for handing CSV files), [geocoder](https://geocoder.readthedocs.io/) (for receiving user's location from the IP address), [datetime](https://docs.python.org/3/library/datetime.html) (for generating unique activity identifiers), [PIL](https://python-pillow.org/) (for handling images), and [webbrowser](https://docs.python.org/3/library/webbrowser.html) (for opening URLs outside of the app).

## Where are the icons from?
The icons used in the app are Google's Material design icons. I downloaded them from [Pictogrammers](https://pictogrammers.com/library/mdi/).

## Which font does the app use?
The app uses [Roboto font family](https://fonts.google.com/?query=roboto).

## Attributions for the images used:
* Dance image: Image by <a href="https://www.freepik.com/free-vector/hand-drawn-flat-people-dancing_16693469.htm#query=dance&position=1&from_view=search&track=sph&uuid=e1719f41-47bd-48df-aa02-ef8c1c2ccaf6">Freepik</a>
* Guitar image: <a href="https://www.freepik.com/free-vector/artists-play-live-music-urban-skate-park-area_21058329.htm#query=guitar%20playing&position=6&from_view=search&track=ais&uuid=57ea4952-7d14-4228-8805-370fe1fefb5c">Image by upklyak</a> on Freepik
* Cinema image: <a href="https://www.freepik.com/free-vector/back-view-people-movie-theater-flat-flyer-template_12076515.htm#page=2&query=cinema&position=6&from_view=search&track=sph&uuid=a4092a52-1c10-49c2-bded-9f3f382cac7f">Image by pch.vector</a> on Freepik
* Cooking image: <a href="https://www.freepik.com/free-vector/collection-people-cooking-their-favourite-food_8247920.htm#page=2&query=cooking&position=28&from_view=search&track=sph&uuid=befce5c8-6987-4976-94bc-efc47029ab66">Image by pikisuperstar</a> on Freepik
* Creative writing: <a href="https://www.freepik.com/free-vector/tiny-creative-people-writing-poems-typewriter-persons-reading-antique-books-feather-ink-bottle-flat-vector-illustration-literature-poetry-concept-banner-website-design-landing-page_24644938.htm#query=writing%20workshop&position=2&from_view=search&track=ais&uuid=594c2f5a-0fff-4446-98b5-1528339bc8d4">Image by pch.vector</a> on Freepik
* Doing school work: <a href="https://www.freepik.com/free-vector/business-people-looking-book_5949657.htm#query=homework&position=13&from_view=search&track=sph&uuid=2f4d251a-068f-4cbe-b92a-0d9d3223c5a0">Image by pikisuperstar</a> on Freepik
