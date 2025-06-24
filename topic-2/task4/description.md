# 🔢 Bài toán: Đếm số bộ ba có tổng là bội số của K

## 📌 Mô tả

Bạn có một danh sách các **số tự nhiên không trùng lặp**.  
Bạn muốn đếm xem có **bao nhiêu cách chọn ba số khác nhau** từ danh sách đó sao cho **tổng của chúng là bội số của K**.

---

## 🎯 Mục tiêu

Viết hàm `solution(arr, K)` nhận vào:

- `arr`: danh sách số tự nhiên
- `K`: một số nguyên dương

Trả về **số lượng cách chọn ba số khác nhau** sao cho **tổng của chúng chia hết cho K**.

---

## 📥 Tham số đầu vào

- `arr`: danh sách các số tự nhiên.
  - Điều kiện: `3 <= len(arr) <= 100`
  - Mỗi phần tử: `1 <= arr[i] <= 1000`
  - Không có phần tử trùng nhau
- `K`: một số nguyên dương từ `1` đến `10`

---

## 📤 Giá trị trả về

- Trả về **số cách chọn ba số khác nhau** sao cho tổng của chúng là **bội số của K**.
- Nếu không có cách nào thỏa điều kiện → trả về `0`.

---

## 📘 Ví dụ

| `arr`             | `K` | `return` |
|-------------------|-----|----------|
| `[1, 2, 3, 4, 5]` | `3` | `4`      |

---

### 🧠 Giải thích

Có 4 cách chọn bộ ba sao cho tổng là bội của 3:

1. `1 + 2 + 3 = 6`
2. `1 + 3 + 5 = 9`
3. `2 + 3 + 4 = 9`
4. `3 + 4 + 5 = 12`

→ Tất cả đều chia hết cho 3  
→ Tổng cộng **4 cách hợp lệ**.

---
