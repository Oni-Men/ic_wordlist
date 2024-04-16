# -*- coding: utf-8 -*-

__author__ = "Onimen"
__date__ = "2024/04/16"
__version__ = "0.0.1"

import os

class Word:

  def __init__(self, row) -> None:
    row = row.split(os.linesep)[0]
    tokens = row.split(",")

    # 用語（同義語が存在するため複数あり）
    # Term (It is possible to exist several synonyms)
    self.words = tokens[0].split("|")

    # コード。学習指導要領の領域を示す。複数指定可能
    # Code (Indicate the area of the Course of Study. It is able to specify multiple)
    self.codes = tokens[1].split(";")

    # カテゴリ
    # Category
    self.category = tokens[2]

    # 説明
    # Description
    self.description = tokens[3]

    # 総意率。詳しい定義は（https://docs.google.com/spreadsheets/d/1FYsq1-ZmwrovR1j8_Q_M5QmSlj6NIZdy/view#gid=1163502466）を参照
    # Rate of consensus. See the link above for more information.
    self.consensus_rate3 = self._try_parse_float(tokens[4], 0)
    self.consensus_rate2 = self._try_parse_float(tokens[5], 0)
    self.consensus_rate1 = self._try_parse_float(tokens[6], 0)

  def _try_parse_float(self, x, or_else):
    """
    引数xをfloatとしてパース可能な場合、xが表す浮動小数点数を返す。そうでない場合、or_elseを返す。
    Return floating-point number which 'x' indicates when sucessfully parsed. Otherwise, returns 'or_else'
    """
    try:
      return float(x)
    except ValueError:
      return or_else

  def has_description(self):
    return not (self.description == None or self.description == "")

  def __str__(self) -> str:
    subject = f"{self.words[0]}"
    aliases = f"  同義語: {str.join(', ', self.words[1:])}"
    category = f"  カテゴリ: {self.category}"
    codes = f"  コード: {str.join(', ', self.codes)}"
    description = f"  説明: {self.description}"

    lines = [subject, aliases, category, codes, description]
    return str.join("\n", lines)