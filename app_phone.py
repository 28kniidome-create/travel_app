import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="旅行アプリ",
    layout="centered"
)

st.markdown("""
<style>
/* 画面の余白を少し広げて見やすくする */
.block-container {
    padding-top: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

/* expander（日付部分）を見やすく */
div[data-testid="stExpander"] summary {
    font-size: 18px;
    font-weight: 600;
}

/* 全体の文字を少し柔らかく */
html, body, [class*="css"] {
    font-family: sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.title("旅程表アプリ作ってみたよ")

trip_name = "九州旅行"
st.header(trip_name)

url = "https://docs.google.com/spreadsheets/d/1T4VP9sBIsyoVQl6saTpQLxgtR7GC_7w1G21tddQjDVM/export?format=csv&gid=0"

df = pd.read_csv(url)

df["日付"] = df["日付"].ffill()

for date in df["日付"].unique():

    with st.expander(f"{date}"):

        day_df = df[df["日付"] == date]

        for index, row in day_df.iterrows():

            time = ""

            if pd.notna(row["時刻"]):
                time = str(row["時刻"])[:5]

            if pd.notna(row["場所"]):

                if time != "":
                    st.info(f"🕒 {time}　{row['場所']}")
                else:
                    st.markdown(f"📍 {row['場所']}")

                if pd.notna(row["備考"]):
                    st.caption(f"💡 {row['備考']}")

                if pd.notna(row["URL"]):

                    button_text = "URL"

                    if "maps.app" in row["URL"].lower():
                        button_text = "🗺️ Google マップ"

                    st.link_button(button_text, row["URL"])

                st.write("")

total_cost = df["金額"].sum()

st.metric(
    label="旅行予算合計",
    value=f"¥{total_cost:,}"
)