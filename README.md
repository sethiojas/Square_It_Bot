# Square It Bot
![SquareIt Bot](https://raw.githubusercontent.com/sethiojas/readme_images/master/SquareIt_bot/cover.png)

## Table of Contents
* [About](#about)
* [Installation](#installation)
* [ScreenShots](#screenshots)
* [Modules Used](#modules-used)

## About
It is a telegram bot that squares any images the user sends to it.
Bot provides an option of 2 colours (for now) which are Black and White, to be used as the background.

***[USE THE BOT](http://t.me/squareIt_bot)***

## Installation

1. Fork the repository

2. Download the contents via github or clone the repo.
	* For cloning 
	* Copy the link in `Clone or Download` option
	* Open terminal and change into prefered directory
	* `git clone <url>`


3. Install required packages
	`pip insrall -r requirements.txt`

4. Open *bot.py* file

5. On line 8 replace:
	`updater = Updater(token='TOKEN', use_context=True)`
	with
	`updater = Updater(token='<VALID TOKEN HERE>', use_context=True)`

6. You are good to go now!

## ScreenShots
![Bot Info](https://github.com/sethiojas/readme_images/blob/master/SquareIt_bot/bot_info.png)
![Main Screen](https://github.com/sethiojas/readme_images/blob/master/SquareIt_bot/bot_screen.png)
![Start](https://github.com/sethiojas/readme_images/blob/master/SquareIt_bot/start.png)
![Sent image and Options](https://github.com/sethiojas/readme_images/blob/master/SquareIt_bot/colour_option.png)
![Square Image](https://github.com/sethiojas/readme_images/blob/master/SquareIt_bot/square_image.png)

## Modules Used
* Python-telegram-bot
* Pillow
* os
