import streamlit as st
import datetime
import random

# --- Danh sách 64 quẻ Kinh Dịch và ý nghĩa demo ---
ten_que = {
    (1, 1): ("Càn vi Thiên", "Thuần Càn: trời, mạnh mẽ, khởi đầu tốt."),
    (2, 2): ("Khôn vi Địa", "Thuần Khôn: đất, nhu thuận, nuôi dưỡng."),
    (1, 2): ("Thủy Thiên Nhu", "Khó khăn, nên kiên nhẫn chờ thời."),
    (2, 1): ("Thiên Địa Bĩ", "Bế tắc, nên an phận chờ cơ hội."),
    # ...(bổ sung thêm 64 quẻ nếu cần)
}

# Chuyển ngày dương sang lịch âm (demo)
def doi_lich_am_duong(ngay):
    return f"Âm lịch tương ứng: {ngay.day}/{ngay.month}/{ngay.year} (demo)"

# Lấy tên và ý nghĩa quẻ
def lay_ten_va_y_nghia_que(thuong, ha):
    return ten_que.get((thuong, ha), ("Chưa rõ", "Đang cập nhật..."))

# --- Giao diện Streamlit ---
st.title("🧧 Gieo Quẻ Kinh Dịch - Mai Hoa Dịch Số")

st.markdown("Chọn ngày và giờ sinh để gieo quẻ theo công thức cá nhân hóa.")

selected_date = st.date_input(
    "Chọn ngày sinh:",
    value=datetime.date.today(),
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date(2100, 12, 31)
)

# Giờ sinh theo 12 địa chi
gio_chi = [
    "Tý (23h-1h)", "Sửu (1h-3h)", "Dần (3h-5h)", "Mão (5h-7h)",
    "Thìn (7h-9h)", "Tỵ (9h-11h)", "Ngọ (11h-13h)", "Mùi (13h-15h)",
    "Thân (15h-17h)", "Dậu (17h-19h)", "Tuất (19h-21h)", "Hợi (21h-23h)"
]

selected_gio = st.selectbox("Chọn giờ sinh (12 địa chi):", gio_chi)

if st.button("🔮 Gieo Quẻ"):
    # Gieo quẻ theo ngày và giờ sinh
    seed_input = selected_date.toordinal() + gio_chi.index(selected_gio) * 100
    random.seed(seed_input)
    thuong = random.randint(1, 64)
    ha = random.randint(1, 64)
    ten, y_nghia = lay_ten_va_y_nghia_que(thuong, ha)

    st.subheader(f"🧿 Tên Quẻ: {ten}")
    st.markdown(f"**Ý nghĩa:** {y_nghia}")
    st.info(f"Ngày dương lịch: {selected_date}\n{doi_lich_am_duong(selected_date)}\nGiờ sinh: {selected_gio}")

    # Gợi ý hào động
    hao_dong = random.randint(1, 6)
    st.write(f"Hào động: {hao_dong} (xem kỹ hào này để hiểu tình thế)")

    # Lưu lịch sử gieo quẻ
    if "lich_su" not in st.session_state:
        st.session_state.lich_su = []
    st.session_state.lich_su.append({
        "ngay": str(selected_date),
        "gio": selected_gio,
        "que": ten,
        "hao": hao_dong
    })

# Hiển thị lịch sử
if "lich_su" in st.session_state:
    st.markdown("## 📜 Lịch sử các lần gieo quẻ")
    for idx, record in enumerate(reversed(st.session_state.lich_su)):
        st.write(
            f"**Lần {len(st.session_state.lich_su)-idx}:** {record['ngay']} {record['gio']} → {record['que']} (Hào {record['hao']})"
        )
