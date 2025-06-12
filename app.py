import streamlit as st
import datetime
import json

# --- Danh sách đầy đủ 64 quẻ Kinh Dịch và ý nghĩa sơ lược ---
ten_que = {
    (1, 1): ("Càn vi Thiên", "Trời mạnh mẽ, tượng trưng cho sự sáng tạo."),
    (1, 2): ("Thiên Địa Bĩ", "Thời kỳ bế tắc, cần kiên nhẫn."),
    (1, 3): ("Thiên Lôi Vô Vọng", "Không nên kỳ vọng xa vời."),
    (1, 4): ("Thiên Sơn Độn", "Nên lui bước, tránh đối đầu."),
    (1, 5): ("Thiên Thủy Tụng", "Tranh chấp, cần hòa giải."),
    (1, 6): ("Thiên Hỏa Đồng Nhân", "Hợp tác và đoàn kết."),
    (1, 7): ("Thiên Trạch Lý", "Tự sửa mình, cải cách."),
    (1, 8): ("Thiên Phong Cấu", "Gặp gỡ cơ duyên tốt."),
    (2, 1): ("Địa Thiên Thái", "Thịnh vượng, hòa hợp."),
    (2, 2): ("Khôn vi Địa", "Đất mềm, nhu thuận."),
    (2, 3): ("Địa Lôi Phục", "Trở lại, tái sinh."),
    (2, 4): ("Địa Sơn Khiêm", "Khiêm nhường, thuận lợi."),
    (2, 5): ("Địa Thủy Sư", "Lãnh đạo tập thể."),
    (2, 6): ("Địa Hỏa Minh Di", "Ánh sáng bị che lấp."),
    (2, 7): ("Địa Trạch Lâm", "Tiến lên, mở rộng."),
    (2, 8): ("Địa Phong Thăng", "Thăng tiến, tăng trưởng."),
    (3, 1): ("Lôi Thiên Đại Tráng", "Mạnh mẽ, phát triển."),
    (3, 2): ("Lôi Địa Dự", "Hân hoan, vui vẻ."),
    (3, 3): ("Thuỷ Lôi Truân", "Gian nan khởi đầu."),
    (3, 4): ("Sơn Lôi Di", "Chuyển dịch, thay đổi."),
    (3, 5): ("Thuỷ Lôi Giải", "Giải thoát, tháo gỡ."),
    (3, 6): ("Hỏa Lôi Phệ Hạp", "Cứng rắn, kiên định."),
    (3, 7): ("Trạch Lôi Tùy", "Thuận theo hoàn cảnh."),
    (3, 8): ("Phong Lôi Ích", "Lợi ích đến từ hành động."),
    (4, 1): ("Sơn Thiên Đại Súc", "Kiềm chế để phát triển."),
    (4, 2): ("Sơn Địa Bác", "Tan rã, kết thúc chu kỳ."),
    (4, 3): ("Sơn Lôi Di", "Di chuyển, cần linh hoạt."),
    (4, 4): ("Sơn vi Cấn", "Dừng lại, tĩnh tại."),
    (4, 5): ("Sơn Thủy Mông", "U mê, cần khai sáng."),
    (4, 6): ("Sơn Hỏa Bí", "Trang trí, đẹp đẽ."),
    (4, 7): ("Sơn Trạch Tổn", "Tổn thất để được lâu dài."),
    (4, 8): ("Sơn Phong Cổ", "Lỗi lầm xưa, cần sửa."),
    (5, 1): ("Thuỷ Thiên Nhu", "Chờ đợi thời cơ."),
    (5, 2): ("Thuỷ Địa Tỷ", "Gắn bó, tương trợ."),
    (5, 3): ("Thuỷ Lôi Giải", "Giải thoát khó khăn."),
    (5, 4): ("Thuỷ Sơn Kiển", "Vượt chướng ngại."),
    (5, 5): ("Thuỷ vi Khảm", "Hiểm nguy, cần cẩn trọng."),
    (5, 6): ("Thuỷ Hỏa Ký Tế", "Hoàn tất, kết quả tốt."),
    (5, 7): ("Thuỷ Trạch Tiết", "Tiết chế, giới hạn."),
    (5, 8): ("Thuỷ Phong Tỉnh", "Giếng nước – tài nguyên."),
    (6, 1): ("Hỏa Thiên Đại Hữu", "Có của cải, giàu có."),
    (6, 2): ("Hỏa Địa Tấn", "Tiến lên, phát triển."),
    (6, 3): ("Hỏa Lôi Phệ Hạp", "Cắn răng vượt khó."),
    (6, 4): ("Hỏa Sơn Lữ", "Du hành, cô đơn."),
    (6, 5): ("Hỏa Thuỷ Vị Tế", "Chưa hoàn tất."),
    (6, 6): ("Hỏa vi Ly", "Sáng suốt, phân biệt."),
    (6, 7): ("Hỏa Trạch Khuê", "Khác biệt, bất đồng."),
    (6, 8): ("Hỏa Phong Đỉnh", "Bình ổn, vững chắc."),
    (7, 1): ("Trạch Thiên Quải", "Quyết đoán, dứt khoát."),
    (7, 2): ("Trạch Địa Tụy", "Tùy tùng, dễ bị ảnh hưởng."),
    (7, 3): ("Trạch Lôi Tùy", "Thuận theo tự nhiên."),
    (7, 4): ("Trạch Sơn Hàm", "Gắn kết, vui vẻ."),
    (7, 5): ("Trạch Thuỷ Khốn", "Khó khăn, thử thách."),
    (7, 6): ("Trạch Hỏa Cách", "Cách mạng, thay đổi."),
    (7, 7): ("Trạch vi Đoài", "Vui vẻ, duyên dáng."),
    (7, 8): ("Trạch Phong Đại Quá", "Vượt quá mức, nguy hiểm."),
    (8, 1): ("Phong Thiên Tiểu Súc", "Tích lũy nhỏ, chờ thời."),
    (8, 2): ("Phong Địa Quan", "Quan sát, suy xét."),
    (8, 3): ("Phong Lôi Ích", "Lợi ích, thịnh vượng."),
    (8, 4): ("Phong Sơn Tiệm", "Tiến dần, ổn định."),
    (8, 5): ("Phong Thủy Hoán", "Biến đổi, đổi mới."),
    (8, 6): ("Phong Hỏa Gia Nhân", "Gia đình, nội bộ."),
    (8, 7): ("Phong Trạch Trung Phu", "Thành thật, trung thực."),
    (8, 8): ("Phong vi Tốn", "Khiêm tốn, nhu thuận."),
}

