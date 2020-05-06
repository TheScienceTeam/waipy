# このプロジェクトについて
Waipy（ワイパイー）は、ユーザー定義Subredditから画像を簡単にダウンロードすることができるプロジェクトです。

## 設定ファイルの内容
手始めにプロジェクトのルート・ディレクトリでcredentials.jsonという設定ファイルを作成して、必要なデータを入力してください。

```json
{
  "count" : "REDACTED",
  "bots" : [
    {
      "agent_id" : "REDACTED",
      "display_name" : "REDACTED",
      "username" : "REDACTED",
      "password" : "REDACTED",
      "email" : "REDACTED",
      "client_id" : "REDACTED",
      "user_agent" : "REDACTED",
      "redirect_uri" : "REDACTED",
      "client_secret" : "REDACTED",
      "status" : "REDACTED",
      "verified" : "REDACTED"
    },
    {
      "agent_id" : "...",
    }
  ]
}
```

##　使い方

```bash
# ヘルプメッセージを出力します
python src/cli.py --help
# 例えばこんな感じで使ってみてよ
python src/cli.py --minscore 50 --limit 1000 scrap animewallpaper
```
