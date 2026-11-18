# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): 5AESIEUNHAN
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-5AESIEUNHAN-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |      Bùi Đăng Quang     |   2A202603640   |   Kỹ sư cổng  |       x      |
|   2 |      Lê Hoàng Sơn     |   2A202603662   |   Kinh doanh  |             |
|   3 |      Đặng Việt Anh     |    2A202603685  |   Sản phẩm (PO)  |             |
|   4 |       Hà Huy Thái    |    2A202603682  |  Vận hành   |             |
|   5 |       Chu Thân Nhất    |    2A202603649  |  Pháp lý   |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HaHuyThai-2A202603682

### Phần việc phụ trách

Vận hành. CP2: Phiếu A câu 1.2 phần chị Hạnh; phối hợp câu 1.4 với Chu Thân Nhất, tham gia câu 1.5 và góp ý vận hành cho câu 1.6.

### Đóng góp cụ thể

Đã viết mục tiêu của chị Hạnh, góp ý khả năng tiếp nhận và xử lý cảnh báo production, giải thích lựa chọn (b) ở câu 1.5 và soát tiêu chí theo tải người duyệt, thời gian chờ, ca ùn, chi phí.

### Bằng chứng

`templates/form-a-criteria.md`: A1 câu 1.2 dòng chị Hạnh; góp ý vận hành ở A2 câu 1.4; A3 câu 1.5; A4 phần góp ý và bảng bốn câu hỏi soát.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## DangVietAnh-2A202603685

### Phần việc phụ trách

Sản phẩm (PO). Phiếu A câu 1.1 và câu 1.6 (A4); theo kế hoạch: câu 2.3 (B3), câu 2.9 (`config/operating_gates.json` mục `business`, B7.4), phần kinh doanh của câu 3.5 và quyết định v2 (C12).

### Đóng góp cụ thể

Viết mục tiêu cấp hệ thống ở câu 1.1 (A1). Điền câu "Nếu … thì …" cho `pass_rate_min` (97%) và `pass_k_min` (95%) ở câu 1.6 (A4, bước 1), cùng bộ thử 22 ticket × 5 seed.

### Bằng chứng

Commit `ec3bac5` (merge `5ed0160`, PR #3 từ nhánh `2A202603685`): `templates/form-a-criteria.md`, câu 1.1 và hai dòng `pass_rate_min`, `pass_k_min` trong A4. Mã lần chạy: chưa có, vì tiêu chí chưa ký và chưa chạy đánh giá.

### Exit ticket

Học được: `pass_k` luôn nhỏ hơn hoặc bằng `pass_rate`, nên ngưỡng `pass_k_min` phải đặt thấp hơn `pass_rate_min`. Chưa chắc: công thức ROI và chi phí mỗi ticket có tính tiền người duyệt không; ngưỡng 97% có đủ chặt với bộ 22 ticket × 5 seed không.


## BuiDangQuang-2A202603640

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
