# 📈 Bài toán lợi nhuận từ giao dịch cổ phiếu

---

## 📝 Mô tả

Giả sử bạn có một danh sách chứa giá cổ phiếu trong `n` ngày liên tiếp.  
Bạn cần tìm **lợi nhuận tối đa** có thể đạt được theo các quy tắc sau:

- Bạn chỉ được **mua cổ phiếu một lần duy nhất** trong suốt `n` ngày.
- Bạn chỉ được **bán cổ phiếu một lần duy nhất**.
- **Không được bán cổ phiếu vào đúng ngày đã mua**, tức là phải **sau ít nhất 1 ngày** mới được bán.
- Bạn **phải** thực hiện **ít nhất một lần mua** và **một lần bán**.
- Bạn chỉ có thể bán nếu đã từng mua trước đó.
- Lợi nhuận tối đa có thể **âm, bằng 0, hoặc dương**.

---

## 🔧 Yêu cầu

Viết hàm `solution(prices)` nhận vào một danh sách `prices`, là giá cổ phiếu trong `n` ngày liên tiếp, và trả về **lợi nhuận tối đa có thể đạt được** nếu tuân thủ đúng các quy tắc trên.

Tuy nhiên, đoạn code đang bị **sai một dòng**, hãy tìm và **chỉ sửa một dòng duy nhất** để đảm bảo code chạy đúng với mọi đầu vào.

---

## 📥 Tham số

- `prices`: Danh sách giá cổ phiếu trong `n` ngày liên tiếp.
  - `2 ≤ len(prices) ≤ 1,000,000`
  - Mỗi phần tử `prices[i]` là số nguyên từ `1` đến `1,000`

---

## 📤 Giá trị trả về

- Trả về một số nguyên là **lợi nhuận tối đa** có thể đạt được sau một lần mua và một lần bán (tuân theo quy tắc).

---

## 📌 Ví dụ

### Ví dụ 1:
- `prices = [1, 2, 3]`
- Mua vào ngày đầu (giá 1), bán vào ngày thứ ba (giá 3)
- Lợi nhuận: `3 - 1 = 2` → **Tối đa**

### Ví dụ 2:
- `prices = [3, 1]`
- Phải mua vào ngày đầu (giá 3), và bắt buộc phải bán vào ngày thứ hai (giá 1)
- Lợi nhuận: `1 - 3 = -2` → **Lỗ**

---