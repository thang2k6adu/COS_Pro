# ♟️ Bài toán: Số ô an toàn không bị quân Hậu chặn (Bishop trên bàn cờ vua)

## 🧾 Đề bài

Trong cờ vua, **quân Hậu (Bishop)** có thể **di chuyển theo đường chéo** không giới hạn số ô trong một lần đi, như hình minh họa bên dưới.  
Nếu có một quân cờ nào đó nằm trên đường di chuyển này, quân Hậu có thể **ăn** quân cờ đó trong một lần đi.

> ![image.png]  
> *Hình ảnh minh họa cách di chuyển của quân Hậu (Bishop)*

Trên bàn cờ vua có kích thước **8 x 8**, có một số quân Hậu đã được đặt sẵn.  
Bạn cần **tính số ô trống mà một quân cờ mới có thể được đặt vào mà không bị bất kỳ quân Hậu nào ăn trong một lần di chuyển**.

Trong hình minh họa, các ô có hình tròn là các ô **bị quân Hậu kiểm soát** (có thể bị ăn trong một lần).  
Vì vậy, số ô an toàn mà bạn có thể đặt một quân cờ mới vào là **50 ô**.

---

## 🎯 Yêu cầu

Viết hàm `solution` sao cho:

- Nhận vào một danh sách `bishops` chứa các vị trí đã đặt quân Hậu trên bàn cờ (kí hiệu dạng `"A1"`, `"D5"`,...),
- Trả về số ô trống trên bàn cờ **không bị bất kỳ quân Hậu nào kiểm soát**.

---

## 📥 Thông tin đầu vào

- `bishops`: danh sách các vị trí đã đặt quân Hậu, mỗi vị trí là một chuỗi.
- Độ dài của `bishops`: từ **1 đến 64**.
- Mỗi vị trí là một chuỗi gồm:
  - Một chữ cái in hoa từ `A` đến `H` biểu thị **cột** (theo chiều ngang),
  - Một chữ số từ `1` đến `8` biểu thị **hàng** (theo chiều dọc).
- Không có vị trí nào bị lặp hoặc không hợp lệ.

---

## 📤 Kết quả trả về

- Trả về **số ô trống** có thể đặt quân cờ mới mà **không bị bất kỳ quân Hậu nào ăn trong một nước đi**.

---

## 📊 Ví dụ

| bishops              | return |
|----------------------|--------|
| `["D5"]`             | `50`   |
| `["D5", "E8", "G2"]` | `42`   |
