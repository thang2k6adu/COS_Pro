# 📘 Mô tả bài toán: Số Kaprekar

**Số Kaprekar** là những số thỏa mãn điều kiện sau:

- Bình phương của chính nó được chia thành hai phần sao cho **tổng của hai phần đó bằng chính số ban đầu**.  
- **Lưu ý**: Cả hai phần sau khi chia đều phải là **số dương**.

### 🧮 Ví dụ:
Số \( 55^2 = 3,025 \).  
Ta có thể chia 3,025 thành:
- 3 và 025  
- 30 và 25  
- 302 và 5  

Trong các cách chia trên, **30 + 25 = 55**, nên **55 là một số Kaprekar**.

---

## ▣ Tham số đầu vào

- Một số tự nhiên `k` được truyền vào làm tham số của hàm `solution`.  
- `k` là một số tự nhiên **từ 50 đến 100,000** (bao gồm cả 50 và 100,000).

---

## ▣ Giá trị trả về

- Trả về **một danh sách các số Kaprekar nhỏ hơn hoặc bằng `k`**, được **sắp xếp theo thứ tự tăng dần**.  
- Nếu không có số nào, trả về danh sách rỗng `[]`.

> ⚠️ Có ít hơn **100 số Kaprekar** nhỏ hơn hoặc bằng 100,000.

---

## ▣ Yêu cầu đặc biệt

Một đoạn mã đã được viết để giải quyết bài toán, **nhưng có một dòng sai** khiến chương trình không hoạt động chính xác.  
👉 **Bạn cần tìm và sửa đúng một dòng duy nhất** để chương trình hoạt động chính xác cho mọi đầu vào.

---

## ▣ Ví dụ

| k   | return                     |
|-----|----------------------------|
| 500 | [9, 45, 55, 99, 297]       |

---

## ▣ Giải thích ví dụ

- \( 9 \times 9 = 81 \) → \( 8 + 1 = 9 \)  
- \( 45 \times 45 = 2,025 \) → \( 20 + 25 = 45 \)  
- \( 55 \times 55 = 3,025 \) → \( 30 + 25 = 55 \)  
- \( 99 \times 99 = 9,801 \) → \( 98 + 01 = 99 \)  
- \( 297 \times 297 = 88,209 \) → \( 88 + 209 = 297 \)
