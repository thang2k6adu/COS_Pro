# 📈 Tìm đoạn tăng dần dài nhất trong danh sách số tự nhiên

Có một danh sách chứa các số tự nhiên. Trong danh sách này, bạn cần tìm **độ dài của đoạn tăng dần dài nhất**, trong đó:

- Một đoạn được coi là "tăng dần" nếu mỗi số phía sau lớn hơn số liền trước.
- Nếu một số giống với số liền trước thì **không được coi là tăng**.

Ví dụ, với danh sách `[3, 1, 2, 4, 5, 1, 2, 2, 3, 4]`, đoạn `[1, 2, 4, 5]` là đoạn tăng dài nhất, có độ dài là 4.

Hãy viết hàm `solution` sao cho, khi danh sách `arr` chứa các số tự nhiên được truyền vào dưới dạng tham số, hàm sẽ trả về độ dài của đoạn tăng dần dài nhất.

---

## 📌 Mô tả tham số

Danh sách `arr` chứa các số tự nhiên và được truyền vào làm tham số của hàm `solution`.

- Độ dài của `arr`: từ 2 đến 200,000 phần tử.
- Mỗi phần tử trong `arr` là số tự nhiên từ 1 đến 1,000,000.

---

## 🎯 Mô tả giá trị trả về

Hàm cần trả về **độ dài của đoạn tăng dần dài nhất** trong danh sách.

- Nếu không tồn tại đoạn tăng dần nào có độ dài từ 2 trở lên, trả về `1`.

---

## 🧪 Ví dụ

| arr                             | return |
|---------------------------------|--------|
| [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]  | 4      |

---

## 📖 Giải thích ví dụ

Đoạn `[1, 2, 4, 5]` là đoạn tăng dần dài nhất trong danh sách, có độ dài 4.

Chú ý rằng khi hai số liền nhau giống nhau (ví dụ `[2, 2]`) thì không được coi là tăng. Do đó đoạn `[1, 2, 2, 3, 4]` sẽ được chia thành hai đoạn: `[1, 2]` và `[2, 3, 4]`.
