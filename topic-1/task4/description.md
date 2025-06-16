# Bài toán: Cộng 1 trong hệ thống số không có số 0

## Mô tả

Một người đã du hành thời gian về quá khứ và truyền bá một hệ thống số không bao gồm chữ số 0. Lịch sử đã thay đổi, và bây giờ trong ý thức của con người, **số 0 không còn tồn tại**.

Vì vậy, hệ thống số hiện tại là:  
`1, 2, 3, ..., 8, 9, 11, 12, 13, ..., 19, 21, ...`  
— hoàn toàn **không có chữ số 0**.

## Yêu cầu

Cho một số tự nhiên `num` **không chứa chữ số 0**, hãy trả về kết quả của phép tính **num + 1** trong hệ thống số mới (kết quả cũng **không chứa chữ số 0**).

## Tham số

- `num` (_integer_): số tự nhiên không chứa chữ số 0.  
  Ràng buộc:  
  `1 <= num <= 999,999,999,999,999,999`

## Kết quả

- Trả về một số tự nhiên là kết quả của `num + 1`, sau khi thay toàn bộ các chữ số `0` (nếu có) trong kết quả thành `1`.

## Ví dụ

### Ví dụ 1:

**Input:**
```python
num = 9949999