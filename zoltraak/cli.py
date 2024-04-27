import argparse
import os
import os.path
import zoltraak

current_directory = os.path.dirname(os.path.abspath(__file__))

# print(package_dir)
# from zoltraak.md_generator import generate_md_from_prompt
from zoltraak.converter import convert_md_to_py
import zoltraak.llms.claude as claude

def main():
    current_dir = os.getcwd()
    package_dir = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(description="MarkdownファイルをPythonファイルに変換します")
    parser.add_argument("input", help="変換対象のMarkdownファイルのパスまたはテキスト", nargs='?')
    parser.add_argument("--output-dir", help="生成されたPythonファイルの出力ディレクトリ", default="generated")
    parser.add_argument("-p", "--prompt", help="追加のプロンプト情報", default=None)
    parser.add_argument("-c", "--compiler", help="コンパイラー（要件定義書のテンプレート）")
    parser.add_argument("-f", "--formatter", help="コードフォーマッター", default="md_comment")
    parser.add_argument("-cc", "--custom-compiler", help="自作コンパイラー（自作定義書生成文書）")
    parser.add_argument("-v", "--version", action="store_true", help="バージョン情報を表示")  # 追加: バージョン情報表示オプション
    args = parser.parse_args()

    if args.version:                                                         # バージョン情報表示オプションが指定された場合
        show_version_and_exit()                                              # - バージョン情報を表示して終了

    if args.input is None:                                                   # 入力ファイルまたはテキストが指定されていない場合
        show_usage_and_exit()                                                # - 使用方法を表示して終了

    if args.input.endswith(".md") or os.path.isfile(args.input) or os.path.isdir(
        args.input
    ):                                                                       # 入力がMarkdownファイル、ファイル、またはディレクトリの場合
        print(args.input)
        print("mo")
        if args.compiler is None and args.custom_compiler is None:           # -- コンパイラーが指定されていない場合
            args.compiler = "dev_obj"                                        # --- デフォルトのコンパイラー（general_def）を使用
        elif args.compiler and args.custom_compiler:                         # -- デフォルトのコンパイラーとカスタムコンパイラーの両方が指定されている場合
            show_compiler_conflict_error_and_exit()                          # --- コンパイラー競合エラーを表示して終了
        
        process_markdown_file(args)                                          # - Markdownファイルを処理する関数を呼び出す
    else:                                                                    # 入力がテキストの場合
        if args.compiler is None and args.custom_compiler is None:           # -- コンパイラーが指定されていない場合  
            show_compiler_error_and_exit()                                   # --- コンパイラーエラーを表示して終了
        elif args.compiler and args.custom_compiler:                         # -- デフォルトのコンパイラーとカスタムコンパイラーの両方が指定されている場合
            show_compiler_conflict_error_and_exit()                          # --- コンパイラー競合エラーを表示して終了
        
        process_text_input(args)                                             # - テキスト入力を処理する関数を呼び出す






def show_version_and_exit():
    print(f"zoltraak version {zoltraak.__version__}")
    exit(0)

def show_usage_and_exit():
    print("\033[31mエラー: 入力ファイルまたはテキストが指定されていません。\033[0m")
    print("\033[92m使用方法: zoltraak <mdファイルのパス または テキスト> [オプション]\033[0m")
    print("\033[33m例1:\033[0m zoltraak calc.md -p \"ドローンを用いた競技システムを考える\" -c dev_obj")
    print("  説明: calc.mdファイルを入力とし、ドローンを用いた競技システムの要件定義書を生成します。")
    print("        オブジェクト指向設計のコンパイラー（dev_obj）を使用します。")
    print("\033[33m例2:\033[0m zoltraak \"タクシーの経営課題を解決するための戦略ドキュメントを作成する\" -c biz_consult")
    print("  説明: プロンプトテキストを入力とし、タクシー会社の経営課題解決のための戦略ドキュメントを生成します。")
    print("        ビジネスコンサルティング用のコンパイラー（biz_consult）を使用します。")
    print("\033[33m例3:\033[0m zoltraak \"レストランの予約管理システムの要件定義書\" -cc custom_compiler.md")
    print("  説明: プロンプトテキストを入力とし、レストランの予約管理システムの要件定義書を生成します。")
    print("        カスタムコンパイラー（custom_compiler.md）を使用します。")
    exit(1)

