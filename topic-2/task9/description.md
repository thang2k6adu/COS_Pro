# 🔐 Kiểm tra mật khẩu có an toàn không

## 📖 Mô tả

Ta cần kiểm tra xem một mật khẩu được đưa vào có **an toàn** hay không.  
Tiêu chí đánh giá sự an toàn của mật khẩu như sau:

> ❗ **Không được sử dụng 3 ký tự liên tiếp trở lên** là **chữ cái hoặc chữ số** theo thứ tự **tăng dần** hoặc **giảm dần**.  
> (Ví dụ như `abc`, `cba`, `012`, `987` là **không hợp lệ**.)

---

## 📥 Tham số

- `password`: Chuỗi sẽ được dùng làm mật khẩu.
- Chứa **chỉ chữ cái thường (`a-z`) và chữ số (`0-9`)**
- Độ dài của `password` nằm trong khoảng **từ 5 đến 20 ký tự**

---

## 📤 Kết quả trả về

- Trả về `true` nếu chuỗi **không vi phạm** quy tắc (mật khẩu **an toàn**)
- Trả về `false` nếu chuỗi **vi phạm** quy tắc (mật khẩu **không an toàn**)

---

## 📘 Ví dụ

| password    | return |
|-------------|--------|
| "cospro890" | true   |
| "cba323"    | false  |

### 🧾 Giải thích:

- `"cospro890"` không chứa chuỗi 3 ký tự tăng/giảm liên tiếp → ✅ an toàn
- `"cba323"` chứa `"cba"` là 3 ký tự chữ cái **giảm dần liên tiếp** → ❌ không an toàn

---

## 🛠️ Yêu cầu

Bạn đã có một đoạn mã kiểm tra điều kiện trên, tuy nhiên nó **chưa chính xác**.  
Hãy **sửa đúng một dòng duy nhất** trong đoạn mã để đảm bảo hoạt động chính xác với mọi đầu vào.
