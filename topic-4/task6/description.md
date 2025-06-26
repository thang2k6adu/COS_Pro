# 💠 Bài toán: Tìm các số tự luyến (số Narcissistic) có đúng `k` chữ số

Khi một chữ số **k** được cho trước, nếu **tổng các chữ số của một số**, mỗi chữ số được **lũy thừa lên k**, **bằng chính số đó**, thì số đó được gọi là **số tự luyến** (hay còn gọi là **số Narcissistic**, **số Armstrong**).

Ví dụ: **153** là một **số tự luyến có 3 chữ số**, vì:

153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153


---

## 📥 Tham số đầu vào

- `k`: một số nguyên tự nhiên, được truyền vào dưới dạng tham số của hàm `solution`.
- Điều kiện: `k` nằm trong khoảng từ **3 đến 6**.

---

## 📤 Giá trị trả về

Hàm `solution(k)` cần:

- Trả về **một danh sách** chứa tất cả các **số tự luyến có đúng `k` chữ số**,
- Danh sách này phải được **sắp xếp theo thứ tự tăng dần**.

---

## 🧪 Ví dụ

| k | Kết quả trả về             |
|---|----------------------------|
| 3 | `[153, 370, 371, 407]`     |

---

## 📖 Giải thích ví dụ

- `153` = 1³ + 5³ + 3³ = 1 + 125 + 27 = **153**
- `370` = 3³ + 7³ + 0³ = 27 + 343 + 0 = **370**
- `371` = 3³ + 7³ + 1³ = 27 + 343 + 1 = **371**
- `407` = 4³ + 0³ + 7³ = 64 + 0 + 343 = **407**

Tất cả các số trên đều có đúng **3 chữ số** và thỏa mãn điều kiện của **số tự luyến**.

---

## 🧩 Gợi ý cài đặt

Để tìm các số tự luyến `k` chữ số, bạn có thể:

- Duyệt tất cả các số từ `10^(k-1)` đến `10^k - 1`,
- Tính tổng lũy thừa `k` của từng chữ số,
- So sánh tổng này với chính số đó để quyết định có phải số tự luyến không.
