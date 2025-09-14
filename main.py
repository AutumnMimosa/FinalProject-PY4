import streamlit as st
#Đặt config page
st.set_page_config(page_title= "Vương quốc mô hình", page_icon = ":sparkles:")

#Tạo thanh bên
with st.sidebar:
  st.title("Vương quốc mô hình")
  st.header('CHào mừng bạn đến Vương quốc mô hình!')
  st.image('shop.jpg')
  st.write('Chúng tôi tự hào là nơi cung cấp, phân phối các mô hình chất lượng, đa dạng mẫu mã, cam kết làm hài lòng các khách hàng chuyên nghiệp. Hãy đến và khám phá thế giới mô hình tại Vương quốc mô hình!')
  st.write(':house: Địa chỉ: 123 Đường ABC, Phường XYZ, Quận DEF, TP. Hồ Chí Minh')
  st.write(':phone: Điện thoại: 0123 456 789')
  
#Tạo trang chính
st.title('Vương quốc mô hình')
 #Tạo các cột và hình ảnh sản phẩm
col1, col2, col3 = st.columns(3)
with col1:
  b1 = st.button('Dragon Ball')
with col2:
  b2 = st.button('Naruto')
with col3:
  b3 = st.button('One Piece')
if b1:
  st.header('Danh sách mô hình Dragon Ball')
  col4, col5, col6 = st.columns(3)
  with col4:
    st.image('dragonball1.jpg')
    st.write('Mô hình Dragon Ball - Mã số: 001')
  with col5:
    st.image('dragonball2.jpg')
    st.write('Mô hình Dragon Ball - Mã số: 002')
  with col6:
    st.image('dragonball3.jpg')
    st.write('Mô hình Dragon Ball - Mã số: 003')

if b2:
  st.header('Danh sách mô hình Naruto')
  col4, col5, col6 = st.columns(3)
  with col4:
    st.image('naruto1.jpg')
    st.write('Mô hình Naruto - Mã số: 001')
  with col5:
    st.image('naruto2.jpg')
    st.write('Mô hình Naruto - Mã số: 002')
  with col6:
    st.image('naruto3.jpg')
    st.write('Mô hình Naruto - Mã số: 003')
if b3:
  st.header('Danh sách mô hình One Piece')
  col4, col5, col6 = st.columns(3)
  with col4:
    st.image('onepiece1.jpg')
    st.write('Mô hình One Piece - Mã số: 001')
  with col5:
    st.image('onepiece2.jpg')
    st.write('Mô hình One Piece - Mã số: 002')
  with col5:
    st.image('onepiece3.jpg')
    st.write('Mô hình One Piece - Mã số: 003')

#Giao diện đặt hàng
st.header('Đặt hàng')
#Lấy thông tin khách hàng và hóa đơn
with st.form('Đơn đặt hàng'):
  topics = ('Dragon Ball', 'Naruto', 'One Piece')
  option_topic = st.selectbox('Chọn chủ đề', topics)
  codes = ('001', '002', '003')
  option_code = st.selectbox('Chọn mã số', codes)
  nums = st.slider('Số lượng bạn muốn đặt:',0,10,0)
  name = st.text_input('Họ và tên:')
  phone = st.text_input('Số điện thoại nhà riêng:')
  address = st.text_input('Địa chỉ giao hàng:')
  bill = {'Loại mô hình': option_topic, 'Mã số': option_code, 'Số lượng': nums, 'Họ và tên khách hàng': name, 'Số điện thoại liên hệ': phone, 'Địa chỉ giao hàng': address}
  submitted = st.form_submit_button('Xác nhận')
  if submitted:
    st.header('Bạn đã chọn:')
    for x,y in bill.items():
      st.write(x,y)
#In hóa đơn
print_bill = st.checkbox('In hóa đơn')
if print_bill:
  ans = ''
  for x in bill:
    ans += str(x) + ': ' + str(bill[x]) + '\n'
    st.download_button('In hóa đơn', ans)
