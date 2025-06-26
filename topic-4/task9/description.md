# 🕒 Tính góc giữa kim giờ và kim phút trên đồng hồ kim

Bạn cần tính góc giữa kim giờ và kim phút của một chiếc đồng hồ kim tại thời điểm `hour` giờ `minute` phút.  
Ví dụ, lúc 3 giờ 00 phút, kim giờ và kim phút tạo thành một góc 90˚.

Hãy viết hàm `solution` sao cho khi được truyền vào thời điểm `hour` giờ và `minute` phút làm tham số, hàm sẽ trả về **góc giữa kim giờ và kim phút** tại thời điểm đó dưới dạng **chuỗi có 1 chữ số thập phân**.

---

## ▣ Mô tả tham số:

- `hour` và `minute` là hai tham số của hàm `solution`.
- `hour` là số nguyên từ 1 đến 12.
- `minute` là số nguyên từ 0 đến 59.

---

## ▣ Mô tả giá trị trả về:

Hàm phải trả về góc giữa kim giờ và kim phút tại thời điểm `hour` giờ `minute` phút, với định dạng là chuỗi số có 1 chữ số sau dấu phẩy (thập phân).

---

## ▣ Ví dụ:

| hour | minute | return |
|------|--------|--------|
| 3    | 0      | "90.0" |

---

## ▣ Giải thích ví dụ:

- Tại thời điểm 3:00, kim giờ chỉ hướng 90 độ, kim phút ở 0 độ → tạo thành góc 90.0˚.
