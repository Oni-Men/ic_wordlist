# 情報科の教科書に含まれる用語からランダムに１つ Discord に投稿するスクリプト

[情報科全教科書用語リスト改240409](https://docs.google.com/spreadsheets/d/1FYsq1-ZmwrovR1j8_Q_M5QmSlj6NIZdy/view#gid=806696916)に含まれる用語をDiscordのチャンネルに投稿します。
この用語集には約6000の用語が含まれていますが、用語の説明があるものは600語ほどです。説明がある約600語のうち特定のカテゴリに属する単語をランダムに1つ選び、それをDiscord WebHookで特定のチャンネルに投稿します。

`run.sh`を実行すると、`python`で書かれた処理が起動する形です。このツールの実行には用語集のURLとWebHookのURLが必要です。このURLはそれぞれファイルに保存しておく必要があります。

| URL | 保存先ファイル |
| --- | --- |
| 用語集 | `sheet.url` |
| Web Hook| `hook.url` |

このスクリプトは実行するたびにランダムな用語を1つ投稿し、終了します。そこで、定期的にチャンネルに投稿するために`cron`を用いて定期実行することを想定しています。以下`cron`の設定に関して説明します。

## cron の設定

まず、このツール(`ic_wordlist`)の配置場所は`/opt/ic_wordlist`であるとします。
さて、`cron`の設定を行っていくので以下のコマンドでエディタを起動してください。

```bash
crontab -e
```

すると、エディタが起動するかと思います。そこに、次のようにして定期実行内容を追記してください。これで毎日12:00にスクリプトが実行されるようになります。

```cron
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
00 12 * * * /opt/ic_wordlist/run.sh >> /var/log/ic_wordlist.log 2>&1
```
