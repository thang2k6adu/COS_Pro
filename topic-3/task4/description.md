# 📌 Bài toán: Nối hai chuỗi với phần trùng lặp

## 🧾 Mô tả

Bạn muốn nối hai chuỗi `s1` và `s2` lại để tạo thành một chuỗi mới.  
Khi đó, **nếu phần cuối của một chuỗi trùng với phần đầu của chuỗi còn lại**, phần trùng nhau **chỉ được viết một lần duy nhất**.

### 🧩 Ví dụ:
Nếu `s1 = "ababc"` và `s2 = "abcdab"`, khi nối `s1` vào trước `s2`, bạn có thể nhận được chuỗi mới có độ dài **9** như sau:

> *(Hình minh họa)*

Tuy nhiên, nếu bạn nối `s2` vào trước `s1`, bạn có thể nhận được chuỗi mới với độ dài **8**, tức là ngắn hơn:

> *(Hình minh họa)*

---

## 🎯 Yêu cầu

Cho hai chuỗi `s1` và `s2`, hãy hoàn thành hàm `solution(s1, s2)` để **trả về độ dài ngắn nhất** có thể có của chuỗi mới sau khi nối `s1` và `s2` (hoặc ngược lại), **với phần trùng lặp chỉ được tính một lần**.

---

## 📥 Ràng buộc

- Hai chuỗi `s1` và `s2` được truyền vào làm tham số.
- `1 ≤ độ dài của s1, s2 ≤ 100`
- `s1` và `s2` chỉ bao gồm **chữ cái thường** từ bảng chữ cái tiếng Anh (`a`–`z`).

---

## 📊 Ví dụ

| s1      | s2       | return |
|---------|----------|--------|
| "ababc" | "abcdab" | 8      |

---

## 📌 Giải thích ví dụ:

- Khi nối `"ababc"` + `"abcdab"` → phần `"ab"` trùng → độ dài chuỗi mới: 9.
- Khi nối `"abcdab"` + `"ababc"` → phần `"ab"` trùng → độ dài chuỗi mới: **8**.
- Kết quả cuối cùng là **8**, vì đây là chuỗi ngắn nhất có thể tạo ra.
