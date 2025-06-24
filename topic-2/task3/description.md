# 📝 Bài toán: Tìm số bài viết cần thêm để nhận phần thưởng

## 📌 Mô tả

Tại **trang web A**, phần thưởng sẽ được trao cho **người đầu tiên viết bài đăng thỏa mãn các điều kiện sau**:

1. Bài đăng phải được viết **sau bài viết cuối cùng hiện tại**.
2. **Số hiệu bài viết** (tức là số thứ tự) phải có **số chữ số chẵn**.
3. Nếu số hiệu bài viết có `2n` chữ số:
   - **Tổng các chữ số của n chữ số đầu** phải **bằng tổng các chữ số của n chữ số cuối**.

> Số hiệu bài viết trên trang được đánh tăng dần. Ví dụ:
>
> Nếu số bài viết cuối hiện tại là `235386`, thì các bài tiếp theo lần lượt là:
> `235387`, `235388`, ...

---

## 🎯 Mục tiêu

Bạn muốn nhận phần thưởng, hãy tính xem **cần viết thêm bao nhiêu bài viết** để bài tiếp theo của bạn là **bài đầu tiên thỏa mãn đủ điều kiện**.

---

## 🧩 Cấu trúc chương trình

Chương trình hoạt động theo các bước:

1. **Tăng số hiệu bài viết lên 1**.
2. Nếu số này có **số chữ số lẻ**, quay lại bước 1.
3. Nếu có **số chữ số chẵn**, thực hiện:
   - 3-1. Chia đôi số thành **nửa đầu** và **nửa sau**.
   - 3-2. Tính **tổng chữ số** của mỗi nửa.
   - 3-3. Nếu **hai tổng bằng nhau**, tiếp tục sang bước 4. Nếu không, quay lại bước 1.
4. Trả về `(số bài viết tìm được - số hiện tại)`.

---

## 📥 Tham số đầu vào

- `num` (int): Số hiệu của bài viết cuối cùng hiện tại.  
  - Ràng buộc: `1 <= num <= 50,000,000`

---

## 📤 Giá trị trả về

Hàm `solution(num)` cần trả về:

- Số lượng **bài viết cần viết thêm** để đến được **bài viết đầu tiên đủ điều kiện nhận phần thưởng**.

---

## 📘 Ví dụ

| `num`     | `return` |
|-----------|----------|
| `1`       | `10`     |
| `235386`  | `20`     |

---

### 🧠 Giải thích

#### Ví dụ 1:

- Số hiện tại là `1`.
- Bài viết đầu tiên thỏa điều kiện là `11`:
  - 2 chữ số → chẵn.
  - Chia làm `1 | 1` → tổng = 1 và 1 → hợp lệ.
- Cần viết thêm: `11 - 1 = 10` bài.

#### Ví dụ 2:

- Số hiện tại: `235386`.
- `235386` → chia thành `235 | 386`:
  - Tổng: `2+3+5 = 10`, `3+8+6 = 17` → không hợp lệ.
- Sau khi viết thêm 20 bài → đến số `235406`:
  - `235 | 406` → tổng: `2+3+5 = 10`, `4+0+6 = 10` → hợp lệ.
- → Cần viết thêm **20 bài**.

---
