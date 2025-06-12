import streamlit as st
import datetime
import random

# --- Danh sách một vài quẻ Kinh Dịch mẫu ---
ten_que = {
    (1, 1): ("Càn vi Thiên", "Thuần Càn tượng trưng cho trời, sức mạnh, sự khởi đầu lớn."),
    (2, 2): ("Khôn vi Địa", "Thuần Khôn tượng trưng cho đất, nhu thuận, dưỡng nuôi."),
    (1, 2): ("Thủy Thiên Nhu", "Tình thế đang khó khăn, cần nhẫn nại chờ thời."),
    (2, 1): ("Thiên Địa Bĩ", "Bế tắc, không thông. Nên an phận và chờ cơ hội."),
    (63, 63): ("Thủy Hỏa Ký Tế", "Mọi việc đã hoàn thành, nên duy trì và ổn định."),
    (64, 64): ("Hỏa Thủy Vị Tế", "Việc chưa xong, cần kiên trì và tránh hấp tấp."),
    # ... Bạn có thể thêm đủ 64 quẻ ở đây
}

# Hàm chuyển đổi ngày dương sang âm (demo)
def doi_lich_am_duong(ngay):
    return f"Âm lịch tương ứng: {ngay.day}/{ngay.month}/{ngay.year} (chưa tính Can Chi, demo)"

# Lấy tên và ý nghĩa quẻ
def lay_ten_va_y_nghia_que(thuong, ha):
    return ten_que.get((thuong, ha), ("Chưa rõ", "Đang cập nhật..."))

# --- Giao diện Streamlit ---
st.set_page_config(page_title="Gieo Quẻ Kinh Dịch", layout="centered")
st.title("🧧 Gieo Quẻ Kinh Dịch - Mai Hoa Dịch Số")
st.markdown("Chọn ngày để gieo quẻ, xem tên quẻ, ý nghĩa và lưu lịch sử gieo quẻ của bạn.")

# Chọn ngày
selected_date = st.date_input(
    "📅 Chọn ngày gieo quẻ:",
    value=datetime.date.today(),
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date(2100, 12, 31)
)

# Gieo quẻ
if st.button("🔮 Gieo Quẻ"):
    # Seed từ ngày
    random.seed(selected_date.toordinal())

    # Mỗi quẻ đơn có 8 quẻ cơ bản, nên random từ 1–8
    thuong = random.randint(1, 8)
    ha = random.randint(1, 8)

    # Hào động từ 1 đến 6
    hao_dong = random.randint(1, 6)

    # Lấy tên quẻ
    ten, y_nghia = lay_ten_va_y_nghia_que(thuong, ha)

    # Hiển thị kết quả
    st.subheader(f"🧿 Tên Quẻ: {ten}")
    st.markdown(f"**Ý nghĩa:** {y_nghia}")
    st.write(f"🔁 Hào động: **{hao_dong}** – nên chú trọng luận giải hào này.")
    
    st.info(f"📆 Ngày dương lịch: {selected_date}\n\n🗓 {doi_lich_am_duong(selected_date)}")

    # Lưu vào session_state
    if "lich_su" not in st.session_state:
        st.session_state.lich_su = []
    st.session_state.lich_su.append({
        "ngay": str(selected_date),
        "thuong": thuong,
        "ha": ha,
        "ten": ten,
        "hao": hao_dong
    })

# --- Hiển thị lịch sử ---
if "lich_su" in st.session_state:
    st.markdown("## 📜 Lịch sử gieo quẻ")
    for idx, q in enumerate(reversed(st.session_state.lich_su)):
        st.write(f"**Lần {len(st.session_state.lich_su) - idx}:** {q['ngay']} → {q['ten']} (Hào {q['hao']})")
