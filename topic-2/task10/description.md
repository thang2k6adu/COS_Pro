# 🔢 Rút gọn các số 0 liên tiếp trong chuỗi

## 📖 Mô tả

Ta có một chuỗi chỉ gồm các ký tự `'0'` và `'1'`.  
Mục tiêu là **rút gọn các nhóm số 0 liên tiếp thành một số 0 duy nhất**.

> Ví dụ, chuỗi `"101100011100"` sẽ được rút gọn thành `"101101110"`.

---

## 📥 Tham số

- `s`: Chuỗi chỉ chứa các ký tự `'0'` và `'1'`, được truyền vào làm tham số.
- Độ dài của `s` là từ **1 đến 1,000 ký tự**.

---

## 📤 Kết quả trả về

- Trả về **chuỗi mới** sau khi đã rút gọn các nhóm `'0'` liên tiếp thành một `'0'`.
- Các ký tự `'1'` được giữ nguyên, không bị thay đổi.

---

## 📘 Ví dụ

| s              | return      |
|----------------|-------------|
| "101100011100" | "101101110" |

### 🧾 Giải thích:

- Trong chuỗi `"101100011100"`:
  - Nhóm `"00"` → rút gọn thành `"0"`
  - Nhóm `"000"` → rút gọn thành `"0"`

➡️ Kết quả sau khi rút gọn là `"101101110"`

---

## 🛠️ Yêu cầu

Bạn đã có sẵn một đoạn mã Python để thực hiện yêu cầu trên. Tuy nhiên, đoạn mã đó có **một dòng bị sai**, khiến chương trình không hoạt động đúng với một số đầu vào.

> 🎯 **Nhiệm vụ của bạn là sửa đúng một dòng duy nhất** để đảm bảo chương trình hoạt động chính xác với mọi chuỗi đầu vào.

