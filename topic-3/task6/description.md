# 문제 설명 (Mô tả bài toán)

Bạn đang cố gắng tìm số cách biểu diễn một số nào đó dưới dạng tổng của **ba số nguyên tố khác nhau**.

Ví dụ, số 33 có thể được biểu diễn theo **4 cách khác nhau** như sau:

1. 3 + 7 + 23  
2. 3 + 11 + 19  
3. 3 + 13 + 17  
4. 5 + 11 + 17

Khi một số tự nhiên `n` được truyền vào dưới dạng tham số, bạn cần viết hàm `solution` để trả về **số cách biểu diễn `n` như một tổng của ba số nguyên tố khác nhau**.  
Hãy điền vào phần còn thiếu để hoàn thiện toàn bộ đoạn mã.

> ※ Có tổng cộng 168 số nguyên tố nhỏ hơn hoặc bằng 1,000.

---

## ▣ 매개변수 설명 (Giải thích tham số)

- `n` được truyền vào làm tham số của hàm `solution`.  
- `n` là một số tự nhiên không vượt quá 1,000.

---

## ▣ return 값 설명 (Giải thích giá trị trả về)

- Hãy trả về số cách có thể biểu diễn `n` dưới dạng tổng của **ba số nguyên tố khác nhau**.  
- Nếu không thể biểu diễn `n` như vậy, hãy trả về `0`.

---

## ▣ 예시 (Ví dụ)

| n  | return |
|----|--------|
| 33 | 4      |
| 9  | 0      |

---

## ▣ 예시 설명 (Giải thích ví dụ)

- **Ví dụ #1**: Như đã trình bày ở phần đầu bài, có 4 cách biểu diễn số 33.  
- **Ví dụ #2**: Số 9 không thể được biểu diễn thành tổng của ba số nguyên tố khác nhau.
