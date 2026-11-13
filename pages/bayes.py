import streamlit as st
from services.bayes_service import calculate_bayes

st.title("Bayes' Theorem")
st.write("Calculate Posterior Probability using Bayes' Theorem.")
st.subheader("Enter Probability Values")

prior = st.number_input(
    "Prior Probability P(A)",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

likelihood = st.number_input(
    "Likelihood P(B|A)",
    min_value=0.0,
    max_value=1.0,
    value=0.8,
    step=0.01
)

evidence = st.number_input(
    "Evidence P(B)",
    min_value=0.000001,
    max_value=1.0,
    value=0.5,
    step=0.01
)

if st.button("Calculate"):
    try:
        result = calculate_bayes(prior, likelihood, evidence)
        st.success("Calculation completed!")
        st.metric(
            label="Posterior Probability P(A|B)",
            value=f"{result:.4f}",
            delta=f"{result:.2%}"
        )
        st.info(
            f"The posterior probability is {result:.2%}."
        )
        st.write(
           "This result shows the probability of event A "
           "after observing evidence B."
       )
    except ValueError as e:
        st.error(str(e))
 