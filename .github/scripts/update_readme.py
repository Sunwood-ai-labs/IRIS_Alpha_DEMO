import os
import sys

# Add the parent directory of 'scripts' to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from github import Github
from loguru import logger
from config import get_settings
from services.llm_service import LLMService

def main():
    logger.info("README更新プロセスを開始します。")
    
    settings = get_settings()
    llm_service = LLMService()
    g = Github(settings.YOUR_PERSONAL_ACCESS_TOKEN_IRIS)
    repo = g.get_repo(settings.GITHUB_REPOSITORY)

    # 最新のリリースを取得
    latest_release = repo.get_latest_release()
    logger.info(f"最新のリリース: {latest_release.title}")

    # READMEの内容を取得
    readme = repo.get_contents("README.md")
    readme_content = readme.decoded_content.decode("utf-8")
    
    repo_summary_path = ".SourceSageAssets/DOCUMIND/Repository_summary.md"
    repo_summary_content = ""

    # リポジトリのサマリーファイルをローカルから読み込む
    try:
        with open(repo_summary_path, 'r', encoding='utf-8') as f:
            repo_summary_content = f.read()
        logger.info("リポジトリのサマリーファイルを読み込みました。")
    except FileNotFoundError:
        logger.warning(f"リポジトリのサマリーファイルが見つかりません: {repo_summary_path}")
    except Exception as e:
        logger.warning(f"リポジトリのサマリーファイルの読み込みに失敗しました: {str(e)}")

    # LLMにプロンプトを送信
    prompt = f"""
以下の情報と更新のガイドラインを元に、READMEを更新してください：

# 更新のガイドライン:

1. 最新の機能や変更点を反映させてください。
2. 既存の構造を維持しつつ、必要な箇所のみを更新してください。
3. リリースノートの詳細すべてをREADMEに含める必要はありません。重要なポイントのみを簡潔に記載してください。
4. リポジトリのサマリーを参考にして、最高のREADMになるように最新の機能や変更点を反映して更新してください。
5. リポジトリの目的、主要機能、使用方法、インストール手順などの重要な情報が欠けている場合は、それらを追加してください。

更新されたREADMEの全文をそのまま出力してください。

---

# 最新のリリースノート:
{latest_release.body}

---

# 現在のREADME:
{readme_content}

---

# リポジトリのサマリー:
{repo_summary_content}

---



    """

    logger.info("LLMに更新を依頼しています...")
    logger.info(f"プロンプト：\n{prompt}")
    updated_readme = llm_service.get_response(prompt, remove_code_block=True)

    logger.info(f">> updated_readme：\n{updated_readme}")
    
    # 更新されたREADMEの内容をファイルに書き込む
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_readme)

    logger.info("READMEの更新が完了しました。")

if __name__ == "__main__":
    main()
