nhập môn toán
a =  int ( đầu vào ( " Nhap he so a ---> " ))
b =  int ( đầu vào ( " Nhap he so b ---> " ))
c =  int ( đầu vào ( " Nhap he so c ---> " ))
đồng bằng = b ^ 2  -  4 * a * c
nếu đồng bằng <  0 :
    in ( " Phương trinh vo nghiem " )
đồng bằng elif ==  0 :
    x =  - b / 2 * a
    in ( " Phương trinh co nghiem kep " , x)
khác :
    x1 = ( - b + math.sqrt (delta)) /  2  * a
    x2 = ( - b - math.sqrt (delta)) /  2  * a
    in ( " Phương trinh co 2 nghiem phan biet " )
    in (x1)
    in (x2)
