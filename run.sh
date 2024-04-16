#!/bin/bash
# -*- coding: utf-8 -*-

if [ ! -f "./sheet.url" ]
then
  echo "---------------------------------------------------------------------"
  echo "[ERROR] the url to the word list is need to specified in 'sheet.url'."
  echo "---------------------------------------------------------------------"
  exit 1
fi

if [ ! -f "./hook.url" ]
then
  echo "-------------------------------------------------------------------"
  echo "[ERROR] the url of discord hook is need to specified in 'hook.url'."
  echo "-------------------------------------------------------------------"
  exit 1
fi

# Set credential information to the shell.
export WORDLIST_SHEET_URL=$(cat sheet.url)
export DISCORD_HOOK_URL=$(cat hook.url)

# Execute the main program as python module
python3 -m wordlist