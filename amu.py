import streamlit as st
st.title("ความโค้งที่อันตราบ")
m = st.number_input("ระยะการกระจัดของโค้ง(เมตร):", value=0.0, step=1.0)
c = st.number_input("ระยtจากกึ่งกลางของการกระจัดของโค้งจนถึงโค้ง(เมตร):", value=0.0, step=1.0)
R = ((c ** 2) / (8 * m)) + (m / 2)
V_max = (R * 127 * 0.2) ** 0.5
st.header(f"• รัศมีโค้ง: **{R:.2f}** องศา")
st.header(f"• ความเร็วสูงสุด: {V_max:.2f} กิโลเมตรต่อชั่วโมง")
st.divider()
