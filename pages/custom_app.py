import streamlit as st
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["Tahoma", "Loma"]

from services.custom_service import calculate

st.title("Matrix Transform Visualizer")
st.write("ดูว่าเมทริกซ์ 2x2 เปลี่ยนเวกเตอร์และรูปสี่เหลี่ยมอย่างไร")

#ตัวอย่างปุ่มเมทริก
presets = {
    "กำหนดเอง": (2, 0, 0, 1),
    "ขยาย x2": (2, 0, 0, 2),
    "หมุน 90°": (0, -1, 1, 0),
    "สะท้อนแกน x": (1, 0, 0, -1),
    "Shear": (1, 1, 0, 1),
    "Singular (det=0)": (1, 2, 2, 4),
}
choice = st.selectbox("เลือกตัวอย่าง", list(presets.keys()))
pa, pb, pc, pd = presets[choice]

#ช่องเมทริก
st.subheader("เมทริกซ์ M")
col1, col2 = st.columns(2)
a = col1.number_input("a", value=float(pa), key=f"a_{choice}")
b = col2.number_input("b", value=float(pb), key=f"b_{choice}")
c = col1.number_input("c", value=float(pc), key=f"c_{choice}")
d = col2.number_input("d", value=float(pd), key=f"d_{choice}")

#ช่องเวกเตอ
st.subheader("เวกเตอร์ v")
col3, col4 = st.columns(2)
x = col3.number_input("x", value=1.0)
y = col4.number_input("y", value=2.0)

if st.button("คำนวณ"):
    #ส่งค่าไปคำนวณที่ service
    new_v, det, inv, square, new_square = calculate(a, b, c, d, x, y)

    #แสดงผลเป็นข้อความ
    st.subheader("ผลลัพธ์")
    st.write(f"Mv = ({new_v[0]:.2f}, {new_v[1]:.2f})")
    st.write(f"determinant = {det:.2f}")
    if inv is None:
        st.warning("ไม่มี inverse เพราะ det = 0 (เมทริกซ์บีบรูปให้แบน)")
    else:
        st.write("inverse =")
        st.write(inv)

    #กราฟ
    fig, ax = plt.subplots()
    ax.plot(square[0], square[1], "k--", label="สี่เหลี่ยมเดิม")
    ax.fill(new_square[0], new_square[1], color="red", alpha=0.3, label="หลังแปลง")
    ax.arrow(0, 0, x, y, head_width=0.2, color="blue", length_includes_head=True)
    ax.arrow(0, 0, new_v[0], new_v[1], head_width=0.2, color="red", length_includes_head=True)
    ax.text(x, y, " v", color="blue")
    ax.text(new_v[0], new_v[1], " Mv", color="red")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.axhline(0, color="black")
    ax.axvline(0, color="black")
    ax.grid(True)
    ax.set_aspect("equal")
    ax.legend()
    st.pyplot(fig)