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

Vận hành.
- Khối 1: Phiếu A câu 1.2 phần chị Hạnh; phối hợp câu 1.4 với Chu Thân Nhất, tham gia câu 1.5 và góp ý vận hành cho câu 1.6.
- Khối 2: Cấu hình vận hành trong `config/operating_gates.json` mục `operations`; soạn thảo Runbook 1, 2, 3 tại Phiếu B mục B7.5 và phương án ứng phó giờ cao điểm tại Phiếu B mục B7.6.

### Đóng góp cụ thể

- Đã viết mục tiêu của chị Hạnh, soát tiêu chí theo tải người duyệt, thời gian chờ, ca ùn, chi phí.
- Thiết lập phân công trực ca: PIC Lê Thanh Tùng (`NV-TUNG`), người duyệt Trần Thị Hạnh (`NV-HANH`), 1 người trực/ca, công suất 6 ca/giờ, trần thời gian chờ duyệt tối đa 60 phút.
- Soạn thảo quy trình ngắt khẩn cấp 5 phút và cơ chế gọi thêm người trực khi hàng chờ vượt quá 4 ca hoặc chạm ngưỡng 20 phút.

### Bằng chứng

- `templates/form-a-criteria.md`: A1 câu 1.2 dòng chị Hạnh, A2 câu 1.4, A3 câu 1.5, A4.
- `config/operating_gates.json`: mục `operations`.
- `templates/form-b-evaluation-gates.md`: B7.5 (Runbook 1–3), B7.6 (Giờ cao điểm), checklist B5 mục 5 & 7.

### Exit ticket

- Học được: Cách cân bằng giữa tỉ lệ chuyển người duyệt (escalation rate) và năng lực tiếp nhận thực tế của nhân sự CSKH để không làm sập hàng chờ vận hành.
- Chưa chắc: Tác động trễ dây chuyền khi có bão lũ diện rộng làm số lượng ca khiếu nại tăng vọt gấp 5-10 lần bình thường.

## DangVietAnh-2A202603685

### Phần việc phụ trách

Sản phẩm (PO).
- Khối 1: Phiếu A câu 1.1 và câu 1.6 (A4); bộ thử 22 ticket × 5 seed.
- Khối 2: Bản đồ dữ liệu và phân tích trôi dạt (drift) chính sách tại Phiếu B mục B3; xây dựng Checklist 9 nhóm việc nghiệm thu go-live tại Phiếu B mục B5; cùng trưởng nhóm thống nhất quyết định Gate 1 v1 tại Phiếu B mục B8.

### Đóng góp cụ thể

- Viết mục tiêu cấp hệ thống ở câu 1.1 (A1). Điền câu "Nếu … thì …" cho `pass_rate_min` (97%) và `pass_k_min` (95%) ở câu 1.6.
- Phân tích rủi ro trôi dạt chính sách khi nâng cấp từ `REFUND-v3` lên `REFUND-v4` (đơn trễ 1 ngày được voucher 20k) và cách ghim phiên bản chính sách.
- Thiết lập checklist 9 nhóm việc rõ ràng với từng PIC chịu trách nhiệm cụ thể. Soạn thảo quyết định Gate 1 v1 "Tiếp tục" dựa trên bằng chứng mốc prepared đạt 100%.

### Bằng chứng

- `templates/form-a-criteria.md`: A1 câu 1.1, A4 bước 1.
- `templates/form-b-evaluation-gates.md`: B3 (Bản đồ dữ liệu và drift), B5 (Checklist 9 nhóm việc), B6 (Pre-mortem), B8 (Quyết định Gate 1 v1).
- Mã lần chạy chứng minh: `R-base-prepared-20261118-162402-293671`.

### Exit ticket

- Học được: Quyết định Gate 1 chỉ có tính thuyết phục khi gắn chặt với bằng chứng đo lường thực tế trên bộ thử và đối chiếu nghiêm ngặt với tiêu chí đã ký kết trước đó.
- Chưa chắc: Khả năng thích ứng của trợ lý khi có các chính sách bồi hoàn linh hoạt theo từng hạng thành viên (VIP, Kim cương).

## BuiDangQuang-2A202603640

### Phần việc phụ trách

Trưởng nhóm / Kỹ sư cổng.
- Khối 1: Quản trị Git, cấu hình môi trường, viết Phiếu A câu 1.3 (Offline metric cho `file_carrier_fault`), tham gia câu 1.5, ký Bản tiêu chí chấp nhận.
- Khối 2: Thực thi Lệnh 2 (đánh giá base), Lệnh 4 (soi gate base), Lệnh 3 (trace soát lỗi `T-002@55`); xây dựng 3 cổng an toàn trong `lab10/guards.py`; viết behavioral test adhoc; thực hiện chốt cổng vòng 1 (`lab10.checkpoint`) và đo mốc `prepared`.

### Đóng góp cụ thể

- Phân tích nguyên nhân gốc ca `T-002@55`: mô hình ghi đè số ngày trễ theo lời khai khách (5 ngày) thay vì tracking DB (2 ngày).
- Lập trình cổng `write_gate` trong `lab10/guards.py`: (1) Chặn hoàn tiền vượt quyền lợi tracking `H.entitlement_vnd`, (2) Chặn ghi lỗi oan cho hãng nếu tracking không xác nhận lỗi `H.carrier_at_fault`, (3) Chuyển duyệt khi chạm trần hoàn tiền ngày `daily_refund_cap_vnd`.
- Kiểm thử và chạy chốt checkpoint vòng 1 thành công (hash `08b820c7`), đưa pass_rate từ 99.09% lên 100%, pass_k đạt 1.0, hoàn sai 0đ, lỗi oan 0 ca, ROI đạt 1.29.

