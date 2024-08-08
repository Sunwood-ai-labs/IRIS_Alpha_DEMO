# 🚀 IRIS v7.1.0 リリースノート

## 📋 概要

IRIS v7.1.0 は、ドキュメントの改善とコードの整理に重点を置いたリリースです。このバージョンでは、READMEの構造と内容を大幅に改善し、ユーザーエクスペリエンスを向上させました。また、リリースノートの自動生成機能を削除し、関連するコードを整理することで、プロジェクトの保守性を向上させています。

## ✨ 新機能
- 🎉  **S3 ファイルアップロード:** S3 にファイルをアップロードする機能を追加しました。AWS 認証情報、バケット名、ファイルパスを指定して、ファイルを S3 にアップロードできます。アップロードが成功すると、S3 上のファイル URL を取得できます。
- 🎉 **GitHub CDN サービス:** GitHub CDN にファイルをアップロードする機能を追加しました。リポジトリ ID、リリース ID、ファイルパスを取得して、GitHub API を使用してファイルをアップロードします。アップロードが成功すると、CDN 上のファイル URL を取得できます。
- 🎉 **S3 バケットの公開設定:** プライベートリポジトリのヘッダー画像を S3 で公開するための設定を追加しました。S3 バケットに公開読み取りポリシーを設定し、パブリックアクセスブロックを無効化することで、S3 バケット内のファイルを公開してアクセスできるようにしました。

## 🛠 改善点
- 🚀  **READMEの構造と内容を大幅に改善** 
- 🚀  **リリースノートの自動生成機能を削除**

## 🐛 バグ修正
- 🐛  **READMEの自動更新処理を一時的に無効化** 

## ⚠️ 重要な変更
- 🔥 **リリースノート自動生成機能削除:** リリースノート自動生成機能は、このバージョンで削除されました。
- 🗑️ **S3 アップロード処理削除:** リリースノート自動生成機能の削除に伴い、S3 へのアップロード処理が削除されました。
- 🗑️ **GitHub CDN アップロード処理削除:** リリースノート自動生成機能の削除に伴い、GitHub CDN へのアップロード処理が削除されました。
- 🗑️ **S3 公開設定処理削除:** リリースノート自動生成機能の削除に伴い、S3 への公開設定処理が削除されました。

## 📦 アップグレード手順

このバージョンへのアップグレード手順は特にありません。

## 👏 謝辞
このリリースへの貢献に感謝します。

- Maki
- iris-s-coon 
- github-actions[bot]

---

# IRIS_Alpha_DEMO

![Project Logo](https://raw.githubusercontent.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/main/docs/release_notes/header_image/release_header_latest.png)

IRIS_Alpha_DEMOは、画像分析、自然言語処理、およびフィボナッチ数列の概念を融合した革新的なPythonプロジェクトです。数学的な美しさと実用的な応用を組み合わせ、ユーザーに独特な体験を提供します。

[![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-7.1.0-green.svg)](https://github.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/releases)

## 🌟 主な機能

- 🖼️ **画像の黄金比分析:** 画像を分析し、黄金比に基づいた構図の評価を行います。
- 🔢 **フィボナッチ数列の計算と探索:** 数列の生成、特定の数の判定、最近接値の検索を行います。
- 🧠 **インタラクティブなフィボナッチクイズ:** 数列に関する知識を楽しく学べます。
- 🌀 **フィボナッチ螺旋の可視化:** 美しい数学的パターンをグラフィカルに表現します。
- 📚 **フィボナッチワードの生成:** 興味深い言語学的パターンを探索します。

## 🚀 はじめ方

### 前提条件

- Python 3.9
- pip (Pythonパッケージマネージャー)

### インストール

1. リポジトリをクローンします：
   ```
   git clone https://github.com/Sunwood-ai-labs/IRIS_Alpha_DEMO.git
   ```

2. プロジェクトディレクトリに移動します：
   ```
   cd IRIS_Alpha_DEMO
   ```

3. 必要なライブラリをインストールします：
   ```
   pip install -r requirements.txt
   ```

### 使用方法

1. メインプログラムを実行します：
   ```
   python fibonacci_game.py
   ```

2. 画面の指示に従って、希望するゲームやツールを選択します。

3. 画像分析機能を使用する場合：
   ```
   python examples/image_golden_ratio_analyzer.py
   ```
   プロンプトに従って画像パスを入力します。

## 📘 ドキュメンテーション

詳細なドキュメンテーションは[Wikiページ](https://github.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/wiki)で確認できます。

## 🛠️ 開発

プロジェクトへの貢献に興味がある方は、[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

## 📅 最新情報

### v7.1.0 (2024年8月12日)
- READMEの構造と内容を大幅に改善
- リリースノートの自動生成機能を削除
- READMEの自動更新処理を一時的に無効化
- その他の細かな修正と改善

全ての更新履歴は[releases](https://github.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/releases)で確認できます。

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 🤝 貢献者

このプロジェクトを可能にしてくれた全ての貢献者に感謝します。