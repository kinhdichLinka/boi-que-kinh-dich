import streamlit as st
from datetime import datetime
import calendar
import chinese_calendar
from convertdate import chinese

st.set_page_config(page_title="Mai Hoa Dịch Số", layout="centered")

st.title("🔮 Bói Quẻ Kinh Dịch - Mai Hoa Dịch Số")
st.markdown("Tính quẻ theo ngày giờ, phương pháp Mai Hoa Dịch Số. Chuyển đổi âm lịch, kết luận tên quẻ và diễn giải.")

# Danh sách 8 quẻ cơ bản
bagua = ["Càn", "Đoài", "Ly", "Chấn", "Tốn", "Khảm", "Cấn", "Khôn"]

# Danh sách 64 quẻ (chỉ demo vài cái, bạn có thể mở rộng)
que_dich = {
    (0, 0): ("Càn vi Càn", "Thuần dương, tượng trưng cho sáng tạo, kiên định, tiến lên. Quẻ tốt."),
    (7, 7): ("Khôn vi Khôn", "Thuần âm, tượng trưng cho nhu thuận, nâng đỡ, dưỡng sinh. Quẻ tốt."),
    (6, 1): ("Cấn Đoài", "Tượng trưng cho cản trở, đụng độ nhưng có cơ hội chuyển hóa."),
    (1, 6): ("Đoài Cấn", "Niềm vui và sự vững chắc kết hợp. Có thể mang lại may mắn."),
    # ... Thêm các tổ hợp quẻ khác nếu muốn
}

# Nhập dữ liệu
col1, col2 = st.columns(2)
with col1:
    ngay_gio = st.date_input("📅 Chọn ngày gieo quẻ", value=datetime.today())
with col2:
    gio = st.time_input("🕓 Chọn giờ gieo quẻ", value=datetime.now().time())

# Chuyển sang Âm lịch
def convert_to_lunar(dt: datetime):
    lunar = chinese.from_gregorian(dt.year, dt.month, dt.day)
    return {
        "year": lunar[0],
        "month": lunar[1],
        "day": lunar[2],
        "leap": lunar[3],
    }

# Quy đổi Can Chi sang số
can_chi_gia_tri = {
    "Giáp": 1, "Ất": 2, "Bính": 3, "Đinh": 4, "Mậu": 5,
    "Kỷ": 6, "Canh": 7, "Tân": 8, "Nhâm": 9, "Quý": 10,
    "Tý": 1, "Sửu": 2, "Dần": 3, "Mão": 4, "Thìn": 5, "Tỵ": 6,
    "Ngọ": 7, "Mùi": 8, "Thân": 9, "Dậu": 10, "Tuất": 11, "Hợi": 12,
}

# Tính toán giá trị Can Chi đơn giản (chỉ chi, demo)
def get_chi_number(year):
    chi = (year - 4) % 12 + 1  # Tý = 1
    return chi

# Tính quẻ
def tinh_que(gio, ngay, thang, nam):
    # Quy đổi giờ sang số can chi (Tý=1, Sửu=2, ...)
    gio_gia_tri = int((gio.hour + 1) // 2) + 1
    if gio_gia_tri > 12:
        gio_gia_tri -= 12

    # Dùng Chi (đơn giản) để tính
    chi_ngay = ngay
    chi_thang = thang
    chi_nam = get_chi_number(nam)

    que_thuong = (chi_ngay + chi_thang + chi_nam) % 8
    que_ha = (gio_gia_tri + chi_ngay + chi_thang + chi_nam) % 8
    que_dong = (gio_gia_tri + chi_ngay + chi_thang + chi_nam) % 6 + 1

    return que_thuong, que_ha, que_dong

# Bấm nút xem quẻ
if st.button("🌠 Xem quẻ"):
    dt = datetime.combine(ngay_gio, gio)
    am_lich = convert_to_lunar(dt)
    st.markdown(f"**Âm lịch:** {am_lich['day']:02d}/{am_lich['month']:02d}/{am_lich['year']} {'(Nhuận)' if am_lich['leap'] else ''}")

    q_thuong, q_ha, q_dong = tinh_que(gio, am_lich['day'], am_lich['month'], am_lich['year'])

    ten_que_thuong = bagua[q_thuong]
    ten_que_ha = bagua[q_ha]
    ten_que = que_dich.get((q_thuong, q_ha), (f"{ten_que_thuong} {ten_que_ha}", "Chưa có diễn giải."))

    st.subheader(f"🔮 Quẻ Chủ: {ten_que[0]}")
    st.markdown(f"**Ý nghĩa:** {ten_que[1]}")
    st.markdown(f"**Hào động:** Vị trí **hào {q_dong}** (đếm từ dưới lên)")

    st.info("Đây là kết quả tính toán theo phương pháp Mai Hoa Dịch Số, có thể mở rộng diễn giải, chi tiết quẻ biến trong bản nâng cấp.")

