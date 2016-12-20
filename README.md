# autoBlogger
Python Auto-Image Download + Social Media Uploader
Goals:
* Work on webscraping tactics and establish a social media presence
* Demonstrate my knowledge of social media sites

For a more in-depth explanation why I made this, go to documentation.md.
There is an issue where the top pictures on a Subreddit could be a link to a website hosting an image, if that is the case then the uploader will fail as the image will not download correctly. Working on a fix.

<h1> Features </h1>
<hr>
* Customizable SubReddit page image downloader
* Uploads to tumblr account (Must customize password / username) 
* Also generates a new folder for your files & can delete last lines to keep said pictures (will be overwritten running the program again)

<h1> Need to run </h1>
<hr> 
1. Selenium
2. Chromedriver
3. lmxl 
4. Tumblr Account

<h1> Tasklist </h1>
<hr>
- [X] Establish a way to grab images
- [X] Set up a blogspot/tumblr account
- [X] Find a reliable way to login to this pages (Maybe Twill/Mechanize)
- [X] Upload said images to the account to be posted
