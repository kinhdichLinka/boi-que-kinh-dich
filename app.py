import streamlit as st
from datetime import datetime
import convertdate

# Danh sách Can và Chi
CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
QUE = ["Càn", "Đoài", "Ly", "Chấn", "Tốn", "Khảm", "Cấn", "Khôn"]
LUAN_GIAI = {
    "Càn": "Quẻ Càn là quẻ của Trời, tượng trưng cho sức mạnh, sự khởi đầu và thành công.",
    "Đoài": "Quẻ Đoài tượng trưng cho vui vẻ, duyên dáng, có phần mềm mỏng và lôi cuốn.",
    "Ly": "Quẻ Ly đại diện cho lửa, ánh sáng, sự hiểu biết, danh tiếng và văn minh.",
    "Chấn": "Quẻ Chấn biểu thị sự chuyển động, thay đổi, sức mạnh bùng nổ.",
    "Tốn": "Quẻ Tốn là gió, linh hoạt, mềm dẻo, đại diện cho sự thuyết phục và thích nghi.",
    "Khảm": "Quẻ Khảm là nước, tượng trưng cho nguy hiểm, chiều sâu và trí tuệ.",
    "Cấn": "Quẻ Cấn là núi, đại diện cho tĩnh lặng, suy ngẫm, chậm rãi nhưng vững chắc.",
    "Khôn": "Quẻ Khôn là Đất, khiêm nhường, tiếp nhận, hỗ trợ và nuôi dưỡng."
}

def convert_to_lunar(date):
    """Chuyển đổi ngày dương sang âm lịch"""
    return convertdate.lunar.from_gregorian(date.year, date.month, date.day)

def get_can_chi_nam(year):
    can = CAN[year % 10]
    chi = CHI[year % 12]
    return f"{can} {chi}"

def get_que_index(*args, modulo):
    total = sum(args)
    return total % modulo

def tra_que(datetime_input):
    gio = datetime_input.hour
    ngay = datetime_input.day
    thang = datetime_input.month
    nam = datetime_input.year

    # Lấy chi số từ Can Chi năm
    chi_nam_index = nam % 12  # ví dụ: Giáp Thìn → Thìn = 4
    can_nam_index = nam % 10

    que_thuong = get_que_index(ngay + thang + can_nam_index + chi_nam_index, modulo=8)
    que_ha = get_que_index(gio + ngay + thang + nam, modulo=8)
    que_dong = get_que_index(gio + ngay + thang + nam, modulo=6)

    ten_que_thuong = QUE[que_thuong]
    ten_que_ha = QUE[que_ha]
    ten_quai = f"{ten_que_thuong} vi {ten_que_ha}"

    y_nghia = LUAN_GIAI.get(ten_que_thuong, "Chưa có luận giải.")

    return {
        "Thượng quái": ten_que_thuong,
        "Hạ quái": ten_que_ha,
        "Quẻ động": que_dong + 1,
        "Tên quẻ": ten_quai,
        "Luận giải": y_nghia
    }

# Giao diện Streamlit
st.title("🧿 Bói Quẻ Kinh Dịch - Mai Hoa Dịch Số")
st.markdown("Hệ thống lập quẻ theo ngày giờ, chuyển âm lịch, xác định tên quẻ và luận giải ý nghĩa.")

input_date = st.date_input("📅 Chọn ngày (dương lịch):", value=datetime.today())
input_time = st.time_input("🕓 Chọn giờ:", value=datetime.now().time())

if st.button("📜 Gieo quẻ"):
    input_datetime = datetime.combine(input_date, input_time)
    result = tra_que(input_datetime)
    lunar = convert_to_lunar(input_datetime)

    st.subheader("📌 Kết quả:")
    st.write(f"🌕 Âm lịch: Ngày {lunar[2]}, Tháng {lunar[1]}, Năm {get_can_chi_nam(input_date.year)}")
    st.write(f"🔮 Thượng quái: **{result['Thượng quái']}**")
    st.write(f"🔮 Hạ quái: **{result['Hạ quái']}**")
    st.write(f"📍 Hào động: **Hào số {result['Quẻ động']}**")
    st.write(f"🪐 Tên quẻ: **{result['Tên quẻ']}**")
    st.markdown(f"📝 **Luận giải:** {result['Luận giải']}")
