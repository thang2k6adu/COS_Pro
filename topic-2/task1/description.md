# Đề Bài: Tính Phí Thuê Sách

## Mô tả

Giá thuê truyện tranh và tiểu thuyết ở cửa hàng cho thuê sách như sau:

| Phân loại   | Phí thuê cơ bản     | Phí phụ thu                    |
|-------------|---------------------|--------------------------------|
| **Truyện tranh** | 2 ngày đầu: 500 won    | Sau đó, mỗi ngày: thêm 200 won     |
| **Tiểu thuyết**  | 3 ngày đầu: 1000 won   | Sau đó, mỗi ngày: thêm 300 won     |

Để tính phí thuê của truyện tranh và tiểu thuyết, bạn cần xây dựng:

- Giao diện `Book`
- Hai lớp `ComicBook` và `Novel` kế thừa từ `Book`
- Một hàm `solution` nhận danh sách loại sách (`book_types`) và số ngày thuê (`day`) để tính tổng phí thuê

## Yêu cầu

### 1. `Book` (Interface)

- Là giao diện cho tất cả sách
- Có hàm `get_rental_price(day: int) -> int` để tính phí thuê dựa trên số ngày

### 2. `ComicBook` (Truyện tranh)

- Kế thừa từ `Book`
- Tính phí thuê:
  - 2 ngày đầu: 500 won
  - Mỗi ngày thêm sau đó: 200 won/ngày

### 3. `Novel` (Tiểu thuyết)

- Kế thừa từ `Book`
- Tính phí thuê:
  - 3 ngày đầu: 1000 won
  - Mỗi ngày thêm sau đó: 300 won/ngày

### 4. `solution(book_types: List[str], day: int) -> int`

- Nhận vào:
  - `book_types`: danh sách các loại sách muốn thuê, gồm `"comic"` hoặc `"novel"`
  - `day`: số ngày thuê sách
- Trả về:
  - Tổng phí thuê của tất cả sách

## Ràng buộc

- `1 <= len(book_types) <= 50`
- `1 <= day <= 100`
- Mỗi phần tử trong `book_types` là `"comic"` hoặc `"novel"`

## Ví dụ

| `book_types`                 | `day` | `return` |
|-----------------------------|-------|----------|
| `["comic", "comic", "novel"]` |  4    |  3100     |

**Giải thích**:

- Truyện tranh (4 ngày):
  - 2 ngày đầu: 500 won
  - 2 ngày sau: 2 × 200 = 400 won
  - Tổng 1 quyển: 900 won × 2 = 1800 won
- Tiểu thuyết (4 ngày):
  - 3 ngày đầu: 1000 won
  - 1 ngày sau: 300 won
  - Tổng: 1300 won  
- Tổng cộng: 1800 + 1300 = **3100 won**

