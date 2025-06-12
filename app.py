import streamlit as st
import datetime
import random

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

# Hàm chuyển đổi ngày dương sang âm (sơ lược)
def doi_lich_am_duong(ngay):
    return f"Âm lịch tương ứng: {ngay.day}/{ngay.month}/{ngay.year} (demo)"

# Hàm lấy tên và ý nghĩa quẻ
def lay_ten_va_y_nghia_que(thuong, ha):
    return ten_que.get((thuong, ha), ("Chưa rõ", "Đang cập nhật..."))

# --- Giao diện Streamlit ---
st.title("🧧 Gieo Quẻ Kinh Dịch - Mai Hoa Dịch Số")

st.markdown("""
Bạn hãy chọn ngày và giờ sinh để xem quẻ dịch, tên quẻ, ý nghĩa và lưu lại lịch sử cá nhân.
""")

selected_date = st.date_input(
    "📅 Chọn ngày muốn gieo quẻ:",
    value=datetime.date.today(),
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date(2100, 12, 31)
)

gio_sinh = st.selectbox(
    "🕰 Chọn giờ sinh (theo 12 giờ địa chi):",
    [
        "Tý (23h – 1h)",
        "Sửu (1h – 3h)",
        "Dần (3h – 5h)",
        "Mão (5h – 7h)",
        "Thìn (7h – 9h)",
        "Tỵ (9h – 11h)",
        "Ngọ (11h – 13h)",
        "Mùi (13h – 15h)",
        "Thân (15h – 17h)",
        "Dậu (17h – 19h)",
        "Tuất (19h – 21h)",
        "Hợi (21h – 23h)"
    ]
)

if st.button("🔮 Gieo Quẻ"):
    # Chuyển giờ sinh thành số đại diện để thêm vào seed
    gio_index = [
        "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", 
        "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"
    ].index(gio_sinh.split()[0])

    # Tạo seed dựa trên ngày và giờ sinh để đảm bảo tính nhất quán
    seed_value = selected_date.toordinal() * 100 + gio_index
    random.seed(seed_value)

    thuong = random.randint(1, 64)
    ha = random.randint(1, 64)
    ten, y_nghia = lay_ten_va_y_nghia_que(thuong, ha)

    st.subheader(f"🧿 Tên Quẻ: {ten}")
    st.markdown(f"**Ý nghĩa:** {y_nghia}")

    st.info(f"Ngày dương lịch: {selected_date}\n\n{doi_lich_am_duong(selected_date)}\n\nGiờ sinh đã chọn: {gio_sinh}")

    # Gợi ý hào động đơn giản
    hao_dong = random.randint(1, 6)
    st.write(f"Hào động: {hao_dong} (hào {hao_dong} động, cần xem kỹ hào này trong sách dịch để hiểu rõ tình thế)")

    # Lưu lịch sử gieo quẻ trong session
    if "lich_su" not in st.session_state:
        st.session_state.lich_su = []
    st.session_state.lich_su.append({
        "ngay": str(selected_date),
        "gio": gio_sinh,
        "que": ten,
        "hao": hao_dong
    })

# --- Hiển thị lịch sử gieo quẻ ---
if "lich_su" in st.session_state:
    st.markdown("## 📜 Lịch sử các lần gieo quẻ")
    for idx, record in enumerate(reversed(st.session_state.lich_su)):
        st.write(f"**Lần {len(st.session_state.lich_su)-idx}:** {record['ngay']} {record['gio']} → {record['que']
