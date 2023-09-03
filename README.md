# sthe_bot
STH's Personal Discord Bot. (It')S THE bot...

Getting Started:
-
You will need:
* Git (https://git-scm.com/downloads)
* Python (https://www.python.org/downloads/)
* IDE (i.e. VSCode, which has Git integration)
* Discord developer account

Before moving on to the next steps ensure that you have the latest version of Python, Git + IDE of your choice, and/or VSCode installed. If you plan to use Git, you can also use VSCode as an IDE, but VSCode also has built-in Git integration, so Git will not be neccessary. Use what you are most comfortable with. I recommend at least using VSCode as your IDE since there is a built-in terminal that can be used to run the Python scripts. 

Setting up VSCode for Python Development:
-
If you plan to use VSCode for Python development, follow this guide here: https://code.visualstudio.com/docs/python/python-tutorial

Otherwise, do what is necessary for your IDE of choice. 

Setting up a Git Environment:
-
If you plan to use Git, make sure you download and install Git from the link above. In file explorer navigate to the folder you want to checkout the code in. Right-click anywhere in the directory and select "Git Bash Here". Enter the following command:
```
git clone https://github.com/edang1012/sthe_bot.git
```
Once the repo is cloned, either go to the repo directory using the "cd" command or close the git window, navigate to the repo directory and "Git Bash Here". now that Git is in the code directory, make a branch to work in using the following command:
```
git checkout -b [branch_name]
```
If you are using VSCode and it's Git integration, use the following guide: https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette

Creating a Discord Application:
-
To get Discord bot credentials, go to https://discord.com/developers/applications

From here, log in and create a new application. In the application, you will be greeted with a "General Information" page. Here, you can name your bot and also give it a profile picture. Under the "Application ID" section of the page, copy the ID. This will be used later in configuring your bot. 

Now, move to the "Bot" page using the menu on the left hand side. Here, you will find a "Build-A-Bot" section. You can give the bot an icon and also a username. Under the username, there is a "Token" section. Copy this token as it will also be used in the configuration of the bot. At the bottom of the page, there will be a "Bot Permissions" section. Here you can check off what permissions you would like to give the bot. The permissions selection will generate an integer. For example, for mine, since I'm just testing, I gave it admin permissions, so the "Permissions Integer" becomes an 8. Save this "Permissions Integer" as it is also used in the bot's configuration. 

Using the left menu, navigate to the "OAuth2" page, then to "URL Generator". In the "Scopes" section, select "Bot". This will open a "Bot Permissions" section. Select the same permissions you did in the previous step. Once this is all done, a URL will be generated at the bottom of the page. Save this URL and use it to invite your new bot to your server. 

Configure Bot Before use:
-
Before the bot can be run, you will need to take the bot_config_template.json file and edit it with your Bot's credentials. Create a copy of the template and name it bot_config.json. Open the file and replace the entries with the information you saved when creating a discord application. The prefix can be set to whatever symbol you would like. This will be used to invoke bot commands. For Token, Permissions, and Application ID input the data you saved earlier from the Discord Developer Portal. These entries must be entered as strings, encapsulated with " ". Under Owners, paste your Discord User ID. You will need to enable developer mode in Discord in order to see this. Right click on your profile to get this User ID. The User ID must be entered as an integer, with no encapsulation. There is an optional Channel ID that is used for the bot to send a status message upon startup. You can select any discord channel the server by pasting its Channel ID here. If don't plan to use this channel feature, leave the entry to the default string value. 

Once the bot_config.json file has been correctly modified, you are ready to run the bot. 

Running the Bot:
-
Before you run the bot, you must first install all dependencies. If you are using VSCode, open the Git repo directory in VSCode and open a new terminal. In the terminal type the following:
```
python -m pip install -r requirements.txt
```
This will install all the required Python packages to run the bot. Once these are installed, you can run the Bot from VSCode by either opening the sthe.py file and clicking "Run Python File" or typing the following in the terminal. Make sure you are in your virtual environment when running the scripts. 
```
python sthe.py
```
If you want to end the script, click in the terminal window and type Ctrl+C. This will close the currently running program. 

Pushing Changes to the Repo:
-
When you make changes to your local repo, you can check what changes have been made using:
```
git status
```
Add/remove files using
```
git add [file_path]
git rm [file_path]
```
Once you are satisfied with the changes and want to commit your changes, use the following. You should always be commiting with a comment to keep track of what changes were made. 
```
git commit -m "[commit_message_here]"
```
After you commit, you will want to push the changes to the remote repo. Use the following. If you run into an issue where you aren't pointed to the remote repo, follow the prompt in Git. It should be some command with a --set-upstream argument or something like that. 
```
git push
```
Occasionally, you will want to get the latest changes from the main branch use these commands:
```
git checkout main
git pull
git checkout [your_branch]
git merge master
```
When you are satisfied with the changes in your branch and have pushed everything to the remote repo, submit a pull request to merge your changes to master. Others will need to review the changes then approve them. Once approved, the changes can be merged to master.

Useful Links:
-
* Discord.py API documentation: https://discordpy.readthedocs.io/en/stable/index.html
* Old STH Red-bot code: https://github.com/edang1012/STH-red-cogs
* Good Template for discord bot coding: https://github.com/kkrypt0nn/Python-Discord-Bot-Template/tree/main#readme
* Git Plugin for Commit Graph Visualizer: https://github.com/NirmalScaria/le-git-graph/blob/main/README.md
