```
  ____        _              ____
 / ___|  ___ | | __ _ _ __  / ___| _ __   __ _ _ __ ___  _ __ ___   ___ _ __
 \___ \ / _ \| |/ _` | '__| \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
  ___) | (_) | | (_| | |     ___) | |_) | (_| | | | | | | | | | | |  __/ |
 |____/ \___/|_|\__,_|_|    |____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|
                                  |_|
```

# IMPORTANT NOTICE

> WE DO NOT AND WILL NOT TAKE ANY RESPONSIBILITY FOR ANY TROUBLE YOU GET IN TO.
> WHETHER THAT BE WITH A BOSS, FAMILLY MEMBER, TEACHER, OR FRIEND. YOU ARE RESPONSIBLE
> FOR THE HANDLING OF THE SOFTWARE, WE JUST MAKE IT.

## About

Solar Spammer is a fairly simple application that spams, and pretty well at that. Due to it's keyboard automation nature, this program will work on nearly any chatting appliction!

## Trello board
[https://trello.com/b/tWYpLiSa](https://trello.com/b/tWYpLiSa) you can monitor our progress and put pressure on us :)))

## Installing

Just open up `install.py` and you are ready to run `main.py` (Be sure to have the latest version of python installed).

## Usage

When you launch the app, you will see 2 tabs

![](https://i.ibb.co/RCHq7Q5/Screenshot-2021-06-15-205020.jpg)

## From Script

In this tab, you have 3 different parameters you need to specify:

- Time between messages
- Message block size
- Select script file

### Time between messages

This paramater is fairly obsolete, so I just reccomend keeping it at default. But essentially it changes the time it waits between lines. You can turn this down if you like, Unless you run everything on a potato, You should be fine.

### Message block size

This controls how many times the program presses "shift+enter" until it presses enter. This is so that you won't get rate limited when sending messages on something like discord. 5 Is reccomended, however you can fine tune this to your liking.

### Select script file

This controls the file the computer will read from and type. Select your text file and you are good to press start! I have included script.txt into here just as a template script, it's the bee movie script. Use it if you want.

### Other features of this tab

The program will also estimate the minutes remaining in the program, percent remaining, and it will also put that percentage on a progress bar.
Please note that once you press start, you have 5 seconds to focus on the correct window!

## Semi-randomized

![](https://i.ibb.co/mG3d9hg/Screenshot-2021-06-15-214104.jpg)

In this tab, instead of reading from a script, the program will take a specified string input, add on some random characters, and send it a specified amount of times.

In this tab, there are 4 paramaters to change:

- Starting string
- Times to spam
- Time between messages
- Lenth of suffix
- Randomize time

### Starting string

This is the prefix of your spam message. for example,

> Lol get spammed m!L7KtL$iUjXM&Lt&nvB

in this case, "Lol get spammed" is the starting string.

### Times to spam

It's in the name. It just is the amount of times the program will spam the message.

### Time between messages

This one is the same as the last time between messages in terms of functionality, but this one has to be set higher (I reccomend either 0.9 or 1 for discord) in order to prevent rate limiting, just because of the fact that this one doesn't "block" the lines together.

### Length of suffix

This is the length of the randomized characters after the starting string. For example, in the case we used earlier

> Lol get spammed {m!L7KtL$iUjXM&Lt&nvB}

"m!L7KtL$iUjXM&Lt&nvB" would be the suffix. The length of this one happens to be 20.

### Other features of this tab

Nothing much, just the "minutes left" thing.

### Randomize time

This option will enable time randomization. What it does is every time a message is sent, it picks a random length to wait unil the next message (between 0.5s and 2s) Simple, and can sometimes prevent autobans from more advanced discord bots, maybe? You can modify it if you want the gap to be bigger, but i'll just keep this for now.

## FAQ

- Q: What if I want to close the spammer before it is finished typing out the text?

- A: Use our killswitch keybind of shift + esc. Closing the window will not stop the spam.

- Q: Why does the UI look so ugly?

- A: We plan on making it look better in the near future.

## Contributing Info

We are very open to contributions! If you'd like to contribute, feel free to submit a pull request.
