
import streamlit as st
from services.text_prediction import (
    load_data,
    get_text,
    build_matrix,
    predict_word,
    generate_text,
    build_matrix_table,
    get_last_word,
    build_prediction_table,
)

st.title("Markov Chain Prediction")
st.write("ระบบทำนายคำถัดไปด้วย Markov Chain")



# ส่วนแสดงผลหน้าเว็บ
data = load_data()

if data is not None:

    st.subheader("เลือกชุดข้อมูล")

    if isinstance(data, dict):
        dataset_names = list(data.keys())

        selected = st.selectbox(
            "เลือก Dataset",
            dataset_names
        )

        text = get_text(data[selected])

    else:
        text = get_text(data)

    st.text_area(
        "ข้อมูลที่เลือก",
        text[:1000],
        height=120
    )

    if st.button("สร้าง Matrix"):

        if text.strip():
            st.session_state.matrix = build_matrix(text)
            st.success("สร้าง Matrix เรียบร้อยแล้ว")
        else:
            st.warning("ไม่พบข้อมูลใน Dataset")

else:
    st.warning("ไม่พบไฟล์ raw_data.json")
    text = st.text_area("กรอกข้อความเพื่อใช้เป็นข้อมูล")

    if st.button("สร้าง Matrix"):
        if text.strip():
            st.session_state.matrix = build_matrix(text)
            st.success("สร้าง Matrix เรียบร้อยแล้ว")
        else:
            st.warning("กรุณากรอกข้อมูลก่อน")


# แสดง Matrix และทำนายคำ
if "matrix" in st.session_state:

    matrix = st.session_state.matrix

    st.subheader("Transition Probability Matrix")

    df = build_matrix_table(matrix)

    st.dataframe(
        df.style.format("{:.3f}"),
        use_container_width=True
    )

    st.divider()

    st.subheader("ทำนายคำถัดไป")

    start = st.text_input(
        "กรอกคำเริ่มต้น",
        placeholder="เช่น I love"
    )

    amount = st.slider(
        "จำนวนคำที่ต้องการทำนาย",
        1, 20, 5
    )

    if st.button("ทำนาย"):

        if start.strip():

            current = get_last_word(start)
            result = predict_word(matrix, current)

            if result:

                st.write("คำที่มีโอกาสเป็นคำถัดไป")

                prediction_df = build_prediction_table(result)

                st.dataframe(
                    prediction_df,
                    use_container_width=True
                )

                sentence = generate_text(
                    matrix,
                    start,
                    amount
                )

                st.write("ประโยคที่ระบบทำนายได้")
                st.success(sentence)

            else:
                st.warning("ไม่พบคำนี้ในชุดข้อมูล")

        else:
            st.warning("กรุณากรอกคำเริ่มต้น")
