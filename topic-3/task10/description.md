# 🧾 Bài toán: Quản lý đặt chỗ cho Tiệm làm tóc và Nhà hàng

Một **tiệm làm tóc** và một **nhà hàng** có các quy tắc nhận đặt chỗ như sau:

---

## ✂️ Tiệm làm tóc (HairShop)

- Chỉ nhận đặt chỗ cho khách **đi một mình (1 người)**.
- **Không được trùng giờ** với bất kỳ khách hàng nào khác.

---

## 🍽️ Nhà hàng (Restaurant)

- Chỉ nhận đặt chỗ khi số người là **từ 2 đến 8 người**.
- **Tối đa hai nhóm** có thể đặt **trùng giờ**.

---

## 👤 Lớp `Customer` (Khách hàng)

- Đại diện cho một khách hàng.
- Các thuộc tính:
  - `id`: Mã định danh khách hàng
  - `time`: Thời gian khách muốn đặt chỗ (giờ)
  - `num_of_people`: Số người đi cùng

---

## 🏪 Lớp `Shop` (Cửa hàng)

- Đại diện cho một cửa hàng.
- Thuộc tính:
  - `reserve_list`: Danh sách khách hàng đã đặt chỗ
- Phương thức:
  - `reserve(customer)`: nhận khách làm đối tượng đầu vào và **thêm vào danh sách nếu đặt thành công**, sau đó trả về `true`.

---

## 💇‍♀️ Lớp `HairShop`

- Kế thừa từ lớp `Shop`.
- Phương thức `reserve(customer)`:
  - Kiểm tra điều kiện:
    - Số người phải là 1.
    - Không được trùng giờ với khách đã đặt.
  - Nếu thoả điều kiện: thêm vào danh sách, trả về `true`.
  - Nếu không: trả về `false`.

---

## 🍴 Lớp `Restaurant`

- Kế thừa từ lớp `Shop`.
- Phương thức `reserve(customer)`:
  - Kiểm tra điều kiện:
    - Số người từ 2 đến 8.
    - Số lượng khách đã đặt cùng giờ không vượt quá 2.
  - Nếu thoả điều kiện: thêm vào danh sách, trả về `true`.
  - Nếu không: trả về `false`.

---

## ✅ Mục tiêu

Bạn được cung cấp:

- `customers`: Danh sách chứa thông tin khách đặt chỗ.
- `shops`: Danh sách chứa tên cửa hàng tương ứng với từng khách muốn đặt.

Viết hàm `solution(customers, shops)` để **trả về số lượng đặt chỗ thành công tại hai cửa hàng**.

> Hãy hoàn thiện đoạn mã bằng cách **điền vào phần còn thiếu**, dựa trên cấu trúc lớp được mô tả ở trên.

---

## 📥 Mô tả tham số

- `customers` và `shops` có **độ dài bằng nhau**.
- Mỗi phần tử trong `customers` là một danh sách gồm:  
  `[ID khách hàng, thời gian đặt (0~23), số người]`
- Giới hạn:
  - `ID khách hàng`: số tự nhiên từ **1 đến 10,000**
  - `Thời gian`: số nguyên từ **0 đến 23**
  - `Số người`: từ **1 đến 10**
  - **ID không trùng lặp**
  - Số lượng khách: từ **1 đến 10**
- Mỗi phần tử trong `shops` là `"hairshop"` hoặc `"restaurant"`
  - `shops[i]` là nơi mà `customers[i]` muốn đặt.

---

## 📤 Kết quả trả về

- Trả về **tổng số lần đặt chỗ thành công** tại hai cửa hàng.

---

## 🧪 Ví dụ

*(Phần ví dụ không được cung cấp trong đề bài gốc)*