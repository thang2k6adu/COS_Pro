# 🔢 Bài toán: Tìm vị trí của số `n` được tạo từ các thẻ số

Đã tạo ra một số bằng cách **nối các thẻ bài có ghi số từ 1 đến 9**.  
Nhiệm vụ của bạn là: **Tìm xem số `n` là số nhỏ thứ mấy** trong các số có thể tạo được bằng cách **kết hợp các thẻ bài đã cho**.

---

## 📋 Mô tả

Ví dụ: Với các thẻ số `[1, 2, 1, 3]`, ta có thể tạo ra các số sau (không trùng lặp thứ tự):

[1123, 1132, 1213, 1231, 1312, ..., 3121, 3211]


Nếu `n = 1312` thì đó là **số nhỏ thứ 5** trong danh sách đã sắp xếp theo thứ tự tăng dần.

---

## 📥 Tham số đầu vào

Hàm `solution` nhận vào:

- `card`: danh sách các số nguyên từ 1 đến 9.
- `n`: số nguyên cần kiểm tra vị trí.

### Ràng buộc:

- `card.length <= 9`
- Mỗi phần tử trong `card` là số nguyên trong `[1, 9]`.
- `n` là số tự nhiên ≤ 999,999,999.
- Số chữ số của `n` bằng với độ dài của `card`.
- Mỗi chữ số trong `n` thuộc `[1, 9]`.

---

## 📤 Kết quả đầu ra

- Trả về thứ tự của `n` trong tất cả các số có thể tạo ra từ `card`, **sắp xếp theo thứ tự tăng dần**.
- Nếu **không thể tạo ra `n` từ `card`**, trả về `-1`.

---

## 🧪 Ví dụ

| `card`        | `n`    | Kết quả (`return`) |
|---------------|--------|--------------------|
| `[1, 2, 1, 3]` | `1312` | `5`                |
| `[1, 1, 1, 2]` | `1122` | `-1`               |

---

## 🧠 Giải thích

- **Ví dụ 1**: Các số có thể tạo ra từ `[1, 2, 1, 3]` là:  
  `[1123, 1132, 1213, 1231, 1312, ...]`  
  → `1312` là số nhỏ thứ **5**.

- **Ví dụ 2**: Với `[1, 1, 1, 2]`, các số có thể tạo gồm:  
  `[1112, 1121, 1211, 2111]`  
  → `1122` không thể tạo được (vì không có đủ số 2) → trả về `-1`.

---
