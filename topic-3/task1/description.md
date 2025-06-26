# 🧪 Kiểm tra khả năng xoay danh sách

## 📝 Đề bài

Khi cho hai danh sách `arrA` và `arrB` gồm các số nguyên, bạn cần kiểm tra xem có thể **xoay arrA** để tạo thành `arrB` hay không.  
Ở đây, **xoay danh sách** có nghĩa là **dịch toàn bộ phần tử sang phải một vị trí**, và **phần tử cuối cùng sẽ được đưa lên đầu danh sách**.

Ví dụ minh họa:  
Nếu `arrA = [1, 2, 3, 4]`, sau một lần xoay sẽ thành `[4, 1, 2, 3]`. Xoay tiếp lần nữa sẽ thành `[3, 4, 1, 2]`.

---

## ⚙️ Cấu trúc chương trình

1. Nếu độ dài của `arrA` và `arrB` khác nhau, trả về `false`.
2. Nếu thành phần (giá trị) của hai danh sách khác nhau, thì cho dù xoay thế nào cũng không thể giống nhau → trả về `false`.
3. Nối `arrA` với chính nó để tạo thành danh sách có độ dài gấp đôi.
4. Kiểm tra xem `arrB` có phải là một đoạn con của danh sách đã nối hay không:
   - Nếu có → trả về `true`
   - Nếu không → trả về `false`

---

## 🎯 Yêu cầu

Viết hàm `solution` sao cho:

- Khi được truyền vào `arrA` và `arrB`,
- Nếu có thể xoay `arrA` để được `arrB` → trả về `true`,
- Ngược lại → trả về `false`.

Bạn cần **điền chính xác các chỗ trống** trong hàm với các hàm `func_a`, `func_b`, `func_c` và các tham số phù hợp, để chương trình hoạt động đúng như mô tả trên.

---

## 📥 Mô tả tham số

- Hai danh sách `arrA` và `arrB` được truyền vào làm tham số của hàm `solution`.
- Độ dài của `arrA` và `arrB` nằm trong khoảng từ **1 đến 1,000**.
- Mỗi phần tử trong `arrA` và `arrB` là số nguyên từ **0 đến 1,000**.

---

## 📤 Mô tả giá trị trả về

- Trả về `true` nếu có thể xoay `arrA` để tạo thành `arrB`.
- Trả về `false` nếu không thể.

---

## 📊 Ví dụ

| arrA         | arrB          | return |
|--------------|---------------|--------|
| [1, 2, 3, 4] | [3, 4, 1, 2]  | true   |
| [1, 2, 3, 4] | [1, 4, 2, 3]  | false  |

### 🧾 Giải thích:

- **Ví dụ #1**: Nếu xoay `arrA` sang phải 2 lần, ta sẽ được `arrB`.
- **Ví dụ #2**: Không thể xoay `arrA` thành `arrB` theo bất kỳ cách nào.
