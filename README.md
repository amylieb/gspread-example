# gspread-example
A very basic example of how to use [gspread]([url](https://docs.gspread.org/en/v5.10.0/)https://docs.gspread.org/en/v5.10.0/) to pull data from a google sheet and populate a jinja template.

This code uses google bot credentials stored in `~/.config/gspread/service_account.json` to open a google sheet called [New Switches](https://docs.google.com/spreadsheets/d/1W9wAzB7t3ttj2Dl_M5KnImShfwOS8hLvcyE-QwvGf1w/edit#gid=0). For each tab it generates access port configuration for an IOS device based on a [jinja template](https://github.com/amylieb/gspread-example/blob/main/template.j2) and saves it as a file based on the name of the tab.

### Step 1: Google Setup ###
- Copy the [example spreadsheet](https://docs.google.com/spreadsheets/d/1W9wAzB7t3ttj2Dl_M5KnImShfwOS8hLvcyE-QwvGf1w/edit#gid=0). Make sure to preserve the name of the spreadsheet (or update the python code in this repo so that it points to the new spreadsheet name).
- Follow the instructions for [creating a bot service account](https://docs.gspread.org/en/v5.10.0/oauth2.html#for-bots-using-service-account) and sharing it with the sheet above.
  - Note: This method sets up an account for a "bot" as opposed to the [OAuth ID method](https://docs.gspread.org/en/v5.10.0/oauth2.html#oauth-client-id), which sets up the ability for your code to run as an existing google user (that user must authorize it first).

### Step 2: Code Setup ###
- Clone this repo onto your laptop, create a python3 venv with `jinja2` and `gspread`, and run the code. Below are steps to do this on a linux or mac from the CLI:
```
bash-3.2$ git clone git@github.com:amylieb/gspread-example.git

[ ... output omitted ... ]

bash-3.2$ cd gspread-example/
bash-3.2$ python3 -m venv venv
bash-3.2$ source venv/bin/activate
(venv) bash-3.2$ pip install gspread jinja2

[ ... output omitted ... ]

(venv) bash-3.2$ python create_configlets.py
```
