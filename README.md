# About GreenTCG
Discord bot for playing GTCG The Game™! Green The Card Game TCG™ (aka GTCGTGTM) was a card game designed to be played during Flaircon, a week-long event on the Flairwars Discord server. Since Flaircon is over, the code is no longer being maintained. The game itself was played on [an external website](https://playingcards.io/); the purpose of the Discord bot was to manage game lobbies and was used as a platform for players to challenge each other to matches. If you're particularly interested, you can find an explaination on how to play GTCGTGTM [here](https://docs.google.com/document/d/1VA46zOvycqDlAxfHvJB5HL4CS6YWK3wvz22_MY9EzI8/edit?usp=sharing).

# Installing Python packages

Before you start installing packages, it's a really good idea to create a virtual environment first. This is especially true since this project is using a newer version of discord.py, and so chances are if you want to use discord.py for any other project you'll probably be using a different version. 

Having a virtual environment lets you use different versions of different packages install for different projects, and will make installing all the required packages much easier. We're going to make a virtual environment called `.venv`, since this name is already in the `.gitignore` file (if you know what you're doing you can name your venv something else, but be sure to ignore it in your git!):

```shell
GreenTCG> python -m venv .venv
```

Now we need to *activate* the virtual enviroment. What this basically does is tells python not to use the packages you've installed on your machine, but to use the packages you've installed locally inside your virtual environment. How you do this depends on what OS and shell you're running:

**Windows**
```shell
GreenTCG> .venv\Scripts\activate
```
**Unix, bash shell**
```shell
GreenTCG$ . .venv/bin/activate
```
**Unix, csh shell**
```shell
GreenTCG$ .venv/bin/activate.csh
```
**Unix, fish shell**
```shell
GreenTCG$ .venv/bin/activate.fish
```

Next we need to install all of the required packages in our virtual environment. You could do this manually, but luckily python has a way to do this automatically for us after we give it a list of required modules:

```shell
GreenTCG> pip install -r requirements.txt
```

This should install all the modules needed. If you add another required module to the project, be sure to update `requirements.txt`!

Keep in mind that any time you want to run the code you'll need to reactivate the venv again.

# Setting up the environment

Here's an example `.env` file, fill in all the correct values and you should be good to go.

```
PREFIX=$
DISCORD_TOKEN={discord token of your bot}
DISCORD_DEV_ID={discord id of developer (used for reloading bot modules via command)}
DEBUG=False
```
