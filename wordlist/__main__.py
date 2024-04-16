#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Onimen"
__date__ = "2024/04/16"
__version__ = "0.0.1"

import random
import os
import sys

from .hook import Hook
from .word import Word
from .scraper import WordListScraper

WORDLIST_SHEET_URL = "WORDLIST_SHEET_URL"
DISCORD_HOOK_URL = "DISCORD_HOOK_URL"

CATEGORIES = ["情報セキュリティ", "認証", "マルウェア", "不正アクセス", "規格や規格制定組織", 
              "電子商取引", "人工知能", "Web", "データ量", "テキストデータ", "画像", "ラスター画像",
              "ベクター画像", "色", "RGB", "CMY", "圧縮", "誤り検出", "ディジタル化", "音のディジタル化",
              "動画", "数値の扱い", "コンピュータ", "ハードウェア", "CPU構成要素", "ビットと符号化",
              "2の補数", "数値と誤差", "論理回路", "論理ゲート", "周辺装置", "ソフトウェア", "ファイル",
              "プログラミング言語", "プログラミングプロセス", "プログラミング図法", "プログラミング環境",
              "ソフト開発", "変数", "演算", "論理演算", "制御構造", "配列", "関数", "レコード", "アルゴリズム",
              "探索", "ソート", "統計", "シミュレーション", "モデル化", "ネットワーク", "インターネット",
              "クライアント・サーバシステム", "トランスポート層", "DNS", "ネットワーク層", "データリンク層",
              "有線LAN", "無線LAN", "デジタル通信", "暗号", "公開鍵暗号", "アクセス制御と認証", 
              "誤りと改ざんの検出", "Webと暗号化", "データベース", "リレーショナルデータベース",
              "統計処理", "相関関係"]

EXIT_OK = 0

def pickup_random_word(wordlist: list[Word], categories = None):
  """
  Returns random word from given word list.
  Pick up the word from categories if the categories were specified.
  """
  wordlist = [*wordlist]

  if categories != None:
    for word in wordlist:
      if word.category not in categories:
        wordlist.remove(word)

  size = len(wordlist)
  index = random.randint(0, size)

  return wordlist[index]

def for_discord_content(word):
  lines = [
    f"## {word.words[0]}",
    f"{word.description}"
  ]
  return str.join("\n", lines)

def for_discord_embed(word):
  embed = {
    "title": f"Googleで「{word.words[0]}」を検索する",
    "description": f"Google検索が開きます。",
    "url": f"https://www.google.com/search?q={word.words[0]}とは",
    "fields": [
      {
        "name": "類義語",
        "value": str.join(", ", word.words[1:]),
        "inline": True
      },
      {
        "name": "カテゴリ",
        "value": word.category,
        "inline": True
      }
    ]
  }
  return embed

def main():
  
  wordlist_sheet_url = os.getenv(WORDLIST_SHEET_URL)
  discord_hook_url = os.getenv(DISCORD_HOOK_URL)

  wordlist = WordListScraper(wordlist_sheet_url).execute()
  word = pickup_random_word(wordlist, categories=CATEGORIES)

  hook = Hook(discord_hook_url)
  hook.set_username("Daily Tips")
  hook.set_content(for_discord_content(word))
  hook.add_embed(for_discord_embed(word))
  hook.send()

  return EXIT_OK


if __name__ == "__main__":
  sys.exit(main())