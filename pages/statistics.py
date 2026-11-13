import streamlit as st

from services.cal_mode import cal_mode
from services.cal_statistics import cal_mean, cal_median, cal_sd, cal_variance, parse_numbers

st.title("📈 Descriptive Statistics")
st.write("Enter numbers to calculate Mean, Median, Mode, Standard Deviation and Variance.")

with st.form("stats_form"):
    text = st.text_input("Numbers (separated by commas or spaces)", value="-100, 0, 10, 20, 30, 100")
    st.form_submit_button("Enter", type="primary")

try:
    data = parse_numbers(text)
except ValueError as e:
    st.error(f"{e}. Example: -100, 0, 10, 20, 30, 100")
    st.stop()

mean = cal_mean(data)
median = cal_median(data)
modes = cal_mode(data)
variance = cal_variance(data)
sd = cal_sd(data)

st.subheader("Results")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Mean", f"{mean:.2f}")
col2.metric("Median", f"{median:.2f}")
col3.metric("Mode", ", ".join(f"{m:g}" for m in modes) if modes else "No mode")
col4.metric("SD", f"{sd:.2f}")
col5.metric("Variance", f"{variance:.2f}")

st.subheader("How it is calculated")
st.markdown(
    """
- **Mean**: add all numbers, then divide by how many numbers there are.
- **Median**: sort the numbers and take the middle one. If there are two middle numbers, take their average.
- **Mode**: the number that appears most often. If every number appears once, there is no mode.
- **Variance**: the average of (number − mean)².
- **SD**: the square root of the variance.
"""
)
