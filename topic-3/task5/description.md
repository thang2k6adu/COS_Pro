# 📱 Bài toán: Mô phỏng ứng dụng bảng điện tử chạy chữ

## 🧾 Mô tả

Có một ứng dụng bảng điện tử hiển thị dòng chữ trên màn hình điện thoại.  
Câu chữ được đặt là `"happy-birthday"`.  
Ứng dụng bảng điện tử hiển thị dòng chữ theo **quy tắc sau**:

1. Ứng dụng hiển thị **14 ký tự** trên màn hình.
2. Mỗi giây, **câu chữ di chuyển sang trái một ký tự**.
3. Những phần ngoài câu chữ được hiển thị bằng dấu `"_"`.
4. Khi hiển thị xong toàn bộ câu chữ, ứng dụng **lặp lại câu chữ từ đầu**.
5. Tức là khi câu chữ đã trôi hết qua màn hình, nó sẽ **xuất hiện lại từ đầu**, tiếp tục di chuyển theo quy tắc.

---

### 📌 Ví dụ:

- Ban đầu (0 giây): `"______________"`  
- Sau 3 giây: `"___________hap"`  
- Sau 14 giây: `"happy-birthday"`  
- Sau 20 giây: `"birthday______"`  
- Sau 28 giây: `"______________"`  
- Sau 29 giây: `"_____________h"`  

Ứng dụng sẽ **liên tục lặp lại** câu chữ như trên.

---

## 🎯 Yêu cầu

Viết hàm `solution(phrases, second)` để trả về **chuỗi hiển thị trên màn hình tại thời điểm `second` giây**.  
Trong đó:
- Ký tự `"_"` được xem như là một **khoảng trắng**.

---

## 📥 Thông tin đầu vào

- `phrases`: Chuỗi câu chữ, luôn là `"happy-birthday"`.
- `second`: Số giây đã trôi qua (1 ≤ second ≤ 10,000), là một **số tự nhiên**.

---

## 📤 Kết quả trả về

Hàm `solution` cần trả về **chuỗi 14 ký tự** đang được hiển thị trên màn hình tại thời điểm `second`.

---

## 📊 Ví dụ

| phrases          | second | return           |
|------------------|--------|------------------|
| "happy-birthday" | 3      | "___________hap" |

---

## 🧠 Giải thích

- Ban đầu, màn hình là `"______________"` (14 dấu gạch dưới).
- Sau 3 giây, 3 ký tự đầu tiên `"hap"` bắt đầu xuất hiện ở cuối chuỗi → `"___________hap"`.
