import streamlit as st
import datetime

# ==== Danh sách Can và Chi ====
CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
QUE = [
    "Càn", "Đoài", "Ly", "Chấn", "Tốn", "Khảm", "Cấn", "Khôn"
]

# ==== Hàm tính Can Chi của năm (theo âm lịch Trung Hoa) ====
def get_can_chi_nam(nam):
    can = CAN[(nam + 6) % 10]
    chi = CHI[(nam + 8) % 12]
    return f"{can} {chi}", (CAN.index(can), CHI.index(chi))

# ==== Giao diện chọn ngày ====
st.title("🧙 Bói Quẻ Kinh Dịch - Mai Hoa Dịch Số")
selected_date = st.date_input(
    "📅 Chọn ngày muốn gieo quẻ:",
    value=datetime.date.today(),
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date(2100, 12, 31)
)

# ==== Giao diện chọn giờ ====
gio_list = [
    "Tý (23h-1h)", "Sửu (1h-3h)", "Dần (3h-5h)", "Mão (5h-7h)",
    "Thìn (7h-9h)", "Tỵ (9h-11h)", "Ngọ (11h-13h)", "Mùi (13h-15h)",
    "Thân (15h-17h)", "Dậu (17h-19h)", "Tuất (19h-21h)", "Hợi (21h-23h)"
]
gio_chi = [g.split()[0] for g in gio_list]
gio_chon = st.selectbox("🕒 Chọn giờ sinh / giờ gieo quẻ:", gio_list)
gio_index = gio_list.index(gio_chon)

# ==== Tính toán các chỉ số ====
ngay = selected_date.day
thang = selected_date.month
nam = selected_date.year

# Can Chi năm
can_chi_nam_text, (can_index, chi_index) = get_can_chi_nam(nam)

# Quẻ hạ = (Giờ + Ngày + Tháng + Năm) % 8
que_ha = (gio_index + ngay + thang + nam) % 8
# Quẻ thượng = (Can_năm + Tháng + Ngày) % 8
que_thuong = (can_index + thang + ngay) % 8
# Hào động = (Giờ + Ngày + Tháng + Năm) % 6 + 1
hao_dong = (gio_index + ngay + thang + nam) % 6 + 1

# ==== Kết luận và hiển thị ====
st.markdown("## 📜 Kết Quả Bói Quẻ")
st.write(f"🌙 Ngày âm lịch (tính Can Chi năm): **{can_chi_nam_text}**")
st.write(f"🔮 Quẻ Thượng: **{QUE[que_thuong]}**")
st.write(f"🔮 Quẻ Hạ: **{QUE[que_ha]}**")
st.write(f"📌 Hào Động: **Hào số {hao_dong}**")
st.success(f"✨ Quẻ: **{QUE[que_thuong]} trên {QUE[que_ha]}**, Hào động: {hao_dong}")

# Gợi ý tên quẻ (chưa đầy đủ danh sách 64 quẻ)
TEN_QUE_64 = {
    ("Càn", "Càn"): "Thuần Càn",
    ("Khôn", "Khôn"): "Thuần Khôn",
    ("Ly", "Càn"): "Hỏa Thiên Đại Hữu",
    ("Cấn", "Khảm"): "Sơn Thủy Mông",
    # Có thể bổ sung dần thêm tên quẻ ở đây...
}
ten_que = TEN_QUE_64.get((QUE[que_thuong], QUE[que_ha]), "Đang cập nhật...")

st.markdown(f"### 🧾 Tên quẻ: **{ten_que}**")
if ten_que != "Đang cập nhật...":
    st.info(f"👉 Đang tra ý nghĩa quẻ **{ten_que}**, sẽ cập nhật sớm.")

