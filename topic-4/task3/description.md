# 🎿 Bài toán: Tính chi phí tối thiểu sử dụng khu trượt tuyết trong `n` ngày

Bạn cần tính **chi phí tối thiểu** để sử dụng khu trượt tuyết **liên tiếp đúng `n` ngày**. Dưới đây là các loại vé được bán tại khu trượt tuyết:

| Loại vé      | Số ngày sử dụng tại khu trượt tuyết             | Giá                |
|--------------|--------------------------------------------------|--------------------|
| one_day      | Dùng được trong **1 ngày** kể từ ngày mua       | `one_day_price`    |
| multi_day    | Dùng được trong **`multi_day` ngày** liên tiếp  | `multi_day_price`  |

Ví dụ, nếu:

- `one_day_price = 3`
- `multi_day = 5`
- `multi_day_price = 14`

thì:
- Vé 1 ngày có giá 3 đơn vị tiền.
- Vé 5 ngày có giá 14 đơn vị tiền.

Giả sử `n = 6`, bạn cần sử dụng khu trượt tuyết **chính xác 6 ngày liên tiếp**, thì chi phí được tính như sau:

- 6 vé 1 ngày → `6 × 3 = 18`
- 1 vé 5 ngày + 1 vé 1 ngày → `14 + 3 = 17`

✅ Do đó, chi phí tối thiểu để dùng trượt tuyết đúng 6 ngày liên tiếp là **17**.

> **Lưu ý:** Bạn **không được** mua 2 vé 5 ngày (tổng cộng 10 ngày), vì bạn chỉ cần **chính xác** `n = 6` ngày.

---

## 📥 Tham số đầu vào

Hàm `solution` nhận vào 4 tham số theo thứ tự sau:

- `one_day_price`: Số nguyên biểu thị giá của vé 1 ngày (1 ≤ giá ≤ 1000).
- `multi_day`: Số ngày mà vé nhiều ngày có hiệu lực (3 ≤ multi_day ≤ 5).
- `multi_day_price`: Số nguyên biểu thị giá của vé nhiều ngày (1 ≤ giá ≤ 1000).
- `n`: Số ngày cần sử dụng khu trượt tuyết một cách **chính xác** (1 ≤ n ≤ 10¹²).

---

## 📤 Giá trị trả về

Trả về một số nguyên: **chi phí tối thiểu** để sử dụng khu trượt tuyết trong đúng `n` ngày liên tiếp.

---

## 🧪 Ví dụ

| one_day_price | multi_day | multi_day_price | n  | Kết quả |
|---------------|-----------|------------------|----|----------|
| 3             | 5         | 14               | 6  | 17       |
| 2             | 3         | 5                | 11 | 19       |

---

## 📖 Giải thích ví dụ

### Ví dụ 1:
- 1 vé 5 ngày + 1 vé 1 ngày → `14 + 3 = 17`
- Nếu mua 6 vé 1 ngày → `6 × 3 = 18` (không tối ưu)

👉 Chi phí tối thiểu là **17**

---

### Ví dụ 2:
- Mua 3 vé 3 ngày = 9 ngày
- Thêm 2 vé 1 ngày = 2 ngày  
→ Tổng cộng đúng 11 ngày

- Chi phí: `3 × 5 + 2 × 2 = 15 + 4 = 19`

👉 Chi phí tối thiểu là **19**
