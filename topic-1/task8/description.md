# 🗳️ Bài toán: Tìm ứng cử viên có số phiếu cao nhất

---

## 📄 Mô tả

Đã tiến hành bỏ phiếu cho các ứng cử viên từ số **1 đến N**.  
Ví dụ, kết quả bỏ phiếu là:  
```python
[1, 5, 4, 3, 2, 5, 2, 5, 5, 4]
Điều này có nghĩa là phiếu bầu lần lượt được ghi nhận cho:
[ứng cử viên số 1, số 5, số 4, số 3, số 2, số 5, số 2, số 5, số 5, số 4].

Trong trường hợp này, ta cần xác định ứng cử viên có nhiều phiếu bầu nhất.

Hàm solution được cung cấp có nhiệm vụ:
Khi được truyền vào:

Số lượng ứng cử viên N

Danh sách kết quả bầu cử votes

Hàm sẽ trả về danh sách số hiệu của ứng cử viên có số phiếu cao nhất.

Tuy nhiên, một dòng trong hàm bị sai, khiến một số đầu vào không cho kết quả chính xác.
👉 Bạn cần chỉ sửa duy nhất một dòng code để hàm hoạt động đúng cho mọi đầu vào.

📌 Mô tả tham số
N: Số lượng ứng cử viên (giá trị từ 1 đến 10).

votes: Danh sách phiếu bầu (độ dài từ 1 đến 100).

Mỗi phần tử là số nguyên từ 1 đến N, biểu thị số hiệu ứng cử viên được chọn.

🔁 Giá trị trả về
Trả về danh sách chứa số hiệu của ứng cử viên có nhiều phiếu bầu nhất.

Nếu có nhiều ứng cử viên đồng hạng nhất, hãy trả về toàn bộ số hiệu của họ, được sắp xếp tăng dần.

✅ Ví dụ
🧪 Ví dụ 1
python
Copy
Edit
N = 5
votes = [1, 5, 4, 3, 2, 5, 2, 5, 5, 4]
📊 Kết quả kiểm phiếu:

1번 → 1 phiếu

2번 → 2 phiếu

3번 → 1 phiếu

4번 → 2 phiếu

5번 → 4 phiếu

🎯 Kết quả trả về:

python
Copy
Edit
[5]
🧪 Ví dụ 2
python
Copy
Edit
N = 3
votes = [1, 2, 3, 2, 3]
📊 Kết quả kiểm phiếu:

1번 → 1 phiếu

2번 → 2 phiếu

3번 → 2 phiếu

🎯 Hai ứng cử viên đồng hạng nhất là 2 và 3, nên kết quả là:

python
Copy
Edit
[2, 3]