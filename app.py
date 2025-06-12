import streamlit as st

def get_can_chi_value(can, chi):
    can_dict = {'Giáp':1,'Ất':2,'Bính':3,'Đinh':4,'Mậu':5,'Kỷ':6,'Canh':7,'Tân':8,'Nhâm':9,'Quý':10}
    chi_dict = {'Tý':1,'Sửu':2,'Dần':3,'Mão':4,'Thìn':5,'Tỵ':6,'Ngọ':7,'Mùi':8,'Thân':9,'Dậu':10,'Tuất':11,'Hợi':12}
    return can_dict[can] + chi_dict[chi]

def lap_que(can_day, chi_day, can_month, chi_month, can_year, chi_year, can_hour, chi_hour):
    s_day = get_can_chi_value(can_day, chi_day)
    s_month = get_can_chi_value(can_month, chi_month)
    s_year = get_can_chi_value(can_year, chi_year)
    s_hour = get_can_chi_value(can_hour, chi_hour)
    q_thuong = (s_day + s_month + s_year) % 8 or 8
    q_ha = (s_hour + s_day + s_month + s_year) % 8 or 8
    hao_dong = (s_hour + s_day + s_month + s_year) % 6 or 6
    return q_thuong, q_ha, hao_dong

st.title("🔮 Quẻ Kinh Dịch – Bói theo Can Chi")
cols = st.columns(2)
with cols[0]:
    can_day = st.selectbox("Can của ngày", list(['Giáp','Ất','Bính','Đinh','Mậu','Kỷ','Canh','Tân','Nhâm','Quý']))
    chi_day = st.selectbox("Chi của ngày", list(['Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi','Thân','Dậu','Tuất','Hợi']))
    can_month = st.selectbox("Can của tháng", list(['Giáp','Ất','Bính','Đinh','Mậu','Kỷ','Canh','Tân','Nhâm','Quý']))
    chi_month = st.selectbox("Chi của tháng", list(['Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi','Thân','Dậu','Tuất','Hợi']))
with cols[1]:
    can_year = st.selectbox("Can của năm", list(['Giáp','Ất','Bính','Đinh','Mậu','Kỷ','Canh','Tân','Nhâm','Quý']))
    chi_year = st.selectbox("Chi của năm", list(['Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi','Thân','Dậu','Tuất','Hợi']))
    can_hour = st.selectbox("Can của giờ", list(['Giáp','Ất','Bính','Đinh','Mậu','Kỷ','Canh','Tân','Nhâm','Quý']))
    chi_hour = st.selectbox("Chi của giờ", list(['Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi','Thân','Dậu','Tuất','Hợi']))

if st.button("Lập Quẻ"):
    q_t, q_h, hao = lap_que(can_day, chi_day, can_month, chi_month, can_year, chi_year, can_hour, chi_hour)
    st.success(f"Quẻ Thượng: {q_t}")
    st.success(f"Quẻ Hạ: {q_h}")
    st.success(f"Hào động: Hào {hao}")
