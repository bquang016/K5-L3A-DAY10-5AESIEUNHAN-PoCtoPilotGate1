# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): 5AESIEUNHAN
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-5AESIEUNHAN-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S8

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
- Khối 3: Xử lý thẻ sự cố S8. Cấu hình giải tỏa lòng tin của nhân viên CSKH (`review_sampling_pct: 10`, `decision_note: true`), soạn thảo Runbook 4 & Runbook 5 (C11), giải tỏa hàng chờ từ 216 phút xuống 5 phút, 0 ca ùn tắc.

### Đóng góp cụ thể

- Đã viết mục tiêu của chị Hạnh, soát tiêu chí theo tải người duyệt, thời gian chờ, ca ùn, chi phí.
- Thiết lập phân công trực ca: PIC Lê Thanh Tùng (`NV-TUNG`), người duyệt Trần Thị Hạnh (`NV-HANH`), 1 người trực/ca, công suất 6 ca/giờ, trần thời gian chờ duyệt tối đa 60 phút.
- Soạn thảo quy trình ngắt khẩn cấp 5 phút và cơ chế gọi thêm người trực khi hàng chờ vượt quá 4 ca hoặc chạm ngưỡng 20 phút.
- Thiết lập cơ chế kiểm mẫu ngẫu nhiên 10% kết hợp ghi chú giải thích minh bạch (`decision_note: true`), giúp đội CSKH dừng kiểm tra thủ công 100%, giải tỏa triệt để 36 ca ùn tắc của sự cố S8.

### Bằng chứng

- `templates/form-a-criteria.md`: A1 câu 1.2 dòng chị Hạnh, A2 câu 1.4, A3 câu 1.5, A4.
- `config/operating_gates.json`: mục `operations`.
- `templates/form-b-evaluation-gates.md`: B7.5 (Runbook 1–3), B7.6 (Giờ cao điểm), checklist B5 mục 5 & 7.
- `templates/form-c-incident.md`: C11 (Runbook 4 & 5, Cập nhật checklist).

### Exit ticket

- Học được: Cách xây dựng và khôi phục lòng tin của đội ngũ vận hành thực tế thông qua các cơ chế phối hợp minh bạch (ghi chú giải thích và kiểm tra mẫu theo tỷ lệ thống nhất).
- Chưa chắc: Khả năng mở rộng quy mô đội duyệt khi hệ thống mở rộng phục vụ thêm nhiều sàn thương mại điện tử đối tác.

## DangVietAnh-2A202603685

### Phần việc phụ trách

Sản phẩm (PO).
- Khối 1: Phiếu A câu 1.1 và câu 1.6 (A4); bộ thử 22 ticket × 5 seed.
- Khối 2: Bản đồ dữ liệu và phân tích trôi dạt (drift) chính sách tại Phiếu B mục B3; xây dựng Checklist 9 nhóm việc nghiệm thu go-live tại Phiếu B mục B5; cùng trưởng nhóm thống nhất quyết định Gate 1 v1 tại Phiếu B mục B8.
- Khối 3: Xử lý thẻ sự cố S8. Phân tích Specification và giả định môi trường (C5), cập nhật fault tree (C6, C9), soạn thảo quyết định Gate 1 v2 "Tiếp tục" tại C12 và 3 dòng bắt buộc cho `submission.json`.

### Đóng góp cụ thể

- Viết mục tiêu cấp hệ thống ở câu 1.1 (A1). Điền câu "Nếu … thì …" cho `pass_rate_min` (97%) và `pass_k_min` (95%) ở câu 1.6.
- Phân tích rủi ro trôi dạt chính sách khi nâng cấp từ `REFUND-v3` lên `REFUND-v4` (đơn trễ 1 ngày được voucher 20k) và cách ghim phiên bản chính sách.
- Thiết lập checklist 9 nhóm việc rõ ràng với từng PIC chịu trách nhiệm cụ thể. Soạn thảo quyết định Gate 1 v1 "Tiếp tục" dựa trên bằng chứng mốc prepared đạt 100%.
- Định nghĩa chuẩn mực Specification cho việc sử dụng mã phê duyệt (phải đảm bảo 5 điều kiện hợp lệ đồng thời). Soạn thảo quyết định Gate 1 v2 "Tiếp tục" với đầy đủ bằng chứng thực nghiệm và 3 dòng bắt buộc.

### Bằng chứng

- `templates/form-a-criteria.md`: A1 câu 1.1, A4 bước 1.
- `templates/form-b-evaluation-gates.md`: B3 (Bản đồ dữ liệu và drift), B5 (Checklist 9 nhóm việc), B6 (Pre-mortem), B8 (Quyết định Gate 1 v1).
- `templates/form-c-incident.md`: C5 (Spec & Giả định), C6 & C9 (Fault Tree), C12 (Quyết định Gate 1 v2).
- `submission/submission.json`: `decision_v2` và `three_lines`.

