# 🔢 Bài toán: Hoàn thiện Ma Phương 4x4

**Ma phương** là một ma trận hình vuông trong đó **tổng các số theo hàng ngang, hàng dọc và hai đường chéo đều bằng nhau**. Ma phương được tạo thành từ các số **tự nhiên liên tiếp từ 1 đến n²**, và **mỗi số chỉ xuất hiện một lần**.

Ví dụ: Một ma phương 4x4 có tổng hàng, cột và chéo đều bằng 34:

[16, 2, 3, 13]
[ 5, 11, 10, ? ]
[ 9, 7, 6, 12]
[ ?, 14, 15, 1]


Bạn cần **hoàn thiện ma phương 4x4** bằng cách điền vào **2 ô còn trống**, được biểu diễn bằng số `0`.

---

## 🧱 Cấu trúc chương trình

Chương trình thực hiện theo các bước sau:

1. **Tìm vị trí** của hai ô chứa số `0`.
2. **Tìm hai số** từ 1 đến 16 **chưa xuất hiện** trong ma trận.
3. Gán:
   - **Số nhỏ hơn** vào ô trống thứ nhất,
   - **Số lớn hơn** vào ô trống thứ hai,
   - Sau đó **kiểm tra xem ma trận có trở thành ma phương không**.
   - Nếu là ma phương:
     - Trả về: `[hàng số nhỏ, cột số nhỏ, số nhỏ, hàng số lớn, cột số lớn, số lớn]`
   - Nếu **không phải** ma phương:
     - Trả về: `[hàng số lớn, cột số lớn, số lớn, hàng số nhỏ, cột số nhỏ, số nhỏ]`

> **Lưu ý:** Dữ liệu đầu vào đảm bảo luôn có thể hoàn thành thành một ma phương hợp lệ.

---

## 📥 Tham số đầu vào

- `matrix`: một **ma trận 2 chiều 4x4**, chứa:
  - 14 số tự nhiên từ `1` đến `16` không trùng nhau
  - 2 ô trống được đánh dấu bằng số `0`

---

## 📤 Giá trị trả về

Trả về một danh sách gồm **6 phần tử**, thể hiện:
- Vị trí hàng, cột và giá trị của từng ô được điền
- Thứ tự phụ thuộc vào việc sau khi thử điền nhỏ trước, lớn sau có tạo thành ma phương không

---

## 🧪 Ví dụ

| `matrix`                                         | `return`        |
|--------------------------------------------------|------------------|
| `[[16,2,3,13],[5,11,10,0],[9,7,6,12],[0,14,15,1]]` | `[4,1,4,2,4,8]`  |

---

## 📖 Giải thích ví dụ

Trong ma trận ví dụ:

- Hai ô `0` nằm tại:
  - `(4, 1)` — hàng 4, cột 1
  - `(2, 4)` — hàng 2, cột 4

- Hai số còn thiếu là: `4` và `8`

Nếu điền:
- `4` vào `(4, 1)`
- `8` vào `(2, 4)`

→ ma trận trở thành **ma phương hợp lệ**, nên kết quả là:

