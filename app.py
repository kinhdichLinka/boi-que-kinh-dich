import streamlit as st
import datetime

# --- Danh sách đầy đủ 64 quẻ Kinh Dịch và ý nghĩa sơ lược ---
ten_que = {
    (1, 1): ("Càn vi Thiên", "Thuần Càn - Tượng trưng cho trời, sức mạnh, sự khởi đầu lớn."),
    (2, 2): ("Khôn vi Địa", "Thuần Khôn - Đất, nhu thuận, dưỡng nuôi."),
    (3, 3): ("Thuỷ Lôi Truân", "Gian nan thuở đầu, cần kiên trì vượt khó."),
    (4, 4): ("Sơn Thuỷ Mông", "Tối tăm, hỗn loạn, cần khai sáng và học hỏi."),
    (5, 5): ("Thuỷ Thiên Nhu", "Chờ thời, nhu thuận để vượt khó."),
    (6, 6): ("Thiên Thuỷ Tụng", "Tranh chấp, kiện tụng, nên giữ hoà khí."),
    (7, 7): ("Địa Thuỷ Sư", "Đội ngũ, tổ chức, cần kỷ luật và lãnh đạo."),
    (8, 8): ("Thuỷ Địa Tỷ", "Gắn bó, tương trợ lẫn nhau."),
    (1, 2): ("Phong Thiên Tiểu Súc", "Tiểu nhân cản trở, cần nhẫn nại."),
    (1, 3): ("Thuỷ Thiên Nhu", "Chờ thời, thuận theo tự nhiên."),
    (1, 4): ("Sơn Thiên Đại Súc", "Tích luỹ, chuẩn bị cho hành động lớn."),
    (1, 5): ("Hỏa Thiên Đại Hữu", "Tài sản lớn, thời kỳ phát triển mạnh."),
    (1, 6): ("Thiên Hỏa Đồng Nhân", "Đồng lòng, đoàn kết phát triển."),
    (1, 7): ("Địa Thiên Thái", "Thịnh vượng, thuận lợi mọi mặt."),
    (1, 8): ("Sơn Thiên Đại Súc", "Tích lũy nội lực, chuẩn bị cho phát triển."),
    (2, 1): ("Thiên Trạch Lý", "Sắp xếp, cải cách, giữ lễ nghĩa."),
    (2, 3): ("Thuỷ Địa Tỷ", "Gắn bó, kết nối, hoà hợp với mọi người."),
    (2, 4): ("Sơn Địa Bác", "Suy tàn, kết thúc giai đoạn cũ."),
    (2, 5): ("Hỏa Địa Tấn", "Tiến lên, phát triển rực rỡ."),
    (2, 6): ("Thiên Địa Bĩ", "Bế tắc, khó khăn, nên chờ thời."),
    (2, 7): ("Địa Thiên Thái", "Giao hòa, thịnh vượng."),
    (2, 8): ("Sơn Địa Bác", "Tàn úa, chuyển đổi sang giai đoạn mới."),
    (3, 1): ("Thiên Lôi Vô Vọng", "Không vọng động, tránh hành động vô căn cứ."),
    (3, 2): ("Phong Lôi Ích", "Lợi ích lớn, cần hành động hợp thời."),
    (3, 4): ("Sơn Lôi Di", "Đổi mới, thay đổi đúng lúc."),
    (3, 5): ("Hỏa Lôi Phệ Hạp", "Cương quyết xử lý vấn đề."),
    (3, 6): ("Thiên Lôi Vô Vọng", "Không vọng tưởng, giữ vững đạo lý."),
    (3, 7): ("Địa Lôi Phục", "Trở về, phục hồi, khởi đầu mới."),
    (3, 8): ("Sơn Lôi Di", "Thay đổi, biến chuyển."),
    (4, 1): ("Thiên Sơn Độn", "Rút lui chiến lược, tránh xung đột."),
    (4, 2): ("Phong Sơn Tiệm", "Tiến chậm rãi nhưng chắc chắn."),
    (4, 3): ("Lôi Sơn Tiểu Quá", "Việc nhỏ nên làm, việc lớn nên tránh."),
    (4, 5): ("Hỏa Sơn Lữ", "Lữ hành, tạm thời, không ổn định."),
    (4, 6): ("Lôi Hỏa Phong", "Rực rỡ, thông minh, phát triển mạnh."),
    (4, 7): ("Địa Sơn Khiêm", "Khiêm tốn, giữ mình."),
    (4, 8): ("Sơn Sơn Cấn", "Dừng lại, tĩnh tại, cần xem xét lại."),
    (5, 1): ("Thiên Thuỷ Tụng", "Tranh chấp, cần hoà giải."),
    (5, 2): ("Phong Thuỷ Hoán", "Biến đổi mạnh, cơ hội chuyển mình."),
    (5, 3): ("Thuỷ Lôi Truân", "Gian nan, vượt khó ban đầu."),
    (5, 4): ("Sơn Thuỷ Mông", "Mông muội, cần học hỏi."),
    (5, 6): ("Hỏa Thuỷ Vị Tế", "Chưa xong, cần hoàn thiện."),
    (5, 7): ("Địa Thuỷ Sư", "Tổ chức, kỷ luật."),
    (5, 8): ("Sơn Thuỷ Mông", "Chưa rõ ràng, cần khai sáng."),
    (6, 1): ("Thiên Hỏa Đồng Nhân", "Hợp tác, đồng lòng."),
    (6, 2): ("Phong Hỏa Gia Nhân", "Gia đình, ổn định nội bộ."),
    (6, 3): ("Thuỷ Hỏa Ký Tế", "Hoàn tất, kết thúc tốt đẹp."),
    (6, 4): ("Sơn Hỏa Bí", "Trang sức, vẻ đẹp, ngoài sáng trong tối."),
    (6, 5): ("Hỏa Thiên Đại Hữu", "Đại tài sản, thành công."),
    (6, 7): ("Địa Hỏa Minh Di", "Ẩn mình, chờ thời."),
    (6, 8): ("Sơn Hỏa Bí", "Vẻ ngoài hào nhoáng, bên trong cần suy xét."),
    (7, 1): ("Thiên Địa Bĩ", "Bế tắc, ngưng trệ."),
    (7, 2): ("Phong Địa Quan", "Quan sát, thấu hiểu thời thế."),
    (7, 3): ("Thuỷ Địa Tỷ", "Tương trợ, hoà hợp."),
    (7, 4): ("Sơn Địa Bác", "Kết thúc, chuyển giai đoạn."),
    (7, 5): ("Hỏa Địa Tấn", "Tiến lên, phát triển."),
    (7, 6): ("Thiên Địa Bĩ", "Bất hòa, nghịch cảnh."),
    (7, 8): ("Sơn Địa Bác", "Tàn lụi, kết thúc chu kỳ."),
    (8, 1): ("Thiên Sơn Độn", "Tạm thời rút lui, không hành động."),
    (8, 2): ("Phong Sơn Tiệm", "Tiến từ từ, vững chắc."),
    (8, 3): ("Thuỷ Sơn Kiển", "Nguy hiểm, cần đề phòng."),
    (8, 4): ("Sơn Sơn Cấn", "Tĩnh tại, dừng lại suy xét."),
    (8, 5): ("Hỏa Sơn Lữ", "Du hành, chưa ổn định."),
    (8, 6): ("Thiên Sơn Độn", "Ẩn mình, tránh mạo hiểm."),
    (8, 7): ("Địa Sơn Khiêm", "Giữ thái độ khiêm tốn."),
    (8, 8): ("Sơn Địa Bác", "Tàn lụi, chuyển đổi sang mới.")
}

