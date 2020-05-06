#!/usr/bin/env python3

import click

import waipy
import gentools as gen

@click.group()
@click.option('--limit', type = click.INT, default = 10, help = "投稿の最大数を定義する")
@click.option('--minscore', type = click.INT, default = 10, help = "リンクカルマの最小値を定義する")
@click.option('--path', type = click.Path(exists=True), help = "ダウンロード済み画像集の対象ディレクトリのパス")
@click.option('--botcount', type = click.INT, default = 1, help = "使いたいボット数を定義する")
@click.option('--config', type = click.Path(exists = True), default = 'credentials.json', help = "設定ファイルのパス")
@click.pass_context
def cli(ctx, limit, minscore, path, botcount, config):
    ctx.ensure_object(dict)
    ctx.obj['LIMIT'] = limit
    ctx.obj['MINSCORE'] = minscore
    ctx.obj['PATH'] = path
    ctx.obj['BOTCOUNT'] = botcount
    ctx.obj['CONFIG'] = config

@cli.command()
@click.argument('subreddit')
@click.pass_context
def scrap(ctx, subreddit):
    limit = ctx.obj['LIMIT']
    min_score = ctx.obj['MINSCORE']
    path = ctx.obj['PATH']

    # Sets default target directory - remove these lines after debugging!
    if not path:
        path = gen.make_onedrive_directory(f"画像/アニメ/{subreddit}")
    
    bot = waipy.Bot(filename = ctx.obj['CONFIG'], count = ctx.obj['BOTCOUNT'])
    
    bot.scrap(
        subreddit = subreddit,
        target_directory = path,
        limit = limit,
        min_score = min_score
    )

    click.secho(f"約{limit}枚の画像が{path}に保存されました。", fg = 'yellow')

if __name__ == '__main__':
    try:
        cli(obj = {})
    except KeyboardInterrupt:
        pass