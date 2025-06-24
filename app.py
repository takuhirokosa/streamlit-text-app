import streamlit as st
from PIL import Image
import io

# ページ設定
st.set_page_config(
    page_title="テキスト入力アプリ",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# メイン画面のタイトル
st.title("📝 テキスト入力・表示アプリ")
st.markdown("---")

# サイドバーの設定
st.sidebar.header("設定オプション")
st.sidebar.markdown("### テキストスタイル設定")

# サイドバーでスタイルオプションを選択
text_style = st.sidebar.selectbox(
    "テキストスタイルを選択:",
    ["通常", "太字", "イタリック", "太字+イタリック", "コード"]
)

text_color = st.sidebar.color_picker("テキストカラー", "#000000")
background_color = st.sidebar.color_picker("背景カラー", "#FFFFFF")

# メイン画面を2つのカラムに分割
col1, col2 = st.columns([2, 1])

with col1:
    st.header("テキスト入力セクション")
    
    # テキスト入力フォーム
    user_input = st.text_area(
        "テキストを入力してください:",
        height=150,
        placeholder="ここにテキストを入力..."
    )
    

    
    # 送信ボタン
    submit_button = st.button("テキストを表示", type="primary")

with col2:
    st.header("画像アップロード")
    
    # 画像アップロード機能
    uploaded_file = st.file_uploader(
        "画像を選択してください",
        type=['png', 'jpg', 'jpeg', 'gif'],
        help="PNG, JPG, JPEG, GIF形式がサポートされています"
    )
    
    # 画像表示
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="アップロードされた画像", use_column_width=True)
            
            # 画像情報を表示
            st.info(f"ファイル名: {uploaded_file.name}")
            st.info(f"画像サイズ: {image.size}")
            st.info(f"ファイルサイズ: {len(uploaded_file.getvalue())} bytes")
            
        except Exception as e:
            st.error(f"画像の読み込みに失敗しました: {e}")

# 結果表示セクション
st.markdown("---")
st.header("📋 入力結果表示")

if submit_button or user_input:
    
    # 表示用のカラムを作成
    display_col1, display_col2 = st.columns([3, 2])
    
    with display_col1:
        if user_input:
            st.subheader("長文テキスト:")
            
            # スタイルを適用してテキストを表示
            styled_text = user_input
            
            if text_style == "太字":
                styled_text = f"<strong>{styled_text}</strong>"
            elif text_style == "イタリック":
                styled_text = f"<em>{styled_text}</em>"
            elif text_style == "太字+イタリック":
                styled_text = f"<strong><em>{styled_text}</em></strong>"
            elif text_style == "コード":
                styled_text = f"<code style='background-color: #f0f0f0; padding: 2px 4px; border-radius: 3px;'>{styled_text}</code>"
            
            # カスタムCSSでカラーを適用
            st.markdown(
                f"""
                <div style="
                    color: {text_color};
                    background-color: {background_color};
                    padding: 10px;
                    border-radius: 5px;
                    border: 1px solid #ddd;
                ">
                {styled_text}
                </div>
                """,
                unsafe_allow_html=True
            )

            
    with display_col2:
        if user_input:
            st.subheader("テキスト統計:")
            total_chars = len(user_input)
            total_words = len(user_input.split())
            
            st.metric("総文字数", total_chars)
            st.metric("総単語数", total_words)
            st.metric("適用スタイル", text_style)

# フッター
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666; font-size: 0.8em;">
    © 2025 Streamlit基本アプリ | 作成者: Claude
    </div>
    """,
    unsafe_allow_html=True
)