# --- Danh sách giờ sinh Can Chi ---
gio_sinh_labels = [
    "Tý (23h-01h)", "Sửu (01h-03h)", "Dần (03h-05h)", "Mão (05h-07h)",
    "Thìn (07h-09h)", "Tỵ (09h-11h)", "Ngọ (11h-13h)", "Mùi (13h-15h)",
    "Thân (15h-17h)", "Dậu (17h-19h)", "Tuất (19h-21h)", "Hợi (21h-23h)"
]

st.title("🔍 Gieo Quẻ Kinh Dịch theo Mai Hoa Dịch Số")
st.markdown("Nhập thông tin **ngày sinh âm lịch** để gieo quẻ theo Mai Hoa Dịch Số:")

col1, col2 = st.columns(2)
with col1:
    ngay = st.number_input("Ngày (âm lịch)", min_value=1, max_value=30, value=1)
    thang = st.number_input("Tháng (âm lịch)", min_value=1, max_value=12, value=1)
with col2:
    nam = st.number_input("Năm (âm lịch)", min_value=1000, max_value=2100, value=2024)
    gio_sinh = st.selectbox("Giờ sinh (theo 12 Can Chi)", options=list(range(12)), format_func=lambda x: gio_sinh_labels[x])

if st.button("🔮 Gieo Quẻ"):
    thuong = (ngay + thang + nam) % 8
    ha = (gio_sinh + ngay + thang + nam) % 8
    hao_dong = (gio_sinh + ngay + thang + nam) % 6 + 1

    thuong = 8 if thuong == 0 else thuong
    ha = 8 if ha == 0 else ha

    ten, y_nghia = ten_que.get((thuong, ha), (f"Quẻ {thuong}-{ha}", "(Chưa cập nhật ý nghĩa cho quẻ này)"))

    ten_que_thuong = next((v[0] for k, v in ten_que.items() if k[0] == thuong and k[1] == thuong), f"Quẻ {thuong}")
    ten_que_ha = next((v[0] for k, v in ten_que.items() if k[1] == ha and k[0] == ha), f"Quẻ {ha}")

    st.subheader(f"🧿 Kết quả gieo quẻ")
    st.markdown(f"- **Quẻ Thượng (số {thuong})** → {ten_que_thuong}")
    st.markdown(f"- **Quẻ Hạ (số {ha})** → {ten_que_ha}")
    st.markdown(f"- **Hào động:** Hào {hao_dong}")
    st.markdown(f"### 🔮 **Quẻ Chủ: {ten}**")
    st.markdown(f"{y_nghia}")

    if "lich_su" not in st.session_state:
        st.session_state.lich_su = []
    st.session_state.lich_su.append({
        "ngay": f"{ngay}/{thang}/{nam}",
        "gio": gio_sinh_labels[gio_sinh],
        "thuong": thuong,
        "ha": ha,
        "que": ten,
        "hao": hao_dong
    })

if "lich_su" in st.session_state:
    st.markdown("## 📜 Lịch sử các lần gieo quẻ")
    for idx, record in enumerate(reversed(st.session_state.lich_su)):
        st.write(f"**Lần {len(st.session_state.lich_su)-idx}:** {record['ngay']} giờ {record['gio']} → {record['que']} (Hào {record['hao']})")

    st.download_button(
        label="📄 Tải xuống lịch sử quẻ (JSON)",
        data=json.dumps(st.session_state.lich_su, indent=2, ensure_ascii=False),
        file_name="lich_su_que.json",
        mime="application/json"
    )
