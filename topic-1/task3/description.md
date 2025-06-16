# Tính Toán Biểu Thức Dạng Chuỗi

Bạn đang cố gắng tính toán một biểu thức dưới dạng chuỗi. Biểu thức bao gồm **2 số tự nhiên** và **1 toán tử** (một trong các toán tử `'+'`, `'-'`, `'*'`).

Ví dụ, nếu biểu thức được cho là `"123+12"` thì kết quả tính toán sẽ là `135`.

Để tính toán biểu thức được tạo bởi chuỗi, chúng ta sẽ xây dựng cấu trúc chương trình đơn giản như sau:

## Cấu Trúc Chương Trình

1. **Tìm vị trí của toán tử** trong biểu thức được cho.  
2. **Chuyển đổi phần chuỗi trước và sau toán tử** thành số.  
3. **Thực hiện phép toán** theo toán tử đã cho.

Bạn cần viết hàm `solution` sao cho nhận vào tham số là biểu thức dạng chuỗi `expression` và trả về kết quả của phép tính.

Hãy tham khảo cấu trúc trên và điền chính xác các hàm `func_a`, `func_b`, `func_c` cùng các tham số vào chỗ trống để chương trình hoạt động đúng.

---

## 🧾 Mô tả Tham Số

- `expression`: là biểu thức dạng chuỗi được truyền vào hàm `solution`.
- `expression` là một biểu thức kết hợp giữa **1 toán tử** và **2 số**.
- Các toán tử có thể là `'+'`, `'-'`, `'*'`.
- Các số là **số tự nhiên từ 1 đến 10.000**.

---

## 🔁 Kết Quả Trả Về

- Trả về kết quả **dưới dạng số**, **không cần** chuyển sang chuỗi.

---

## 📌 Ví Dụ

Biểu thức: `"123+12"`  
Toán tử là `'+'`, số phía trước là `123`, số phía sau là `12`.  
Kết quả phép tính là `123 + 12 = 135`.

---

## 🧪 Kiểm Tra với enumerate (tuỳ chọn)

```python
for x in enumerate('123+12'):
    index, value = x 
    print(index, value, x)