def show_compiler_error_and_exit():
    print("\033[31mエラー: コンパイラーが指定されていません。\033[0m")
    print("-c オプションでデフォルトのコンパイラーを指定するか、")
    print("-cc オプションで自作のコンパイラー（要件定義書のテンプレート）のファイルパスを指定してください。")
    print("\033[92mデフォルトのコンパイラー:\033[0m")
    print("\033[33m- dev_obj: オブジェクト指向設計を用いた開発タスクに関する要件定義書を生成するコンパイラ\033[0m")
    print("  説明: オブジェクト指向の原則に基づいて、開発タスクの要件定義書を生成します。クラス図、シーケンス図、ユースケースなどを含みます。")
    print("\033[33m- dev_func: 関数型プログラミングを用いた開発タスクに関する要件定義書を生成するコンパイラ\033[0m")
    print("  説明: 関数型プログラミングの原則に基づいて、開発タスクの要件定義書を生成します。純粋関数、不変性、高階関数などの概念を取り入れます。")
    print("\033[33m- biz_consult: ビジネスコンサルティングに関するドキュメントを生成するコンパイラ\033[0m")
    print("  説明: 企業の課題解決や戦略立案のためのコンサルティングドキュメントを生成します。市場分析、SWOT分析、アクションプランなどを含みます。")
    print("\033[33m- general_def: 一般的な開発タスクに関する要件定義書を生成するコンパイラ\033[0m")
    print("  説明: 様々な開発タスクに対応した汎用的な要件定義書を生成します。システムの目的、機能要件、非機能要件などを網羅します。")
    print("\033[33m- general_reqdef: 一般的な要求事項に関する要件定義書を生成するコンパイラ\033[0m")
    print("  説明: システム開発以外の一般的な要求事項について、要件定義書を生成します。プロジェクトの目標、スコープ、制約条件などを明確にします。")
    exit(1)

def show_compiler_conflict_error_and_exit():
    print("\033[31mエラー: -c オプションと -cc オプションは同時に指定できません。\033[0m")
    exit(1)

def process_markdown_file(args):
    """
    Markdownファイルを処理する
    """
    # print(os.path.basename(args.input))
    # print(os.path.basename(args.input))
    # # md_file_path = os.path.join("requirements", os.path.basename(args.input))
    # md_file_path = os.path.join("requirements", os.path.basename(args.input))
    md_file_path = args.input
    print("md_file_path:", md_file_path)
    output_dir = os.path.abspath(args.output_dir)
    print("output_dir:", output_dir)
    prompt = args.prompt

    zoltraak_dir = os.path.dirname(zoltraak.__file__)

    if args.custom_compiler:
        compiler_path = get_custom_compiler_path(args.custom_compiler)
    else:
        compiler_path = os.path.join(zoltraak_dir, "setting/compiler", args.compiler + ".md")
        print(f"デフォルトコンパイラーのパス: {compiler_path}")

    formatter_path = os.path.join(zoltraak_dir, "setting/formatter", args.formatter + ".md")
    print("compiler_path:", compiler_path)
    print("formatter_path:", formatter_path)

    md_file_rel_path = os.path.relpath(md_file_path, os.getcwd())
    py_file_rel_path = os.path.splitext(md_file_rel_path)[0] + ".py"
    py_file_path = os.path.join(output_dir, py_file_rel_path)

    os.makedirs(os.path.dirname(py_file_path), exist_ok=True)
    convert_md_to_py(
        md_file_path,
        py_file_path,
        prompt,
        compiler_path,
        formatter_path,
    )

def get_custom_compiler_path(custom_compiler):
    compiler_path = os.path.abspath(custom_compiler)
    if not os.path.exists(compiler_path):
        print(f"\033[31mエラー: 指定されたカスタムコンパイラーのファイル '{compiler_path}' が存在しません。\033[0m")
        print("\033[33m以下の点を確認してください:\033[0m")
        print("1. ファイルが指定されたパスに存在することを確認してください。")
        print("2. カスタムコンパイラーのファイルパスが正しいことを確認してください。")
        print("3. ファイル名の拡張子が '.md' であることを確認してください。")
        print("4. ファイルの読み取り権限があることを確認してください。")
        exit(1)
    print(f"カスタムコンパイラーのパス: {compiler_path}")
    return compiler_path

def process_text_input(args):
    text = args.input
    md_file_path = generate_md_file_name(text)
    print(f"新しい要件定義書 '{md_file_path}' が生成されました。")
    prompt = f"{text}"

    if args.custom_compiler:
        os.system(f"zoltraak {md_file_path} -p \"{prompt}\" -cc {args.custom_compiler} -f {args.formatter}")
    else:
        os.system(f"zoltraak {md_file_path} -p \"{prompt}\" -c {args.compiler} -f {args.formatter}")
def generate_md_file_name(prompt):
    # promptからファイル名を生成するためにgenerate_response関数を利用

    # requirementsディレクトリが存在しない場合は作成する
    requirements_dir = "requirements"
    if not os.path.exists(requirements_dir):
        os.makedirs(requirements_dir)

    # zoltraak/requirements/内のファイル名を全て取得
    existing_files = [file for file in os.listdir(requirements_dir) if file.startswith("def_")]

    # print("existing_files:", existing_files)

    # 既存のファイル名と被らないようにファイル名を生成するプロンプトを作成
    file_name_prompt = f"{prompt}に基づいて、要件定義書のファイル名をdef_hogehoge.mdの形式で提案してください。\n"
    file_name_prompt += f"ただし、以下の既存のファイル名と被らないようにしてください。\n{', '.join(existing_files)}\n"
    file_name_prompt += "ファイル名のみをアウトプットしてください。\n"
    # print("file_name_prompt:", file_name_prompt)
    response = claude.generate_response(file_name_prompt)
    file_name = response.strip()
    return f"{file_name}"