### Exit ticket

- Học được: Một hệ thống AI khi tích hợp vào doanh nghiệp phải tôn trọng tuyệt đối thẩm quyền phân cấp của con người và phải chịu sự ràng buộc chặt chẽ của quy chế tài chính.
- Chưa chắc: Tần suất cần thiết để cập nhật lại các quy tắc kiểm tra logic nghiệp vụ khi có thay đổi trong quy trình quản trị doanh nghiệp.

## BuiDangQuang-2A202603640

### Phần việc phụ trách

Trưởng nhóm / Kỹ sư cổng.
- Khối 1: Quản trị Git, cấu hình môi trường, viết Phiếu A câu 1.3 (Offline metric cho `file_carrier_fault`), tham gia câu 1.5, ký Bản tiêu chí chấp nhận.
- Khối 2: Thực thi Lệnh 2 (đánh giá base), Lệnh 4 (soi gate base), Lệnh 3 (trace soát lỗi `T-002@55`); xây dựng 3 cổng an toàn trong `lab10/guards.py`; viết behavioral test adhoc; thực hiện chốt cổng vòng 1 (`lab10.checkpoint`) và đo mốc `prepared`.
- Khối 3: Xử lý thẻ sự cố S8. Thực hiện dò trace các ticket hỏng (`S8-01`, `S8-02`, `S8-03`, `S8-43`), lập trình cổng an toàn kiểm tra 5 điều kiện hợp lệ của approval và trần hoàn tiền 300k/khách trong `lab10/guards.py`; bổ sung metric `invalid_approval_rate` trong `lab10/monitors.py`; thực hiện đánh giá kiểm tra mốc after và hồi quy base.

### Đóng góp cụ thể

- Phân tích nguyên nhân gốc ca `T-002@55`: mô hình ghi đè số ngày trễ theo lời khai khách (5 ngày) thay vì tracking DB (2 ngày).
- Lập trình cổng `write_gate` trong `lab10/guards.py`: (1) Chặn hoàn tiền vượt quyền lợi tracking `H.entitlement_vnd`, (2) Chặn ghi lỗi oan cho hãng nếu tracking không xác nhận lỗi `H.carrier_at_fault`, (3) Chuyển duyệt khi chạm trần hoàn tiền ngày `daily_refund_cap_vnd`.
- Kiểm thử và chạy chốt checkpoint vòng 1 thành công (hash `08b820c7`).
- Phát hiện lỗi logic trong việc sử dụng bảng `approvals` của sự cố S8; lập trình bổ sung cổng xác thực approval và cổng giới hạn 300k/khách/ngày; thêm monitor `invalid_approval_rate`, đưa pass_rate trên gói sự cố S8 từ 86.54% lên 100%, hoàn sai về 0đ, lỗi oan về 0, ROI đạt 2.39.

### Bằng chứng

- `lab10/guards.py`, `lab10/guards_round1.py`, `config/round1.lock`, `lab10/monitors.py`.
- `templates/form-b-evaluation-gates.md`: B0, B1, B2, B7.1, B7.2, B7.3, B8.
- `templates/form-c-incident.md`: C0, C1, C2, C7, C8.
- Báo cáo chạy: `R-S8-before-20261118-165638-85f037`, `R-S8-prepared-20261118-165638-85f037`, `R-S8-after-20261118-165620-85f037`.

### Exit ticket

- Học được: Các API và database nội bộ luôn chứa dữ liệu lịch sử không còn hiệu lực; phần mềm AI tuyệt đối không được truy vấn và sử dụng dữ liệu ủy quyền một cách ngây thơ mà bắt buộc phải có cổng xác thực nghiệp vụ đa tầng.
- Chưa chắc: Cách thiết kế kiến trúc phân tán để đồng bộ thời gian thực trạng thái thu hồi phê duyệt giữa nhiều vùng dịch vụ.

## LeHoangSon-2A202603662

### Phần việc phụ trách

Kinh doanh.
- Khối 1: Soạn tiêu chí an toàn tài chính và chi phí ở câu 1.6; chuẩn bị số liệu `business_ops` và trần hoàn tiền ngày.
- Khối 2: Cấu hình kinh doanh trong `config/operating_gates.json` mục `business`; phân tích cơ cấu chi phí ticket, ROI và rủi ro theo từng kho/hãng trong báo cáo đánh giá nền; điền Phiếu B mục B7.4.
- Khối 3: Xử lý thẻ sự cố S8. Phân tích tác động tài chính của các khoản hoàn sai 6.845k và trần 300k/khách/ngày (C2, C7), phân tích chi phí ticket sau sửa (2.952đ) và ROI phục hồi lên 2.39 (C11, C12).

### Đóng góp cụ thể

