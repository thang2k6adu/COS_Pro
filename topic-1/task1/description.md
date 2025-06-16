## 📦 DeliveryStore

**DeliveryStore** là giao diện (interface) của một cửa hàng giao đồ ăn.

Mọi cửa hàng giao đồ ăn cần ktriển hai (implement) 2 hàm:
- `set_order_list`
- `get_total_price`

- Hàm `set_order_list` nhận vào một danh sách các món ăn được đặt và lưu trữ lại.
- Hàm `get_total_price` trả về tổng giá tiền của các món đã đặt.

---

## 🍽️ Food

**Food** là lớp đại diện cho món ăn.

Mỗi món ăn bao gồm:
- Tên (`name`)
- Giá (`price`)

---

## 🍕 PizzaStore

**PizzaStore** là lớp đại diện cho cửa hàng giao pizza, và triển khai giao diện `DeliveryStore`.

- `menu_list`: lưu danh sách các món ăn có thể đặt tại cửa hàng pizza.
- `order_list`: lưu tên các món ăn đã được khách hàng đặt.

- Hàm `set_order_list`: nhận danh sách món ăn được đặt và lưu vào `order_list`.
- Hàm `get_total_price`: tính tổng giá tiền của tất cả các món trong `order_list` và trả về kết quả.

---

## 🧪 Nhiệm vụ

Viết hàm `solution`, nhận vào danh sách các món ăn được đặt (`order_list`) dưới dạng tham số, và trả về tổng giá trị đơn hàng.

Dựa vào cấu trúc lớp đã cho ở trên, hãy hoàn thiện các phần còn thiếu của mã nguồn để hoàn thành yêu cầu.

---

### 📌 Giải thích tham số

- `order_list`: danh sách tên các món ăn được đặt, truyền vào hàm `solution`.
    - Độ dài của `order_list` từ 1 đến 5 phần tử.
    - Mỗi phần tử là tên món ăn dưới dạng chuỗi (string).
    - Không có món nào bị lặp lại trong `order_list`.
    - Tên món ăn và giá tiền của từng món được khởi tạo sẵn trong constructor của `PizzaStore`.

---

### 📥 Giải thích giá trị trả về

Hàm `solution` cần trả về tổng giá tiền của các món ăn được