### Bằng chứng

- `lab10/guards.py`, `lab10/guards_round1.py`, `config/round1.lock`.
- `templates/form-b-evaluation-gates.md`: B0, B1, B2, B7.1, B7.2, B7.3, B8.
- Báo cáo chạy: `R-base-before-20261118-154948-bde05c`, `R-base-after-20261118-162337-293671`, `R-base-prepared-20261118-162402-293671`.

### Exit ticket

- Học được: Tuyệt đối không để LLM tự quyết các tham số then chốt liên quan đến tiền bạc và quyền lợi đối tác; phải dùng cổng code bám vào nguồn sự thật (Source of Truth) từ cơ sở dữ liệu.
- Chưa chắc: Phương án tối ưu hóa chi phí token LLM khi lượng context của các đơn hàng phức tạp có nhiều kiện phát sinh đồng thời.

## LeHoangSon-2A202603662

### Phần việc phụ trách

Kinh doanh.
- Khối 1: Soạn tiêu chí an toàn tài chính và chi phí ở câu 1.6; chuẩn bị số liệu `business_ops` và trần hoàn tiền ngày.
- Khối 2: Cấu hình kinh doanh trong `config/operating_gates.json` mục `business`; phân tích cơ cấu chi phí ticket, ROI và rủi ro theo từng kho/hãng trong báo cáo đánh giá nền; điền Phiếu B mục B7.4.

### Đóng góp cụ thể

- Hoàn thành các câu tiêu chí cho `wrongful_refund_vnd_max = 0`, `wrongful_carrier_faults_max = 0`, `pii_leaks_max = 0` trong Phiếu A mục A4.
- Thiết lập thông số mục `business`: `daily_refund_cap_vnd = 2000000`, `cost_budget_per_ticket_vnd = 1500`, `roi_min = 0.2`, `pilot_scope: all`.
- Phân tích báo cáo theo kho: cảnh báo kho `?` có chi phí 10.359đ/ticket cao hơn chi phí xử lý thủ công (10.000đ); xác nhận tổng thể ROI đạt 1.29 (tiết kiệm ròng ~124k/ngày).

### Bằng chứng

- `templates/form-a-criteria.md`: A4 mục kinh doanh.
- `config/operating_gates.json`: mục `business`.
- `templates/form-b-evaluation-gates.md`: B7.4, B1, B8.

### Exit ticket

- Học được: Một hệ thống AI chỉ có tính khả thi trong doanh nghiệp nếu chứng minh được bài toán ROI dương và chi phí trên mỗi đơn vị giao dịch thấp hơn làm tay.
- Chưa chắc: Cơ chế phân bổ ngân sách bồi hoàn linh hoạt giữa các kho trong những đợt kích cầu thương mại điện tử lớn.

## ChuThanNhat-2A202603649

### Phần việc phụ trách

Pháp lý.
- Khối 1: Phiếu A câu 1.2 phần chị Oanh đối soát kế toán; câu 1.4 thiết kế Telemetry production phát hiện thiệt hại đối tác không nhãn; rà soát điều khoản PII.
- Khối 2: Thực hiện phân tích rủi ro HAZOP vòng 1 tại Phiếu B mục B4; đóng góp lăng kính Pháp lý trong Pre-mortem tại B6; thiết lập cấu hình tuân thủ pháp luật trong `config/operating_gates.json` mục `legal`.

### Đóng góp cụ thể

- Soạn thảo phân tích HAZOP cho công cụ `issue_refund` với các guideword WRONG, INVALID, INCOMPLETE, PERTURBED và các rủi ro ngoài kỹ thuật (tranh chấp đối soát, vi phạm dữ liệu).
- Cấu hình chặn rò rỉ dữ liệu cá nhân khách hàng sang bên thứ ba: `pii_fields_blocked_to_third_party: ["phone", "customer_name", "address"]` theo Nghị định 13/2023/NĐ-CP.
- Quy định điều kiện ghi phạt lỗi hãng: bắt buộc có nguyên nhân lỗi được ghi nhận chính thức (`carrier_fault_requires_recorded_cause: true`) để bảo vệ tài xế và hãng giao vận khỏi bị phạt oan.

### Bằng chứng

- `templates/form-a-criteria.md`: A1 câu 1.2 dòng chị Oanh, A2 câu 1.4 telemetry production.
- `config/operating_gates.json`: mục `legal`.
- `templates/form-b-evaluation-gates.md`: B4 (HAZOP vòng 1), B6 (Pre-mortem Pháp lý), B7.2.

### Exit ticket

- Học được: Các rào cản pháp lý và bảo vệ dữ liệu cá nhân không thể giải quyết bằng prompt thuần túy mà phải được kiểm soát bằng quy định cứng trong cấu hình và cổng kiểm soát đầu ra.
- Chưa chắc: Quy trình hòa giải và thẩm quyền phân xử khi phát sinh tranh chấp bồi thường đa phương (khách - sàn - kho - bưu tá).