- Hoàn thành các câu tiêu chí cho `wrongful_refund_vnd_max = 0`, `wrongful_carrier_faults_max = 0`, `pii_leaks_max = 0` trong Phiếu A mục A4.
- Thiết lập thông số mục `business`: `daily_refund_cap_vnd = 2000000`, `cost_budget_per_ticket_vnd = 1500`, `roi_min = 0.2`, `pilot_scope: all`.
- Phân tích báo cáo theo kho: cảnh báo kho `?` có chi phí 10.359đ/ticket cao hơn chi phí xử lý thủ công (10.000đ); xác nhận tổng thể ROI đạt 1.29 ở vòng 1.
- Phân tích rủi ro tài chính của sự cố S8: khoản hoàn sai 6.845.000đ làm thâm hụt ngân sách nặng nề và ROI rơi xuống mức âm (-2.44); xác nhận các cổng sửa ở vòng 2 đã khôi phục ROI lên 2.39 và tiết kiệm ròng 366.479đ/ngày.

### Bằng chứng

- `templates/form-a-criteria.md`: A4 mục kinh doanh.
- `config/operating_gates.json`: mục `business`.
- `templates/form-b-evaluation-gates.md`: B7.4, B1, B8.
- `templates/form-c-incident.md`: C7 (hiệu quả chi phí), C12 (phân tích chỉ số kinh doanh v2).

### Exit ticket

- Học được: Lòng tin của con người và hiệu quả tài chính có mối quan hệ biện chứng; khi con người mất lòng tin, chi phí kiểm tra thủ công sẽ xóa sổ hoàn toàn mọi lợi ích kinh tế mà AI mang lại.
- Chưa chắc: Tác động của chính sách bồi hoàn linh hoạt đến chỉ số giữ chân khách hàng (retention rate) dài hạn.

## ChuThanNhat-2A202603649

### Phần việc phụ trách

Pháp lý.
- Khối 1: Phiếu A câu 1.2 phần chị Oanh đối soát kế toán; câu 1.4 thiết kế Telemetry production phát hiện thiệt hại đối tác không nhãn; rà soát điều khoản PII.
- Khối 2: Thực hiện phân tích rủi ro HAZOP vòng 1 tại Phiếu B mục B4; đóng góp lăng kính Pháp lý trong Pre-mortem tại B6; thiết lập cấu hình tuân thủ pháp luật trong `config/operating_gates.json` mục `legal`.
- Khối 3: Xử lý thẻ sự cố S8. Phân tích HAZOP sự cố S8 (C4), phân tích hiệu chỉnh lòng tin và trách nhiệm giải trình của Trưởng ca CSKH (C3.4), xây dựng Risk Register (C10) quản trị rủi ro phê duyệt tài chính.

### Đóng góp cụ thể

- Soạn thảo phân tích HAZOP cho công cụ `issue_refund` với các guideword WRONG, INVALID, INCOMPLETE, PERTURBED và các rủi ro ngoài kỹ thuật.
- Cấu hình chặn rò rỉ dữ liệu cá nhân khách hàng sang bên thứ ba: `pii_fields_blocked_to_third_party: ["phone", "customer_name", "address"]` theo Nghị định 13/2023/NĐ-CP.
- Quy định điều kiện ghi phạt lỗi hãng: bắt buộc có nguyên nhân lỗi được ghi nhận chính thức (`carrier_fault_requires_recorded_cause: true`).
- Phân tích rủi ro pháp lý của việc mạo danh chữ ký duyệt trong sự cố S8; thiết lập điều khoản bảo vệ trách nhiệm giải trình của Trưởng ca CSKH (`NV-HANH`); bổ sung mục rủi ro ủy quyền phê duyệt vào Risk Register (C10).

### Bằng chứng

- `templates/form-a-criteria.md`: A1 câu 1.2 dòng chị Oanh, A2 câu 1.4 telemetry production.
- `config/operating_gates.json`: mục `legal`.
- `templates/form-b-evaluation-gates.md`: B4 (HAZOP vòng 1), B6 (Pre-mortem Pháp lý), B7.2.
- `templates/form-c-incident.md`: C3.4 (Hiệu chỉnh lòng tin), C4 (HAZOP S8), C10 (Risk Register).

### Exit ticket

- Học được: Trong các hệ thống ra quyết định tự động, việc gắn trách nhiệm giải trình cá nhân cho con người phải đi kèm cơ chế kiểm soát kỹ thuật để người đứng tên không bị quy trách nhiệm cho các hành động mà họ không thực hiện.
- Chưa chắc: Khung pháp lý điều chỉnh trách nhiệm bồi thường thiệt hại khi AI gây ra lỗi hệ thống trong các hợp đồng hợp tác đa phương (sàn - ví điện tử - đơn vị vận chuyển).
