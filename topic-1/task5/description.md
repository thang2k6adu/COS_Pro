# Bài toán: Tổng các số nằm trên đường chéo trong ma trận xoáy ốc

## Mô tả

Bạn có một lưới (ma trận) kích thước `n x n`, trong đó các số từ **1 đến n × n** được đặt theo thứ tự nhất định.

Khi các số được sắp xếp theo **hình xoắn ốc** như trong hình minh họa, ma trận đó được gọi là **ma trận xoáy ốc bậc n**.

Trong ma trận xoáy ốc, bạn cần **tính tổng các số nằm trên đường chéo chính** — tức là từ ô ở hàng 1 cột 1 đến ô ở hàng n cột n.

## Tham số đầu vào

- `n` (_integer_): một số nguyên đại diện cho kích thước của ma trận `n x n`.
- Ràng buộc: `1 <= n <= 100`

## Kết quả đầu ra

- Trả về **tổng các số nằm trên đường chéo chính** của ma trận xoáy ốc bậc `n`.

## Ví dụ

### Ví dụ 1

**Input:**
n = 3
**Ma trận xoáy ốc:**
1 2 3
8 9 4
7 6 5
**Đường chéo chính:** 1, 9, 5  
**Output:** `15`

### Ví dụ 2

**Input:**
n = 2
**Ma trận xoáy ốc:**
1 2
4 3
**Đường chéo chính:** 1, 3  
**Output:** `4`