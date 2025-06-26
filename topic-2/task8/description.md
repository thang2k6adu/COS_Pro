# 📘 Tạo danh sách mới theo quy tắc xen kẽ đầu-cuối

## 📝 Mô tả

Khi một danh sách chứa các số tự nhiên được cho trước, ta muốn tạo ra một danh sách mới theo các quy tắc sau:

1. Thêm phần tử **đầu tiên** của danh sách ban đầu vào vị trí **đầu tiên** của danh sách mới.  
2. Thêm phần tử **cuối cùng** của danh sách ban đầu vào vị trí **thứ hai** của danh sách mới.  
3. Tiếp tục, luân phiên lấy phần tử **đầu tiên còn lại** và **cuối cùng còn lại** trong danh sách ban đầu, rồi thêm chúng vào danh sách mới theo thứ tự.  
4. Lặp lại quá trình trên **cho đến khi không còn phần tử nào** trong danh sách ban đầu.

Bạn được cung cấp một danh sách `arr` chứa các số tự nhiên làm tham số đầu vào.  
Hãy thực hiện quá trình trên để tạo ra danh sách mới và trả về kết quả từ hàm `solution`.

> ❗ Tuy nhiên, đoạn mã đã viết sẵn có **một dòng sai**, khiến một số trường hợp đầu vào không hoạt động đúng.  
> Bạn cần **sửa đúng một dòng duy nhất** để đoạn mã hoạt động chính xác với mọi trường hợp.

---

## 📥 Tham số

- `arr` là một danh sách chứa các số tự nhiên.
- `1 ≤ len(arr) ≤ 1,000`
- Mỗi phần tử trong `arr` là một số tự nhiên từ `1` đến `10,000`.

---

## 📤 Giá trị trả về

- Trả về danh sách mới được tạo ra theo quy tắc mô tả ở trên.

---

## 📘 Ví dụ

| arr                | return             |
|--------------------|--------------------|
| [1, 2, 3, 4, 5, 6] | [1, 6, 2, 5, 3, 4] |

### 🧾 Giải thích:

Quá trình tạo danh sách mới từ `[1, 2, 3, 4, 5, 6]`:

| arr còn lại        | Danh sách mới       |
|--------------------|---------------------|
| [1, 2, 3, 4, 5, 6] | []                  |
| [2, 3, 4, 5, 6]    | [1]                 |
| [2, 3, 4, 5]       | [1, 6]              |
| [3, 4, 5]          | [1, 6, 2]           |
| [3, 4]             | [1, 6, 2, 5]        |
| [4]                | [1, 6, 2, 5, 3]     |
| []                 | [1, 6, 2, 5, 3, 4]  |

---

## ✅ Mục tiêu

Hoàn thành hoặc sửa lại đúng **một dòng duy nhất** trong hàm `solution` sao cho mọi đầu vào đều được xử lý đúng theo quy tắc trên.
