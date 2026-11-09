import streamlit as st
st.title("ความโค้งที่อันตราบ")
m = st.number_input("ระยะการกระจัดของโค้ง(เมตร):", value=0.0)
c = st.number_input("ระยtจากกึ่งกลางของการกระจัดของโค้งจนถึงโค้ง(เมตร):", value=0.0)
R = (c ** 2 / 8 * m) + (m / 2)
V(max) = (R * 127 * 0.2) ** 0.5
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{R:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {V(max):.2f} บาท")
st.divider()
