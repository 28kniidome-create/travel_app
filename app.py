import streamlit as st
import pandas as pd

st.title("旅行アプリ")

url = "https://docs.google.com/spreadsheets/d/1T4VP9sBIsyoVQl6saTpQLxgtR7GC_7w1G21tddQjDVM/export?format=csv&gid=0"

df = pd.read_csv(url)

current_date = None

for index, row in df.iterrows():

    if pd.notna(row["日付"]):
        current_date = row["日付"]
        st.divider()
        st.subheader(f"{current_date}")

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

            button_text = "🔗 開く"

            if "maps.app.goo.gl" in row["URL"].lower():
                button_text = "🗺️ 地図を見る"

            st.link_button(button_text, row["URL"])
            st.write("")

total_cost = df["金額"].sum()

st.metric(
    label="旅行予算合計",
    value=f"¥{total_cost:,}"
)