# gspread-example
A very basic example of how to use [gspread]([url](https://docs.gspread.org/en/v5.10.0/)https://docs.gspread.org/en/v5.10.0/) data to populate a jinja template.

### Step 1: Google Setup ###
- Follow the instructions for [creating a bot service account](https://docs.gspread.org/en/v5.10.0/oauth2.html#for-bots-using-service-account)
  - Note: This method sets up an account for a "bot" as opposed to the [OAuth ID method](https://docs.gspread.org/en/v5.10.0/oauth2.html#oauth-client-id), which sets up the ability for your code to run as an existing google user (that user must authorize it first).
- Copy the example spreadsheet linked above and share it with your bot's email address

### Step 2: Code Setup ###
- Clone this repo onto your laptop, create a python3 venv with `jinja2` and `gspread`, and run the code. Below are steps to do this on a linux or mac from the CLI:
```

```
