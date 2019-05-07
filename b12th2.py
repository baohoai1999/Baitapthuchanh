nhập khẩu lại
giá trị = []
các mặt hàng = [x cho x trong  đầu vào ( "Lời nói : " ) .split ( ' , ' )]
# #############
cho p trong các mục:
    nếu  len (p) < 6  hoặc  len (p) > 12 :
        tiếp tục
    khác :
        vượt qua
    nếu  không re.search ( " [az] " , p):
       tiếp tục
    elif  không re.search ( " [0-9] " , p):
       tiếp tục
    elif  không re.search ( " [AZ] " , p):
       tiếp tục
    elif  không re.search ( " [$ # @] " , p):
       tiếp tục
    elif re.search ( " \ s " , p):
       tiếp tục
    khác :
       vượt qua
    value.append (p)
in ( " , " .join (giá trị))
