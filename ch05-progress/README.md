# 第5章 サポートページ — Chainlit リサーチツールの段階的構築

本リポジトリは、書籍第5章のサンプルコードです。Chainlit の Step 機能を中心に、リサーチツールを段階的に拡張していく過程を体験できます。

## セットアップ

### 前提条件

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- OpenAI API キー

### インストール

```bash
uv sync
```

### 環境変数の設定

`.env.example` をコピーして `.env` を作成し、OpenAI API キーを設定してください。

```bash
cp .env.example .env
```

```
OPENAI_API_KEY=your_openai_api_key_here
```

> **注意**: `.env` は Git にコミットしないでください。

## サンプルアプリ一覧

| TARGET | 概要 |
|--------|------|
| `ch5_0` | Step 表示なし版 — ストリーミング回答のみのベースライン |
| `ch5_4` | Step 表示あり版 — ルート・トピック・サイトの階層的な Step を導入 |
| `ch5_5` | Step 出力のリッチ化 — トピック Step にテーブル形式の出力と信頼度表示を追加 |
| `ch5_6` | TaskList の導入 — 調査の進捗をタスクリストで可視化 |
| `ch5_7` | Plotly チャート — 信頼度ヒートマップをインラインで表示 |
| `ch5_8` | 並行処理と豆知識 — トピック生成と豆知識生成を `asyncio.gather` で並行実行 |

## 実行方法

`TARGET` 環境変数でアプリを切り替えます。

```bash
# 例: ch5_0 を実行
make run TARGET=ch5_0

# 例: ch5_4 を実行
make run TARGET=ch5_4

# TARGET を省略すると ch5_4 がデフォルトで起動します
make run
```

起動後、ブラウザで http://localhost:8000 にアクセスしてください。