# --- Hàm chuyển đổi Can Chi từ số ---
can_list = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
chi_list = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

def get_can_chi_index(n):
    can = can_list[n % 10]
    chi = chi_list[n % 12]
    return can, chi, n

# --- Giao diện nhập thông tin ngày giờ sinh âm lịch ---
st.title("🔍 Gieo Quẻ Kinh Dịch theo Mai Hoa Dịch Số")
st.markdown("Nhập thông tin ngày sinh âm lịch để gieo quẻ theo Mai Hoa Dịch Số:")

col1, col2 = st.columns(2)
with col1:
    ngay = st.number_input("Ngày (âm lịch)", min_value=1, max_value=30, value=1)
    thang = st.number_input("Tháng (âm lịch)", min_value=1, max_value=12, value=1)
with col2:
    nam = st.number_input("Năm (âm lịch)", min_value=1000, max_value=2100, value=2024)
    gio_sinh = st.number_input("Giờ sinh (theo canh giờ: 0-11)", min_value=0, max_value=11, value=0, help="Tý = 0, Sửu = 1, ..., Hợi = 11")

if st.button("🔮 Gieo Quẻ"):
    # Tính quẻ theo công thức đã thống nhất:
    thuong = (ngay + thang + nam) % 8
    ha = (gio_sinh + ngay + thang + nam) % 8
    hao_dong = (gio_sinh + ngay + thang + nam) % 6 + 1  # Hào từ 1 đến 6

    # Đảm bảo giá trị từ 1 đến 8 (không có quẻ 0)
    thuong = 8 if thuong == 0 else thuong
    ha = 8 if ha == 0 else ha

    # Lấy tên quẻ và ý nghĩa
    ten, y_nghia = ten_que.get((thuong, ha), ("Chưa rõ", "(Chưa cập nhật ý nghĩa cho quẻ này)"))

    st.subheader(f"🧿 Tên Quẻ: {ten} ({thuong} - {ha})")
    st.markdown(f"**Ý nghĩa sơ lược:** {y_nghia}")
    st.write(f"**Hào động:** Hào {hao_dong}")

    # Lưu lịch sử
    if "lich_su" not in st.session_state:
        st.session_state.lich_su = []
    st.session_state.lich_su.append({
        "ngay": f"{ngay}/{thang}/{nam}",
        "gio": gio_sinh,
        "thuong": thuong,
        "ha": ha,
        "que": ten,
        "hao": hao_dong
    })

# --- Hiển thị lịch sử các lần gieo quẻ ---
if "lich_su" in st.session_state:
    st.markdown("## 📜 Lịch sử các lần gieo quẻ")
    for idx, record in enumerate(reversed(st.session_state.lich_su)):
        st.write(f"**Lần {len(st.session_state.lich_su)-idx}:** {record['ngay']} giờ {record['gio']} → {record['que']} (Hào {record['hao']})")
