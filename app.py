import streamlit as st
import datetime
from convertdate import chinese

# --- Thiết lập danh sách Can Chi và Quẻ Dịch ---
thien_can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
dia_chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
quenames = [
    "Càn", "Đoài", "Ly", "Chấn", "Tốn", "Khảm", "Cấn", "Khôn"
]

# --- Hàm tính chỉ số Can và Chi ---
def get_can_chi(year, month, day):
    can_nam = thien_can[(year + 6) % 10]
    chi_nam = dia_chi[(year + 8) % 12]

    # Ước lượng can chi ngày (chính xác cần dùng lịch ngày giờ cổ)
    total_days = (datetime.date(year, month, day) - datetime.date(1900, 1, 1)).days
    can_ngay = thien_can[(total_days + 10) % 10]
    chi_ngay = dia_chi[(total_days + 12) % 12]

    return can_nam + " " + chi_nam, can_ngay + " " + chi_ngay

# --- Hàm chuyển Can Chi thành số ---
def chi_to_number(chi: str):
    if chi in dia_chi:
        return dia_chi.index(chi) + 1
    return 0

# --- Hàm lập quẻ theo công thức riêng ---
def lap_que(gio, ngay, thang, nam):
    # Quẻ hạ
    que_ha_index = (gio + ngay + thang + nam) % 8
    que_ha = quenames[que_ha_index]

    # Quẻ thượng
    que_thuong_index = (ngay + thang + nam) % 8
    que_thuong = quenames[que_thuong_index]

    # Hào động
    hao_dong = (gio + ngay + thang + nam) % 6 + 1

    ten_que = f"{que_thuong} trên {que_ha}"
    return que_thuong, que_ha, hao_dong, ten_que

# --- Giao diện Streamlit ---
st.title("🧿 Bói Quẻ Kinh Dịch - Mai Hoa Dịch Số")
selected_date = st.date_input(
    "Chọn ngày muốn gieo quẻ:",
    value=datetime.date.today(),
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date(2100, 12, 31)
)

gio = st.number_input("Nhập giờ (0–23):", min_value=0, max_value=23, value=12)

# Chuyển sang âm lịch
year, month, day = selected_date.year, selected_date.month, selected_date.day
am_nam, am_thang, am_ngay, is_leap = chinese.from_gregorian(year, month, day)

# Tính Can Chi
can_chi_nam, can_chi_ngay = get_can_chi(year, month, day)

# Lập quẻ
que_thuong, que_ha, hao_dong, ten_que = lap_que(gio, am_ngay, am_thang, chi_to_number(can_chi_nam.split()[1]))

# --- Hiển thị kết quả ---
st.subheader("📆 Ngày đã chọn:")
st.write(f"Dương lịch: {day}/{month}/{year}")
st.write(f"Âm lịch: {am_ngay}/{am_thang}/{am_nam} {'(tháng nhuận)' if is_leap else ''}")
st.write(f"Can Chi năm: {can_chi_nam}")
st.write(f"Can Chi ngày: {can_chi_ngay}")

st.subheader("📜 Kết quả gieo quẻ:")
st.write(f"Quẻ: **{ten_que}**, Hào động: **Hào số {hao_dong}**")

# --- Luận giải cơ bản ---
st.subheader("📖 Luận giải ý nghĩa:")
luan_giai = {
    "Càn trên Càn": "Thuần Càn - Đại cát, tượng trưng cho sự sáng tạo, vươn lên, thành công toàn diện.",
    "Khôn trên Khôn": "Thuần Khôn - Thuận theo tự nhiên, vững chắc, nền tảng bền lâu.",
    # Bạn có thể thêm nhiều quẻ ở đây
}

st.info(luan_giai.get(ten_que, "Đây là quẻ ít gặp hoặc chưa có trong kho luận giải."))
