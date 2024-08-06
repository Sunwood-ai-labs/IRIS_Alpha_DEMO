# IRIS_Alpha_DEMO

[![Release](https://raw.githubusercontent.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/main/.github/release_notes/header_image/release_header_latest.png)](https://raw.githubusercontent.com/Sunwood-ai-labs/IRIS_Alpha_DEMO/main/.github/release_notes/header_image/release_header_latest.png)

# 最新のリリースノート:

## IRIS リリースノート - バージョン v1.1.0

リリース日: 2024-08-06

## 新機能

- フィボナッチ数列生成機能が追加されました。
    - 指定された数のフィボナッチ数列を返す `fibonacci(n)` 関数。
    - 再帰的なアプローチを用いた `fibonacci_recursive(n)` 関数。
    - 与えられた数がフィボナッチ数列に含まれているかどうかを判定する `is_fibonacci(num)` 関数。
- フィボナッチ数列ジェネレータの使用例が追加されました。
    - `examples/fibonacci_examples.py` にて、`fibonacci(n)`、`fibonacci_recursive(n)`、`is_fibonacci(num)` 関数の使用方法を示す例が確認できます。

## 変更点

- リリースノート生成時のヘッダーフォントファミリーが修正されました。
    - 従来は "Times New Roman" が使用されていましたが、一部環境で正常に表示されない問題がありました。
    - 今後は "DejaVu Math TeX Gyre" を使用することで、多くの環境での表示互換性が向上しました。
- 不要なログ出力が削除されました。
    - `translate_readme.py` および `generate_header_image.py` から、不要なログ出力設定が削除されました。

---

# リポジトリのサマリー:
# Project: IRIS_Alpha_DEMO

```plaintext
OS: posix
Directory: /home/runner/work/IRIS_Alpha_DEMO/IRIS_Alpha_DEMO

├─ examples/
│  ├─ fibonacci_examples.py
├─ fibonacci.py
├─ issue_creator.log
├─ README.md
```

## .

`fibonacci.py`

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = fibonacci_recursive(n - 1)
    fib.append(fib[-1] + fib[-2])
    return fib

def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num
```

`issue_creator.log`

```plaintext

```

`README.md`

```markdown
# IRIS_Alpha_DEMO
```

## .github

`.github/labels.csv`

```plaintext
label,description
bug,何かが正常に動作していません
documentation,ドキュメントの改善または追加
duplicate,このイシューまたはプルリクエストは既に存在します
enhancement,新機能または要望
feature,新機能または要望
good first issue,初心者に適しています
help wanted,追加の注意が必要です
invalid,これは適切ではないようです
question,さらなる情報が必要です
wontfix,これは対応されません
```

---

<!-- Automated update --># Last updated: Tue Aug  6 11:29:15 UTC 2024 - Release: v1.1.0 - Run ID: 10265646027
<!-- Automated update -->
