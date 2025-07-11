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
cd app
uv add -r requirements.txt

# VOICEVOXの起動
# VOICEVOXアプリケーションを起動するか、以下のコマンドでサーバーを起動
voicevox_engine --host 0.0.0.0 --port 50021
```

### 3. クライアントのセットアップ
```bash
# クライアント用依存関係のインストール
cd client
uv add -r requirements.txt
```

## 使用方法

### サーバー起動
```bash
# プロジェクトルートディレクトリで実行
python run_server.py
```

### クライアント起動
```bash
# プロジェクトルートディレクトリで実行
python run_client.py

# 別のサーバーに接続する場合
python run_client.py http://192.168.1.100:8000
```

### 単体実行版
```bash
# サーバーとクライアントを同一PCで実行
python main_standalone.py
```

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

## 開発原則
- **YAGNI**: 必要な機能のみ実装
- **KISS**: シンプルで分かりやすい設計
- **DRY**: コードの重複を避ける
- **責務分離**: 各層の責務を明確に分離

## トラブルシューティング

### よくある問題
1. **OpenAI API エラー**: APIキーが正しく設定されているか確認
2. **VOICEVOX 接続エラー**: VOICEVOXが起動しているか確認
3. **音声デバイス エラー**: マイク・スピーカーの接続を確認
4. **ネットワーク エラー**: サーバーとクライアントの接続を確認

### ログ確認
サーバーとクライアントのログを確認して問題を特定してください。