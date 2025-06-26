# 📌 Mô tả bài toán: Di chuyển robot theo lệnh

Một con robot chỉ có thể di chuyển theo hướng trục **x** hoặc trục **y**, và có thể điều khiển bằng các chữ cái. Các chữ cái dùng để điều khiển bao gồm 4 loại: **'L'**, **'R'**, **'U'**, **'D'**. Trong đó:

- **'L'** nghĩa là di chuyển theo trục x, lùi về bên trái **-1 đơn vị**
- **'R'** nghĩa là di chuyển theo trục x, tiến về bên phải **+1 đơn vị**
- **'U'** nghĩa là di chuyển theo trục y, đi lên **+1 đơn vị**
- **'D'** nghĩa là di chuyển theo trục y, đi xuống **-1 đơn vị**

Cho một chuỗi lệnh `commands` bao gồm các ký tự được đưa ra theo thứ tự, hãy hoàn thành hàm `solution` sao cho thực hiện lần lượt các lệnh này và **trả về vị trí cuối cùng của robot**.

---

## 🧾 Tham số

### `commands: str`

- Là chuỗi chứa các lệnh điều khiển robot, bao gồm các ký tự `'L'`, `'R'`, `'U'`, `'D'`
- Độ dài chuỗi: **1 ≤ length(commands) ≤ 100**

---

## 🔁 Giá trị trả về

- Trả về vị trí cuối cùng của robot dưới dạng danh sách `[x, y]`
  - `x`: tọa độ theo trục x
  - `y`: tọa độ theo trục y

---

## 📘 Ví dụ

```python
>>> solution("URDDL")
[0, 0]
