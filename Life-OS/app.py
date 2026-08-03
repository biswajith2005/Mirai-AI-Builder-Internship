import streamlit as st
import pandas as pd
import plotly.express as px
from google import genai
from dotenv import load_dotenv
import os
import os
from urllib.parse import quote

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.set_page_config(
    page_title="Life-OS Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

def prepare_summary(dataframe):
    """
    Summarizes the selected day's screen time by category
    and converts it into a clean string for Gemini.
    """

    summary = (
        dataframe.groupby("Category")["Minutes_Used"]
        .sum()
        .reset_index()
        .sort_values(by="Minutes_Used", ascending=False)
    )

    return summary.to_string(index=False)

st.title("🧠 Life-OS Wellbeing Dashboard")
st.caption("Track your digital habits and receive AI-powered lifestyle coaching.")

df = pd.read_csv("screentime.csv")

df["Date"] = pd.to_datetime(df["Date"])

st.subheader("📊 Screen Time Data")

st.dataframe(df, use_container_width=True)

st.sidebar.title("⚙ Controls")

selected_day = st.sidebar.selectbox(
    "Select a Day",
    sorted(df["Date"].dt.date.unique(), reverse=True)
)

daily_goal = st.sidebar.slider(
    "Daily Screen Time Goal (Hours)",
    min_value=1,
    max_value=12,
    value=5
)

st.sidebar.success(f"Current Goal: {daily_goal} hours/day")

today_df = df[df["Date"].dt.date == selected_day]

summary_text = prepare_summary(today_df)



# Total minutes used today
total_minutes = today_df["Minutes_Used"].sum()

# Convert to hours
total_hours = round(total_minutes / 60, 1)

# Most used app
top_app = today_df.loc[
    today_df["Minutes_Used"].idxmax(),
    "App_Name"
]

# Goal in minutes
goal_minutes = daily_goal * 60

# Difference from goal
difference = total_minutes - goal_minutes

difference_hours = round(difference / 60, 1)

prompt = f"""
You are Life-OS, an expert digital wellbeing and productivity coach.

Here is today's screen time summary:

{summary_text}

Total Screen Time: {total_hours} hours
Daily Goal: {daily_goal} hours

Your task:

1. Give the user a Productivity Score out of 10.

2. Explain the user's biggest unhealthy habit.

3. Mention one positive habit.

4. Suggest exactly three practical real-world alternatives instead of excessive screen time.
Examples:
- Go for a walk
- Read a book
- Meal prep
- Exercise
- Stretch
- Meditation
- Meet a friend
- Practice a hobby

5. End with a short motivational paragraph.

Rules:
- Be supportive but honest.
- Do NOT simply say "use your phone less."
- Base every suggestion on the provided data.
- Format your response using Markdown headings and bullet points.
"""

st.subheader(f"Usage for {selected_day}")

st.dataframe(today_df, use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📱 Total Screen Time",
        value=f"{total_hours} hrs"
    )

with col2:
    st.metric(
        label="🔥 Most Used App",
        value=top_app
    )

with col3:
    st.metric(
        label="🎯 Goal Difference",
        value=f"{total_hours} hrs",
        delta=f"{difference_hours:+.1f} hrs",
        delta_color="inverse"
    )

daily_usage = (
    df.groupby("Date")["Minutes_Used"]
    .sum()
    .reset_index()
)

delta_color="inverse"

progress = min(total_minutes / goal_minutes, 1.0)

st.subheader("🎯 Daily Goal Progress")

st.progress(progress)

st.write(
    f"Used **{total_hours} hrs** out of **{daily_goal} hrs** goal."
)

st.divider()

with st.expander("📄 View Today's Raw Data"):
    st.dataframe(today_df, use_container_width=True)

st.subheader("📈 14-Day Screen Time Trend")

fig = px.line(
    daily_usage,
    x="Date",
    y="Minutes_Used",
    markers=True,
    title="Daily Screen Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Minutes Used",
    height=450
)

st.plotly_chart(fig, use_container_width=True)

category_usage = (
    today_df.groupby("Category")["Minutes_Used"]
    .sum()
    .reset_index()
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("📊 Category Usage")

    bar_fig = px.bar(
        category_usage,
        x="Category",
        y="Minutes_Used",
        color="Category"
    )

    st.plotly_chart(bar_fig, use_container_width=True)

with col2:

    st.subheader("🥧 Screen Time Distribution")

    pie_fig = px.pie(
        category_usage,
        names="Category",
        values="Minutes_Used"
    )

    st.plotly_chart(pie_fig, use_container_width=True)

csv = today_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Today's Data",
    data=csv,
    file_name=f"{selected_day}_screen_time.csv",
    mime="text/csv"
)

st.subheader("🔍 Data Sent to Gemini")

st.code(summary_text)

st.divider()

st.header("🧠 AI Lifestyle Coach")

if st.button("Generate AI Coaching"):

    with st.spinner("Analyzing your screen habits..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        advice = response.text

        avatar_prompt = f"""
        Based on the following screen time:

{summary_text}

Generate ONLY a short image prompt.

If productivity is high,
describe a disciplined successful person.

If screen time is excessive,
describe a lazy person addicted to their phone.

Do not explain anything.

Only output the image description.
"""
        avatar_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=avatar_prompt
)

        image_prompt = avatar_response.text.strip()

        encoded_prompt = quote(image_prompt)

        image_url = (
    f"https://image.pollinations.ai/prompt/{encoded_prompt}"
    "?width=1024&height=1024&seed=42"
)

        if total_hours < 4:
            st.success(advice)

        elif total_hours < 6:
            st.info(advice)

        elif total_hours < 8:
            st.warning(advice)

        else:
            st.error(advice)

        st.subheader("🎭 Your Digital Reflection")

        st.image(
    image_url,
    caption="AI-generated reflection based on today's digital habits.",
    use_container_width=True
)