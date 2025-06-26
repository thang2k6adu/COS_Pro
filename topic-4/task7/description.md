# ⚔️ Bài toán: Tính máu còn lại của các đơn vị trong trò chơi

Trong trò chơi, có ba loại đơn vị: **Quái vật (Monster)**, **Chiến binh (Warrior)** và **Healer (Hồi máu)**.

Để tính toán sự thay đổi của lượng máu (HP) khi các đơn vị bị tấn công hoặc được hồi máu, người ta định nghĩa các lớp `Unit`, `Monster`, `Warrior`, và `Healer` như sau:

---

## 🧱 Cấu trúc lớp

### 🔹 Lớp `Unit`
- Đại diện cho đơn vị chung.
- Thuộc tính:
  - `HP`: máu ban đầu là **1,000**
- Phương thức:
  - `under_attack`: khi bị tấn công, giảm lượng máu tương ứng.

---

### 🔹 Lớp `Monster`
- Kế thừa từ `Unit`, đại diện cho **quái vật**.
- Thuộc tính:
  - `attack_point`: sức tấn công của quái vật.
- Phương thức:
  - `attack`: trả về sức tấn công.
  - `under_attack`: khi bị tấn công, máu bị giảm.

---

### 🔹 Lớp `Warrior`
- Kế thừa từ `Unit`, đại diện cho **chiến binh**.
- Thuộc tính:
  - `attack_point`: sức tấn công của chiến binh.
- Phương thức:
  - `attack`: trả về sức tấn công.
  - `under_attack`: khi bị tấn công, máu bị giảm.

---

### 🔹 Lớp `Healer`
- Kế thừa từ `Unit`, đại diện cho **hồi máu**.
- Thuộc tính:
  - `healing_point`: lượng máu có thể hồi.
- Phương thức:
  - `healing`: hồi máu cho đơn vị khác bằng `healing_point`.
  - `under_attack`: khi bị tấn công, máu bị giảm.
> ⚠️ Lưu ý: máu sau khi hồi **có thể vượt quá 1,000**.

---

## 🎮 Tình huống mô phỏng

1. **Quái vật tấn công** chiến binh và healer, mỗi người **một lần**.
2. **Chiến binh tấn công** quái vật một lần.
3. **Healer hồi máu** cho quái vật và chiến binh, mỗi người một lần.

---

## 📥 Tham số đầu vào

Hàm `solution` nhận vào 3 tham số:

| Tham số               | Mô tả                        | Giá trị giới hạn         |
|------------------------|-------------------------------|---------------------------|
| `monster_attack_point` | Sức tấn công của quái vật     | 1 ≤ giá trị ≤ 500         |
| `warrior_attack_point` | Sức tấn công của chiến binh   | 1 ≤ giá trị ≤ 500         |
| `healing_point`        | Lượng hồi máu của healer      | 1 ≤ giá trị ≤ 500         |

---

## 📤 Kết quả trả về

- Sau khi tất cả các hành động diễn ra, hãy trả về một **danh sách gồm 3 phần tử** theo thứ tự:
  - Máu còn lại của quái vật
  - Máu còn lại của chiến binh
  - Máu còn lại của healer

---

## 🧪 Ví dụ

### Input:
```python
monster_attack_point = 100  
warrior_attack_point = 90  
healing_point = 30

📖 Giải thích chi tiết
Ban đầu tất cả các đơn vị có HP = 1,000

Quái vật tấn công:

Chiến binh: 1,000 → 900

Healer: 1,000 → 900

Chiến binh tấn công quái vật:

Quái vật: 1,000 → 910

Healer hồi máu:

Quái vật: 910 → 940

Chiến binh: 900 → 930