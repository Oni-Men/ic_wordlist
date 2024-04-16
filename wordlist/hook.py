# -*- coding: utf-8 -*-

__author__ = "Onimen"
__date__ = "2024/04/16"
__version__ = "0.0.1"

import json
from urllib.request import Request
from urllib import request


class Hook:
  
  def __init__(self, hook_url) -> None:
    self.hook_url = hook_url
    self.content = ""
    self.username = ""
    self.avatar_url = ""
    self.embeds = []

  def set_username(self, username):
    self.username = username
    return self

  def set_avatar_url(self, avatar_url):
    self.avatar_url = avatar_url
    return self

  def set_content(self, content: str):
    self.content = content.replace("\n", "\r")
    return self

  def add_embed(self, embed):
    if len(self.embeds) >= 10:
      raise RuntimeError("The number of embeds must be equal to or less than 10.")
    self.embeds.append(embed)
    return self

  def _create_payload(self):
    payload = {
      "content": self.content,
      "username": self.username,
      "avatar_url": self.avatar_url,
      "embeds": self.embeds
    }
    return json.dumps(payload).encode()

  def send(self):
    """
    DiscordのWebHookを叩く
    """
    headers = {
      "Content-Type": "application/json",
      "User-Agent": "",
    }
    req = Request(self.hook_url, self._create_payload(), headers, method="POST")
    request.urlopen(req)