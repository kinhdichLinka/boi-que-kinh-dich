import streamlit as st
import datetime

# --- Danh sách 64 quẻ Kinh Dịch và ý nghĩa ---
ten_que = {
    (1, 1): ("Càn vi Thiên", "Thuần Càn tượng trưng cho trời, sức mạnh, sự khởi đầu lớn."),
    (2, 2): ("Khôn vi Địa", "Thuần Khôn tượng trưng cho đất, nhu thuận, dưỡng nuôi."),
    (1, 2): ("Thủy Thiên Nhu", "Tình thế đang khó khăn, cần nhẫn nại chờ thời."),
    (2, 1): ("Thiên Địa Bĩ", "Bế tắc, không thông. Nên an phận và chờ cơ hội."),
    # ... (Thêm đầy đủ 64 quẻ như trên)
    (63, 63): ("Thủy Hỏa Ký Tế", "Mọi việc đã hoàn thành, nên duy trì và ổn định."),
    (64, 64): ("Hỏa Thủy Vị Tế", "Việc chưa xong, cần kiên trì và tránh hấp tấp.")
}

# Hàm lấy tên và ý nghĩa quẻ
def lay_ten_va_y_nghia_que(thuong, ha):
    return ten_que.get((thuong, ha), ("Chưa rõ", "Đang cập nhật..."))

# --- Giao diện Streamlit ---
st.title("🧧 Gieo Quẻ Kinh Dịch - Mai Hoa Dịch Số")

st.markdown("""
Hãy nhập thông tin **ngày âm lịch** và **giờ sinh** để xem quẻ dịch, tên quẻ, ý nghĩa và lưu lại lịch sử cá nhân.
""")

# Nhập ngày âm lịch
col1, col2, col3 = st.columns(3)
am_ngay = col1.number_input("Ngày (âm lịch)", min_value=1, max_value=30, value=1)
am_thang = col2.number_input("Tháng (âm lịch)", min_value=1, max_value=12, value=1)
am_nam = col3.number_input("Năm (âm lịch)", min_value=1900, max_value=2100, value=2024)

# Nhập giờ sinh theo 12 chi
gio_sinh = st.selectbox("Giờ sinh (theo 12 Chi)", [
    "Tý (23h-1h)", "Sửu (1h-3h)", "Dần (3h-5h)", "Mão (5h-7h)",
    "Thìn (7h-9h)", "Tỵ (9h-11h)", "Ngọ (11h-13h)", "Mùi (13h-15h)",
    "Thân (15h-17h)", "Dậu (17h-19h)", "Tuất (19h-21h)", "Hợi (21h-23h)"
])

if st.button("🔮 Gieo Quẻ"):
    # Tính toán số quẻ và hào động từ ngày âm + giờ sinh (giản lược)
    so_que_thuong = (am_ngay + am_thang) % 64 or 64
    so_que_ha = (am_thang + am_nam) % 64 or 64
    hao_dong = (am_ngay + am_thang + am_nam) % 6 or 6

    ten, y_nghia = lay_ten_va_y_nghia_que(so_que_thuong, so_que_ha)

    st.subheader(f"🧿 Tên Quẻ: {ten}")
    st.markdown(f"**Ý nghĩa:** {y_nghia}")

    st.info(f"Ngày âm lịch: {am_ngay}/{am_thang}/{am_nam} — Giờ sinh: {gio_sinh}")
    st.write(f"Hào động: {hao_dong} (Xem kỹ hào {hao_dong} để hiểu chiều hướng biến đổi)")

    # Lưu lịch sử trong session
    if "lich_su" not in st.session_state:
        st.session_state.lich_su = []
    st.session_state.lich_su.append({
        "ngay": f"{am_ngay}/{am_thang}/{am_nam}",
        "gio": gio_sinh,
        "que": ten,
        "hao": hao_dong
    })

# --- Hiển thị lịch sử gieo quẻ ---
if "lich_su" in st.session_state:
    st.markdown("## 📜 Lịch sử các lần gieo quẻ")
    for idx, record in enumerate(reversed(st.session_state.lich_su)):
        st.write(f"**Lần {len(st.session_state.lich_su)-idx}:** {record['ngay']} {record['gio']} → {record['que']} (Hào {record['hao']})")
