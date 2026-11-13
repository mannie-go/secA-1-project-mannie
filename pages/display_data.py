import streamlit as st
import os
from services.data_service import load_data, build_table

st.title(" แสดงข้อมูลดิบ (Data Viewer)")
st.markdown("ดึงข้อมูลจากโฟลเดอร์ `data/` มาจัดรูปแบบและแสดงผลให้อ่านง่าย")

file_path = os.path.join("data", "raw_data.json")

if os.path.exists(file_path):
    data = load_data(file_path)
    
    st.subheader("1. การแสดงผลในรูปแบบ JSON")
    st.json(data)
    
    st.subheader("2. การแสดงผลในรูปแบบตารางสรุป")
    try:
        df = build_table(data)
            
        st.dataframe(df, use_container_width=True)
    except ValueError:
        st.info(" รูปแบบของข้อมูลในไฟล์ raw_data.json มีโครงสร้างที่ซับซ้อนเกินกว่าจะแสดงเป็นตารางอัตโนมัติได้")
        
else:
    st.error(f" ไม่พบไฟล์: `{file_path}` โปรดตรวจสอบให้แน่ใจว่าได้วางไฟล์ข้อมูลดิบไว้ในโฟลเดอร์ data/ ของโปรเจกต์กลุ่มแล้ว")