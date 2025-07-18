# OpenAI リアルタイム音声チャットプロジェクト

## 概要
OpenAI APIとVOICEVOXを使用したリアルタイム音声チャットシステムです。
サーバーとクライアントが分離されており、異なるPCで実行可能です。

## ディレクトリ構造
```
voice-assistant/
├── app/                    # サーバーサイド
│   ├── api/               # API層
│   ├── services/          # ビジネスロジック層
│   ├── models/            # データモデル
│   ├── config/            # 設定管理
│   └── requirements.txt   # サーバー依存関係
├── client/                # クライアントサイド
│   ├── core/             # コア機能
│   ├── services/         # サービス層
│   ├── models/           # データモデル
│   ├── utils/            # ユーティリティ
│   └── requirements.txt  # クライアント依存関係
├── run_server.py         # サーバー起動スクリプト
├── run_client.py         # クライアント起動スクリプト
├── main_standalone.py    # 単体実行版
└── .env                  # 環境変数
```

## セットアップ

### 1. 環境変数の設定
```bash
cp .env.example .env
# .envファイルを編集してOpenAI API keyを設定
```

### 2. サーバーのセットアップ
```bash
# サーバー用依存関係のインストール
uv sync

# VOICEVOXアプリケーションを起動
# 下記リンクからダウンロード
https://voicevox.hiroshiba.jp/

# macの認証エラーがでるので下記知恵袋を参考に対処(自己責任ではあるが)
https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11315231866
```

### 3. クライアントのセットアップ
```bash
# プロジェクト全体の依存関係が既にuvでインストールされています
# 追加のセットアップは不要です
```

## 使用方法

### サーバー起動
```bash
# プロジェクトルートディレクトリで実行
uv run python run_server.py
```

### クライアント起動
```bash
# ターミナルを新しく開く
# プロジェクトルートディレクトリで実行
uv run python run_client.py

# 別のサーバーに接続する場合
uv run python run_client.py http://192.168.1.100:8000
```

### 複数PCで使用する場合
デフォルトではサーバーは`0.0.0.0:8000`で全インターフェースで待ち受けており、複数のPCから接続可能です。

1. **サーバー側の設定**
   - サーバーは既に全IPアドレスで待ち受けています（`0.0.0.0`）
   - ファイアウォールで8000番ポートを開放してください
   - サーバーのIPアドレスを確認：
     ```bash
     # macOS/Linux
     ifconfig | grep inet
     # Windows
     ipconfig
     ```

2. **クライアント側の設定**
   - 環境変数で設定: `SERVER_URL=http://サーバーIP:8000`を`.env`に追加
   - または実行時に指定: `uv run python run_client.py http://サーバーIP:8000`

3. **ネットワーク要件**
   - サーバーとクライアントは同一ネットワーク内にある必要があります
   - VPN経由でも接続可能です


## 設定

### 環境変数
- `OPENAI_API_KEY`: OpenAI APIキー（必須）
- `SERVER_HOST`: サーバーのホスト（デフォルト: 0.0.0.0）
- `SERVER_PORT`: サーバーのポート（デフォルト: 8000）
- `SERVER_URL`: クライアントが接続するサーバーURL（デフォルト: http://localhost:8000）

## アーキテクチャ

### サーバー（app/）
- **API層**: FastAPIを使用したREST API
- **サービス層**: AI処理、音声合成の分離
- **モデル層**: データスキーマ定義
- **設定層**: 環境変数管理

### クライアント（client/）
- **コア層**: メインクライアント機能
- **サービス層**: 音声処理、API通信の分離
- **モデル層**: 音声データモデル
- **ユーティリティ層**: 共通処理

