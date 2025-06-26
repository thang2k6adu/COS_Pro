# 💴 Tối thiểu hóa số lượng tiền thối lại

## 📖 Mô tả

Tại Hàn Quốc, có 8 loại tiền như sau:

- **Tiền xu**: 10 won, 50 won, 100 won, 500 won  
- **Tiền giấy**: 1,000 won, 5,000 won, 10,000 won, 50,000 won

Khi cần **trả lại tiền thừa cho khách**, mục tiêu là **sử dụng ít đồng xu và tờ tiền nhất có thể**.

Ví dụ, nếu cần trả lại **2,760 won**, ta có thể trả như sau:

- 1,000 won × 2 tờ  
- 500 won × 1 đồng  
- 100 won × 2 đồng  
- 50 won × 1 đồng  
- 10 won × 1 đồng

Tổng cộng là **7 đơn vị tiền**, đây là cách tối ưu.

---

## 📥 Tham số

### `money: int`

- Số tiền cần thối lại cho khách
- Là số tự nhiên từ **10 đến 100,000**
- Luôn là **bội số của 10**

---

## 📤 Giá trị trả về

- Trả về **tổng số đồng xu và tờ tiền ít nhất** cần dùng để thối lại đúng số tiền `money`.

---

## 📘 Ví dụ

| money | return |
|-------|--------|
| 2760  | 7      |

### 🧾 Giải thích:

Trả lại 2760 won như sau:

- 1,000 won: 2 tờ  
- 500 won: 1 đồng  
- 100 won: 2 đồng  
- 50 won: 1 đồng  
- 10 won: 1 đồng  

=> Tổng cộng 7 đơn vị tiền → `return 7`.

---

## 🧠 Yêu cầu

Viết hàm `solution(money)` sao cho thực hiện đúng logic trên và trả về số lượng tiền nhỏ nhất cần dùng.

