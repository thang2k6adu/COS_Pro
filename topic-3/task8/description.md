# 🌀 Bài toán: Mua thêm quạt cho học sinh

Trong mỗi lớp học có sẵn **4 chiếc quạt máy**.  
Mỗi chiếc quạt có thể làm mát cho **k học sinh**.  
Bạn cần tính xem phải **mua thêm bao nhiêu chiếc quạt** để **tất cả học sinh trong mỗi lớp** đều được làm mát.

---

## 📌 Ví dụ minh họa

Giả sử mỗi quạt có thể làm mát **3 học sinh**, và số học sinh trong mỗi lớp là:

[15, 17, 19, 10, 23]


- Có sẵn 4 chiếc quạt → dùng được cho 4 lớp đầu.
- Cần làm mát cho tất cả học sinh, tính số quạt cần thêm:

| Lớp | Số học sinh | Quạt cần thiết | Quạt còn thiếu |
|-----|-------------|----------------|----------------|
| 1   | 15          | 5              | 1              |
| 2   | 17          | 6              | 2              |
| 3   | 19          | 7              | 3              |
| 4   | 10          | 4              | 0              |
| 5   | 23          | 8              | 4              |

👉 Tổng cộng cần mua thêm **10 chiếc quạt**.

---

## 🧾 Thông tin đầu vào

Hàm `solution` nhận vào hai tham số:

- `k`: Số học sinh mà mỗi quạt có thể làm mát.  
  - Giá trị: **từ 1 đến 25**
- `student`: Danh sách số học sinh trong từng lớp học.  
  - Mỗi lớp có **1 đến 1,000 học sinh**
  - Tổng số lớp: **1 đến 100**

---

## 📤 Giá trị trả về

Trả về **số lượng quạt tối thiểu cần mua thêm** để đảm bảo mọi học sinh trong từng lớp đều được làm mát.

---

## ⚠️ Lưu ý

Một đoạn mã đã được viết để giải bài toán này, **nhưng có một dòng sai**, khiến chương trình không hoạt động chính xác với một số đầu vào.  
👉 Nhiệm vụ của bạn là **sửa đúng một dòng duy nhất** để chương trình chạy đúng với mọi trường hợp.

---

## 🧪 Ví dụ

| k | student              | return |
|---|----------------------|--------|
| 1 | [4, 4, 4, 4]         | 0      |
| 3 | [15, 17, 19, 10, 23] | 10     |

---

## 📚 Giải thích ví dụ

- **Ví dụ 1**: Có 4 lớp, mỗi lớp 4 học sinh. Mỗi quạt làm mát được 1 học sinh, và có sẵn 4 quạt → Không cần mua thêm.
- **Ví dụ 2**: Như đã phân tích ở phần ví dụ minh họa, cần mua thêm 10 quạt.
