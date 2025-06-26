# 📚 Tìm Chuỗi Palindrome Thứ k Theo Thứ Tự Từ Điển

## 🧾 Đề bài

Chuỗi mà khi **đảo ngược trước sau vẫn giống y hệt ban đầu** được gọi là **chuỗi Palindrome** (chuỗi đối xứng).  
Ví dụ: `"aba"` là một chuỗi Palindrome, còn `"abccca"` **không phải** là Palindrome.

Trong một chuỗi bất kỳ, có thể có **nhiều chuỗi con** là Palindrome.  
Trong số các chuỗi Palindrome đó, bạn cần tìm **chuỗi Palindrome lớn thứ k theo thứ tự từ điển (alphabet)**.  
"Chuỗi lớn thứ k" nghĩa là: sắp xếp **tất cả các chuỗi con Palindrome** theo **thứ tự từ điển**, rồi lấy chuỗi ở vị trí thứ k.

Để làm điều đó, chương trình được xây dựng theo cấu trúc sau:

1. Khởi tạo danh sách `palindromes` để lưu các chuỗi Palindrome.
2. Duyệt qua **tất cả các chuỗi con** của chuỗi ban đầu và thực hiện:
   - 2-1. Kiểm tra xem chuỗi con đó có phải là Palindrome hay không. Nếu phải, kiểm tra xem nó **đã có trong danh sách** `palindromes` hay chưa.
   - 2-2. Nếu chưa có, thì thêm chuỗi đó vào danh sách.
3. Sắp xếp danh sách `palindromes` theo **thứ tự từ điển** (alphabetical order).
4. Nếu độ dài danh sách **nhỏ hơn k**, trả về `"NULL"`.
5. Ngược lại, trả về phần tử ở vị trí thứ `k - 1` trong danh sách.

---

## 🎯 Nhiệm vụ

Viết hàm `solution` sao cho:

- Nhận vào một chuỗi `s` và một số nguyên `k`.
- Trả về **chuỗi Palindrome lớn thứ k theo thứ tự từ điển** (tính từ 1).
- Nếu không có đủ `k` chuỗi Palindrome, trả về `"NULL"`.

Bạn cần hoàn thành hàm bằng cách điền chính xác vào các hàm còn trống như `func_a`, `func_b`, `func_c` và tham số tương ứng để đảm bảo chương trình hoạt động đúng.

---

## 📥 Mô tả tham số

- Tham số truyền vào là chuỗi `s` và số nguyên `k`.
- `s`: độ dài từ 1 đến 100, chỉ gồm **chữ cái thường**.
- `k`: số nguyên dương nhỏ hơn hoặc bằng 200.

---

## 📤 Mô tả giá trị trả về

- Trả về **chuỗi Palindrome thứ k theo thứ tự từ điển**.
- Nếu số lượng chuỗi Palindrome ít hơn `k`, trả về `"NULL"`.

---

## 📊 Ví dụ

| s        | k | return  |
|----------|---|---------|
| "abcba"  | 4 | "bcb"   |
| "ccddcc" | 7 | "NULL"  |

---

### 📌 Giải thích:

- **Ví dụ #1:**  
  Các chuỗi con Palindrome của `"abcba"`:  
  `"a"`, `"abcba"`, `"b"`, `"bcb"`, `"c"`  
  → Sắp xếp từ điển: `"a"`, `"abcba"`, `"b"`, `"bcb"`, `"c"`  
  → Vị trí thứ 4: `"bcb"`

- **Ví dụ #2:**  
  Các chuỗi Palindrome của `"ccddcc"`:  
  `"c"`, `"cc"`, `"ccddcc"`, `"cddc"`, `"d"`, `"dd"`  
  → Tổng cộng 6 chuỗi → không có chuỗi thứ 7 → trả về `"NULL"`
