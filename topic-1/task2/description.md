# 📘 Bài toán: Khoảng cách Hamming

**Khoảng cách Hamming** là số lượng ký tự khác nhau tại cùng một vị trí giữa hai chuỗi có cùng độ dài.

Ví dụ, với hai chuỗi nhị phân `"10010"` và `"110"` thì trước tiên ta cần làm cho chúng có cùng độ dài bằng cách thêm hai số 0 vào đầu chuỗi `"110"` để biến thành `"00110"`.

Khi đó, các ký tự khác nhau ở vị trí đầu tiên và thứ ba, nên khoảng cách Hamming là 2.

## Mô tả bài toán

Bạn cần viết hàm `solution(binaryA, binaryB)` để tính khoảng cách Hamming giữa hai chuỗi nhị phân `binaryA` và `binaryB`.

Chương trình được xây dựng theo các bước sau:

1. Lấy độ dài lớn hơn trong hai chuỗi nhị phân.
2. Nếu `binaryA` ngắn hơn, thêm các số 0 vào đầu chuỗi để bằng độ dài lớn hơn.
3. Nếu `binaryB` ngắn hơn, cũng thêm các số 0 tương tự.
4. Tính khoảng cách Hamming giữa hai chuỗi đã có cùng độ dài.

Để tránh lặp mã, phần thêm 0 vào đầu chuỗi được viết thành hàm phụ `func_a`.

## Thông tin đầu vào

- `binaryA` là chuỗi nhị phân có độ dài từ 1 đến 10.
- `binaryA` chỉ chứa ký tự `'0'` hoặc `'1'`, không bắt đầu bằng `'0'`.
- `binaryB` tương tự như `binaryA`.

## Thông tin đầu ra

- Trả về một số nguyên là khoảng cách Hamming giữa hai chuỗi.

## Ví dụ

### Input

```python
binaryA = "10010"
binaryB = "110"
