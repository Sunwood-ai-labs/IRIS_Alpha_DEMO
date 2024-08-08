# 🚀 IRIS v8.1.0 リリースノート

## 📋 概要

IRIS v8.1.0 は、画像分析とカラーパレット抽出機能の強化に焦点を当てたリリースです。このバージョンでは、リリースノートのヘッダー画像から自動的にカラーパレットを抽出する機能を追加し、リリースノートのデザインをさらに魅力的にしました。また、ヘッダー画像生成スクリプトを改善し、スムーズな領域の検出とテキスト配置の最適化を導入することで、より洗練された画像生成を可能にしました。

## ✨ 新機能

- 🎉 ヘッダー画像からカラーパレットを自動的に抽出する機能を追加しました。 (commit: 05345ca)
- 🎉 ヘッダー画像生成スクリプトを改善し、スムーズな領域の検出とテキスト配置の最適化を導入しました。 (commit: b0a12be)

## 🛠 改善点

- 🚀 画像処理とカラー分析機能を強化し、自動的に最適なテキスト配置と色を選択するように `generate_header_image` メソッドを改良しました。 (commit: 5d0e1d6)
- 🚀 色空間の可視化機能を追加しました。 (commit: 5d0e1d6)
- 🚀 画像処理の柔軟性を向上させるために、 `use_smooth_area` と `target_ratio` パラメータを `generate_header_image` メソッドに追加しました。 (commit: b0a12be)

## 🐛 バグ修正

- 🐛 なし

## ⚠️ 重要な変更

- ⚠️ なし

## 📦 アップグレード手順

- アップグレード手順はありません。

## 👏 謝辞

このリリースへの貢献に感謝します。

- iris-s-coon 
- Maki

---

# 🚀 IRIS_Alpha_DEMO

![Project Logo](https://raw.githubusercontent.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/main/docs/release_notes/header_image/release_header_latest.png)

IRIS_Alpha_DEMOは、画像分析、自然言語処理、およびフィボナッチ数列の概念を融合した革新的なPythonプロジェクトです。数学的な美しさと実用的な応用を組み合わせ、ユーザーに独特な体験を提供します。

[![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-8.1.0-green.svg)](https://github.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/releases)

## 🌟 主な機能

- 🖼️ **画像の黄金比分析:** 画像を分析し、黄金比に基づいた構図の評価を行います。
- 🔢 **フィボナッチ数列の計算と探索:** 数列の生成、特定の数の判定、最近接値の検索を行います。
- 🧠 **インタラクティブなフィボナッチクイズ:** 数列に関する知識を楽しく学べます。
- 🌀 **フィボナッチ螺旋の可視化:** 美しい数学的パターンをグラフィカルに表現します。
- 📚 **フィボナッチワードの生成:** 興味深い言語学的パターンを探索します。

## 🚀 はじめ方

### 📦 前提条件

- Python 3.9
- pip (Pythonパッケージマネージャー)

### 📦 インストール

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

## 🔧 使用方法

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

## 🆕 最新情報

全ての更新履歴は[releases](https://github.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/releases)で確認できます。

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 🤝 貢献者

このプロジェクトを可能にしてくれた全ての貢献者に感謝します。
```
```
```