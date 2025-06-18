# 🪜 Trò chơi leo cầu thang của hai học sinh A và B

---

## 📄 Mô tả

Hai học sinh A và B đã chơi một trò chơi gọi là "trò chơi cầu thang".  
Quy tắc của trò chơi như sau:

1. Bắt đầu từ bậc thấp nhất của cầu thang (bậc số 0).
2. Chơi oẳn tù tì (gawi-bawi-bo - tương đương với kéo, búa, bao).
3. Nếu thắng: bước lên **3 bậc**.
4. Nếu thua: bước xuống **1 bậc**.
5. Nếu hòa: đứng yên, không di chuyển.
6. Nếu đang ở bậc thấp nhất (bậc 0) và thua → vẫn đứng yên, không bị lùi.
7. Các bước 2–5 được lặp lại **10 lần**.

Sau khi trò chơi kết thúc, ta muốn xác định A đang đứng ở **bậc thang thứ mấy**.

---

## 🧾 Mô tả hàm

Viết hàm `solution` sao cho:
- Khi được truyền vào hai danh sách `recordA` và `recordB` chứa lịch sử chơi oẳn tù tì của A và B (10 lần chơi),
- Hàm trả về **vị trí cầu thang cuối cùng của A**.

---

## 📌 Mô tả tham số

- `recordA`, `recordB`: danh sách độ dài đúng 10, chứa các số nguyên đại diện cho kết quả từng lượt chơi.
  - Mỗi phần tử có giá trị:
    - `0`: kéo
    - `1`: búa
    - `2`: bao

---

## 🔁 Giá trị trả về

- Trả về số nguyên là vị trí cuối cùng của A trên cầu thang sau khi chơi xong 10 lượt.
- Vị trí thấp nhất là **bậc số 0**.

---

## ⚠️ Lưu ý

- Trong đoạn mã được cung cấp sẵn, **có một dòng bị sai** khiến hàm không luôn cho kết quả chính xác.
- Bạn cần **chỉ sửa duy nhất một dòng** để mọi đầu vào đều cho kết quả đúng.

---

## ✅ Ví dụ

(Ảnh ví dụ hiển thị kết quả từng lượt chơi và cách A di chuyển trên cầu thang)