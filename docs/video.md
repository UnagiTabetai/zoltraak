# はじめに

このドキュメントでは、プロンプト、ドキュメント（自然言語）、プログラム（高級言語）、システムテスト項目の4つの状態を表現し、それらの間の遷移や同期をアニメーションで示す方法について説明します。アニメーションの作成にはPythonのライブラリであるmanim（Mathematical Animation Engine）を使用します。

# 各状態の表現

## テキストの作成

各状態を表すテキストを作成します。テキストには状態の名称を記載し、色とフォントサイズを指定します。プロンプトは赤色、ドキュメントは青色、プログラムは緑色、システムテスト項目はオレンジ色とします。フォントサイズは24に設定します。

## 図形の作成

各状態を表す図形を作成します。プロンプト、ドキュメント、プログラムは円形、システムテスト項目は四角形とします。初期の図形の色は白色とします。

## 図形の配置

作成した図形を横に並べます。図形間の間隔は1.5に設定します。

## テキストの配置

作成したテキストを対応する図形の上に配置します。

# アニメーションの構築

## 図形とテキストの表示

作成した図形とテキストを同時に表示します。図形の表示にはアニメーションを使用し、テキストの表示には単純な表示を使用します。

## 状態遷移の表現

状態間の遷移を矢印で表現します。矢印は白色とします。

1. プロンプトからドキュメントへの遷移
   - プロンプトの円形を赤色に変更し、1秒間待機します。
   - "zoltraak document -p prompt"というコマンドを表示し、1秒間待機します。
   - プロンプトからドキュメントへの矢印を表示し、ドキュメントの円形を青色に変更します。
   - 1秒間待機します。

2. ドキュメントからプログラムへの遷移
   - "zoltraakdocument"というコマンドを表示し、前のコマンドを非表示にします。
   - ドキュメントからプログラムへの矢印を表示し、プログラムの円形を緑色に変更します。
   - 1秒間待機します。

3. プログラムからシステムテスト項目への遷移
   - プログラムからシステムテスト項目への矢印を表示し、システムテスト項目の四角形をオレンジ色に変更します。
   - 1秒間待機します。

4. システムテスト項目からドキュメントへの遷移
   - システムテスト項目からドキュメントへの矢印を表示します。矢印の位置は他の矢印より下に配置します。
   - 1秒間待機します。

## 同期の表現

ドキュメントとプログラムの同期を表現するために、以下の手順を実行します。

1. "テスト項目を網羅されるまで、ドキュメントとプログラムの再構築が進む"というテキストを表示し、1秒間待機後に非表示にします。

2. ドキュメントとプログラムの間に双方向の黄色い矢印を表示します。

3. ドキュメントとプログラムの間に"Compile"というテキストを表示します。

4. "zoltraakdocument"というコマンドを表示し、前のコマンドを非表示にします。

5. ドキュメントが変更されたことを表現するために、ドキュメントの円形の色を薄い青色に変更し、フラッシュアニメーションを適用します。

6. プログラムが変更されたことを表現するために、プログラムの円形の色を薄い緑色に変更し、フラッシュアニメーションを適用します。これを2回繰り返します。

7. ドキュメントが再度変更されたことを表現するために、ドキュメントの円形の色を薄い青色に変更し、フラッシュアニメーションを適用します。

8. "zoltraakdocument を行うたびにシステム実行と双方の同期がチェックされる"というテキストを表示します。

# まとめ

このドキュメントでは、プロンプト、ドキュメント、プログラム、システムテスト項目の4つの状態とそれらの間の遷移や同期をアニメーションで表現する方法について説明しました。以下の手順でアニメーションを構築します。

1. 各状態を表すテキストと図形を作成し、適切に配置します。
2. 図形とテキストを表示します。
3. 状態間の遷移を矢印で表現します。
4. ドキュメントとプログラムの同期を双方向の矢印とフラッシュアニメーションで表現します。

このアニメーションにより、システムの状態遷移と同期の流れを視覚的に理解することができます。