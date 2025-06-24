# 🛤️ Bài toán: Tính thời gian chờ tàu điện ngầm

## 📌 Mô tả bài toán

Có một danh sách chứa các thời điểm tàu điện ngầm sẽ đến **ga A** trong ngày hôm nay, được sắp xếp theo thứ tự thời gian. Khi biết **thời gian hiện tại**, bạn cần tính xem **phải chờ ít nhất bao nhiêu phút** nữa để có thể lên tàu điện ngầm.

## 🧩 Cấu trúc chương trình

Chúng ta giải bài toán theo các bước sau:

1. Chuyển đổi thời gian hiện tại thành số **phút kể từ 00:00**.
2. Lặp qua danh sách thời điểm tàu đến (`subway_times`):
   - 2-1. Chuyển đổi từng thời điểm tàu đến thành số phút kể từ 00:00.
   - 2-2. So sánh với thời gian hiện tại để tìm **thời gian chờ tối thiểu**.
3. Trả về giá trị thời gian chờ tối thiểu tìm được ở bước 2.

Một số phần được viết thành hàm phụ `func_a` để tái sử dụng. Nhiệm vụ của bạn là **hoàn thiện phần còn thiếu để chương trình hoạt động đúng**.

---

## 🔧 Tham số

### Tham số đầu vào

- `subway_times`: Danh sách các thời điểm tàu điện ngầm sẽ đến trong ngày (đã sắp xếp theo thời gian).
  - Độ dài: `1 <= len(subway_times) <= 100`
  - Không chứa thời điểm trùng lặp.
- `current_time`: Thời gian hiện tại, dưới dạng chuỗi `"HH:MM"`.

### Định dạng thời gian

- Dùng **định dạng 24 giờ** từ `"00:00"` đến `"23:59"`.
- Tất cả thời gian luôn đúng định dạng `"XX:YY"`, với `XX` là giờ, `YY` là phút.
- **Chuyến tàu đầu tiên**: sau `05:00`.
- **Chuyến tàu cuối cùng**: trước `23:59`.

---

## 🎯 Giá trị trả về

Hàm `solution(subway_times, current_time)` cần trả về:

- **Số phút ít nhất** cần chờ để lên chuyến tàu kế tiếp.
- Nếu không còn chuyến tàu nào có thể đi được trong ngày → **trả về `-1`**.

---

## 📘 Ví dụ

| `subway_times`                        | `current_time` | `return` |
|--------------------------------------|----------------|----------|
| `["05:31", "11:59", "13:30", "23:32"]` | `"12:00"`      | `90`     |
| `["14:31", "15:31"]`                  | `"15:31"`      | `0`      |

### 🧠 Giải thích

- **Ví dụ 1**:  
  - `current_time` là `12:00` → chuyến kế tiếp là `13:30` → cần chờ `90 phút`.

- **Ví dụ 2**:  
  - `current_time` là `15:31` → có chuyến đến đúng lúc này → chờ `0 phút`.

---

