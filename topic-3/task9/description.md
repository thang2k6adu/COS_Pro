# 🏪 Bài toán: Mở Popup Store Đạt Doanh Thu Tối Đa

Một cửa hàng đang có kế hoạch mở **popup store**.  
**Popup store** là một cửa hàng chỉ hoạt động trong **thời gian giới hạn**.

Cửa hàng dự định mở **popup store trong k ngày liên tiếp**.  
Bạn được cung cấp danh sách doanh thu ước tính trong **n ngày**, và cần xác định khoảng thời gian **k ngày liên tiếp** nào mang lại **tổng doanh thu cao nhất**.

---

## 📥 Đầu vào

Hàm `solution` nhận vào hai tham số:

- `revenue`: Danh sách doanh thu ước tính trong n ngày  
  - Độ dài từ **1 đến 200,000**
  - Mỗi phần tử là **số tự nhiên không vượt quá 10,000**

- `k`: Số ngày liên tiếp mở popup store  
  - Từ **1 đến 100,000**
  - Không vượt quá độ dài của `revenue`

---

## 🎯 Mục tiêu

Viết hàm `solution` để **trả về tổng doanh thu lớn nhất có thể có trong bất kỳ k ngày liên tiếp nào**.

⚠️ **Lưu ý:**  
Một đoạn mã đã được viết để giải bài toán này, tuy nhiên **một dòng trong mã bị sai**, khiến kết quả không chính xác trong một số trường hợp.  
👉 Hãy **chỉ sửa đúng một dòng duy nhất** để đoạn mã hoạt động chính xác với mọi đầu vào.

---

## 📤 Kết quả trả về

Trả về **tổng doanh thu cao nhất** đạt được trong **k ngày liên tiếp** bất kỳ.

---

## 🧪 Ví dụ

| revenue                   | k | return |
|---------------------------|---|--------|
| [1, 1, 9, 3, 7, 6, 5, 10] | 4 | 28     |
| [1, 1, 5, 1, 1]           | 1 | 5      |

---

## 📚 Giải thích ví dụ

- **Ví dụ #1:**
  Các khoảng 4 ngày liên tiếp và tổng doanh thu:
  - [1, 1, 9, 3] → 14  
  - [1, 9, 3, 7] → 20  
  - [9, 3, 7, 6] → 25  
  - [3, 7, 6, 5] → 21  
  - [7, 6, 5, 10] → **28** (cao nhất)

- **Ví dụ #2:**
  Vì chỉ chọn 1 ngày, nên chọn ngày có doanh thu cao nhất là **5**
