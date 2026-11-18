# Phiếu B · Đo, rủi ro, cổng vòng 1 và quyết định v1 · Khối 2A + 2B + chốt (phút 65–115)

**Bàn:** ______

Tiêu chí đã ký ở Phiếu A. Từ phút 65 bàn mới được chạy trợ lý. Khối 2A (65–85) chưa sửa code hay config. Khối 2B (85–105) sửa
`lab10/guards.py` và `config/operating_gates.json`. Phút 105–115 chốt cổng vòng 1 rồi viết quyết định v1. Sau phút 115 không sửa phiếu này
(trừ khi Phiếu C bảo "mở lại" một ô và ghi bằng bút khác màu).

**Mục lục**
- [B0 · Nhật ký lần chạy vòng 1 (suốt khối)](#b0)
- [B1 · Câu 2.1 · Lần chạy đầu tiên, cổng tự chặn hay người duyệt · phút 65–71](#b1)
- [B2 · Câu 2.2 · Bảng soát lỗi `T-002@55` · phút 71–75](#b2)
- [B3 · Câu 2.3 · Bản đồ dữ liệu và ví dụ drift · phút 65–75](#b3)
- [B4 · Câu 2.4 · HAZOP vòng 1 · phút 65–75](#b4)
- [B5 · Câu 2.4 · Checklist 9 nhóm việc, lần 1 · phút 70–75](#b5)
- [B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa · phút 75–85](#b6)
- [B7 · Câu 2.6–2.10 · Cổng phòng ngừa, runbook phần 1–3, giờ cao điểm · phút 85–105](#b7)
- [B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 · phút 105–115](#b8)

---

<a id="b0"></a>

## B0 · Nhật ký lần chạy vòng 1

*Yêu cầu: ít nhất 3 lần chạy, mỗi lần đổi một thứ, có mã lần chạy và khoảng tin cậy.* Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi
một dòng vào `runs/journal.jsonl`. Việc của bàn là điền cột "Đổi MỘT thứ gì" (tham số `--note`) và cột "Kết luận".
Mọi con số trong quyết định Gate 1 phải trỏ về một dòng ở đây hoặc ở Phiếu C mục C0.

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | base · base | (baseline, chưa có cổng) | | | | | |
| 2 | | base · after | (cổng vòng 1, thử trước khi chốt) | | | | | |
| 3 | | base · prepared | (cổng vòng 1 đã chốt) | | | | | |
| 4 | | | | | | | | |

---

<a id="b1"></a>

## B1 · Câu 2.1 · Lần chạy đánh giá đầu tiên

```bash
python3 -m lab10.eval --suite base --stage base --note "baseline"
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

- Mã lần chạy: `__________` (ghi cả vào B0 dòng 1)
- Ngưỡng đã ký nào `[CHƯA]` đạt: …
- Khối "kinh doanh và vận hành" ở cuối output: dòng nào đáng lo? …
- Khối "theo kho và hãng": kho hoặc hãng nào có số xấu nhất? …

**Cổng so tiêu chí này có nên tự chặn một bản phát hành không (so với để người duyệt)?**

| Lý lẽ ủng hộ tự chặn | Lý lẽ phản đối |
|---|---|
| | |

Khuyến nghị (khoanh một): **tự chặn · người duyệt · kết hợp**. Vì: …

---

<a id="b2"></a>

## B2 · Câu 2.2 · Bảng soát lỗi cho `T-002@55`

```bash
python3 -m lab10.trace --suite base --ticket T-002 --seed 55
```

**Cách làm, giữ nguyên ba phần:** (1) ghi lại từng lỗi bằng **cái người ta thực sự thấy**, ai gặp, mức hệ trọng,
và xếp vào một trong ba **loại lỗi**; (2) đưa lỗi qua bộ câu hỏi để tìm **nguồn**; (3) viết **hướng xử lý**: vì sao người ta coi
đó là lỗi, người ta đi tiếp bằng đường nào, hệ thống học được gì.

Ba loại lỗi:
- **Giới hạn của hệ thống**: hệ thống không thể trả lời đúng, hoặc không trả lời được, vì giới hạn vốn có.
- **Lỗi ngữ cảnh**: hệ thống "chạy đúng thiết kế" nhưng người dùng thấy sai, vì hành động không được giải thích, trái với hình dung của họ, hoặc dựa trên giả định kém.
- **Lỗi chìm**: hệ thống chạy sai mà **cả người dùng lẫn hệ thống đều không nhận ra**. Với một trợ lý có quyền ghi sổ, đây là loại nguy hiểm nhất: người chịu hại thường là bên thứ ba.

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 |
|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 |
|---|---|---|
| Vì sao người gặp coi đây là lỗi | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | |

**Ví dụ (bộ nền, đừng chép):** `T-002@55` · sổ cái có dòng hoàn 20.000đ, hãng VNX nhận một lỗi, trong khi tracking ghi trễ 2 ngày ·
khách không thấy gì sai, hãng chịu · cao · **lỗi chìm**. Nguồn: đầu vào (đặt sai trọng số cho con số khách tự khai). Xử lý:
hãng coi là lỗi vì sổ giao của họ ghi 2 ngày; kiểu giải pháp: trao quyền cho người (số khai khác tracking thì chuyển người duyệt);
tín hiệu: đếm sự kiện `model_override` mỗi ngày.

---

<a id="b3"></a>

## B3 · Câu 2.3 · Bản đồ dữ liệu của trợ lý và ví dụ drift

**Cách làm:** đi từ người dùng và việc họ cần làm, tới đầu ra của hệ thống, rồi mới hỏi hệ thống cần dữ liệu
gì, định dạng ra sao, và **thế giới thật làm dữ liệu đó lệch đi thế nào**; cuối cùng tóm lại trong vài câu.
Trợ lý LogiX không huấn luyện gì trong lab này, nên ta hỏi về "dữ liệu trợ lý đọc lúc chạy / trường then chốt / nguồn sự thật".
Gợi ý: mở `data/world.json` phần `policies`, `orders[].parcels`, `ops_limits`, `ops_facts`.

| Mục | Điền cho trợ lý hoàn tiền |
|---|---|
| Người dùng | |
| Việc người dùng cần làm xong | |
| Đầu ra của hệ thống (kể cả các lệnh ghi) | |
| Dữ liệu trợ lý đọc lúc chạy (bảng nào trong `data/world.json`) | |
| Trường then chốt quyết định tiền và lỗi hãng | |
| Với mỗi trường then chốt: **nguồn sự thật** hay **bản sao** (ai cập nhật, khi nào)? | |
| Định dạng cần để ý (ngày, trường được phép trống, đơn nhiều kiện) | |
| Thế giới thật làm dữ liệu lệch ở đâu (theo mùa, đổi chính sách, giờ cao điểm, người nhập tay)? | |
| Câu người ngoài sẽ hỏi về nguồn dữ liệu ("sao hệ thống biết đơn trễ mấy ngày?") | |

**Tóm lại (điền vào chỗ trống):**
Trợ lý dùng `__________`, `__________`, `__________` để giúp `__________` làm được `__________`.
Trường mà nếu sai thì tiền hoặc lỗi hãng sai theo: `__________`, `__________`.
Chúng tôi biết thế giới thật sẽ làm dữ liệu lệch ở: `__________`. Dấu hiệu nhìn thấy sớm nhất: `__________`.

**Ví dụ drift trong 3 tháng tới** (lấy từ dòng "thế giới thật làm dữ liệu lệch"): cái gì đổi `____` · đổi ngày nào `____` ·
trường nào cho thấy `____` · con số nào của Bản tiêu chí bị ảnh hưởng `____`.
Đây là đầu vào đổi hay quan hệ vào–ra đổi? Chỉ số nào sẽ phát hiện? `__________`

**Ví dụ một dòng (đừng chép):** trường then chốt `parcels[].delivered_date` · bản ghi do máy quét ở điểm phát tạo ra, là nguồn
sự thật về ngày giao · lệch khi điểm phát quét sót hoặc nhập bù bằng tay.

---

<a id="b4"></a>

## B4 · Câu 2.4 · HAZOP vòng 1 trên tool của agent

*Chỉ làm MỘT vòng, trên MỘT tool. Đây là HAZOP vòng 1; HAZOP của thẻ sự cố viết riêng ở Phiếu C mục C4, không ghi đè bảng này.*

**Khung tư duy.** HAZOP không hỏi "cái gì có thể hỏng" một cách chung chung. Nó cầm từng **từ gợi ý** áp vào từng **dòng dữ
liệu đi vào một hành động** và hỏi: nếu dòng này lệch theo kiểu đó thì hậu quả là gì, ai chịu. Mục tiêu là tìm ra những nhánh
mà cả bàn chưa nghĩ tới, không phải tả lại nhánh đã biết.

| Guideword | Nghĩa khi áp vào một tool của agent |
|---|---|
| **WRONG** | Giá trị đưa vào có đủ, hợp lệ về hình thức, nhưng sai sự thật |
| **INVALID** | Giá trị không còn hiệu lực: hết hạn, sai phiên bản, sai đối tượng |
| **INCOMPLETE** | Thiếu một phần thông tin cần có để quyết định |
| **PERTURBED** | Đầu vào bị ai đó cố ý hoặc vô tình làm lệch (cài câu lệnh, gửi lặp) |
| **INCAPABLE** | Thành phần không trả lời được: quá tải, lỗi, hết quota |

**Câu hỏi dẫn dắt:** tool nào tạo ra hậu quả không đảo ngược? Mỗi tham số của tool đó lấy từ đâu (ticket, DB, model tự suy)?
Với mỗi guideword: hậu quả cho ai, hiện có gì ngăn, cần thêm gate ở tầng nào (phát hiện / chặn / giới hạn thiệt hại)?

Tool chọn phân tích: `file_carrier_fault` và `notify_carrier` (lệnh ghi gây tác động tới hãng / bên thứ ba)

| Tham số / dòng dữ liệu | Guideword | Lệch cụ thể (viết bằng dữ kiện của lab) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `file_carrier_fault`: `carrier_id`, `delay_days`, nguyên nhân tracking | WRONG | Ticket đổ lỗi cho hãng ở `O-1007-P1`, nhưng tracking ghi `delay_cause=MERCHANT_HANDOVER`; nguyên nhân này không nằm trong `fault_causes` của policy REFUND-v3 đang hiệu lực ngày `2026-11-16`. | Ghi lỗi oan cho LGX; hãng/tài xế có thể bị phạt hoặc mất uy tín dù dữ liệu nguồn quy nguyên nhân cho khâu bàn giao của shop. | Hiện `config/operating_gates.json` chưa bật `carrier_fault_requires_recorded_cause`; tool ghi đúng tham số model đưa vào. | Bật `legal.carrier_fault_requires_recorded_cause=true`; trong `write_gate`, lấy kiện theo `order_id+parcel_id`, tính ngày từ tracking và nguyên nhân từ DB/chính sách hiệu lực; nếu lệch thì chặn/chuyển người (chặn). |
| `file_carrier_fault`: chính sách áp dụng cho ngày xử lý | INVALID | Dùng REFUND-v4 trước `effective_from=2026-12-01` trong khi `as_of=2026-11-16`; v4 chỉ cho ghi lỗi nguyên nhân `CARRIER`, còn v3 đang hiệu lực cho phép nguyên nhân `CARRIER` và `FORCE_MAJEURE`. | Hãng bị áp sai quy tắc; khách và LogiX nhận quyết định không nhất quán. | `effective_policy` có thể chọn policy theo `as_of`, nhưng tool tự nó không xác thực policy_id/phiên bản từ model. | `pre_guard` ghim `policy_id` theo `effective_policy(ctx.tools.lookup_policies(), ctx.as_of)`; `write_gate` từ chối khi policy/đầu vào không cùng phiên bản (chặn). |
| `file_carrier_fault`: `parcel_id` và `delay_cause` | INCOMPLETE | `O-1010-P1` và `O-1012-P1` có `delay_cause=null`; không có nguyên nhân ghi nhận để quy lỗi. | Hãng bị ghi lỗi không có chứng cứ; đội đối soát phải gỡ lỗi và xử lý khiếu nại. | Hiện cổng `carrier_fault_requires_recorded_cause=false`; nếu thiếu kiện, kiểm tra bổ sung trong tool chỉ trả None khi không tìm thấy parcel. | Bật `legal.carrier_fault_requires_recorded_cause=true`; thiếu cause hoặc parcel thì không ghi lỗi, tạo hàng chờ người đối soát (chặn/giới hạn thiệt hại). |
| `notify_carrier`: `payload` lấy từ nội dung ticket / model | PERTURBED | Khách chèn tên, số điện thoại hoặc địa chỉ của người nhận quà vào chữ tự do; model chép nguyên văn vào payload gửi hãng. Ví dụ đơn quà `O-1024` có người nhận khác chủ tài khoản. | Dữ liệu cá nhân của khách/người nhận quà rời LogiX tới bên thứ ba không cần thiết; người nhận chịu ảnh hưởng và LogiX phải xử lý sự cố dữ liệu. | Chưa có danh sách chặn: `pii_fields_blocked_to_third_party=[]`; tool chỉ loại trường nếu cấu hình có tên trường, không quét PII nằm trong đoạn văn tự do. | Đặt `legal.pii_fields_blocked_to_third_party` gồm `name`, `phone`, `street`, `recipient`; chỉ dựng payload từ allowlist chính sách (`order_id`, `parcel_id`, `district`, `delay_days`), không chép văn bản ticket; chặn/gỡ trường nhạy cảm trước khi gửi. |

Không bắt buộc điền đủ năm dòng. Bắt buộc: **ít nhất ba dòng, trong đó một dòng là nhánh bàn chưa thấy trên trace**.

**Mở rộng ra ngoài kỹ thuật (thêm ít nhất hai dòng):** "thành phần" không chỉ là model và tool. Áp cùng năm từ gợi ý vào:

| Thành phần ngoài code | Ví dụ câu hỏi |
|---|---|
| **Người duyệt** (vận hành) | INCAPABLE: chỉ một người trực mà 14 ca tới trong một giờ thì ca cuối chờ bao lâu? |
| **Ngân sách** (kinh doanh) | WRONG: tổng hoàn tự động trong ngày vượt mức Finance cho phép mà không ai được báo thì sao? |
| **Phạm vi pilot** (kinh doanh) | INVALID: có nhóm ticket nào trợ lý luôn phải chuyển người, tức là tự động hoá vô nghĩa? |
| **Dữ liệu gửi bên thứ ba** (pháp lý) | PERTURBED: chữ khách tự gõ có tên, số điện thoại người khác bị chép sang hãng thì ai chịu? |

| Thành phần | Guideword | Lệch cụ thể | Hậu quả, cho ai | Cổng đề xuất: code hay con số nào trong `config/operating_gates.json` |
|---|---|---|---|---|
| Người duyệt vận hành | INCAPABLE | Theo `ops_facts`, mặc định 1 người duyệt được 6 ca/giờ; giờ cao điểm dồn 14 ca/giờ thì 8 ca vượt công suất trong giờ đó, SLA nhận xử lý là 60 phút. | Khách chờ quá SLA; nhân viên quá tải có thể duyệt vội hoặc bỏ sót khiếu nại của hãng. | `operations.reviewers_on_shift=1`; `review_capacity_per_hour` và `max_queue_wait_minutes` hiện null, chưa có ngưỡng ùn. | Đặt `operations.reviewers_on_shift` theo lịch trực, `review_capacity_per_hour=6` mỗi người, `max_queue_wait_minutes=60`; khi hàng chờ vượt công suất gọi người dự phòng/thu hẹp pilot, quá SLA thì tạm ngừng lệnh ghi cần duyệt. |
| Ngân sách Finance | WRONG | Nhầm trần hoàn tự động 2.000.000đ/ngày trong `ops_limits` với tổng mọi khoản hoàn; hoặc ngưỡng bị cấu hình cao hơn trần Finance. | LogiX vượt ngân sách và không còn tiền cho ca cần xử lý; Finance chịu chi phí ngoài kế hoạch. | `business.daily_refund_cap_vnd=null`; tool chưa áp cổng cap nếu chưa đặt giá trị. | Đặt `business.daily_refund_cap_vnd=2000000` theo `ops_limits.daily_auto_refund_budget_vnd`; theo dõi tổng hoàn tự động trong ngày và chuyển người khi chạm trần (giới hạn thiệt hại). |

**Ví dụ mẫu (`issue_refund`, đừng chép):** tham số `amount_vnd` · WRONG · số tiền tính từ số ngày khách tự khai · LogiX mất
tiền, hãng bị kéo theo một lỗi · hiện chỉ có trần "không vượt tổng tiền đơn" · cổng ghi so với quyền lợi tính từ DB (chặn).

---

<a id="b5"></a>

## B5 · Câu 2.4 · Checklist go-live 9 nhóm việc, lần 1

Checklist chín nhóm việc phải xong trước khi chạy thử thật. Bàn điền lần đầu ở đây, rồi cập nhật sau sự cố ở Phiếu C mục C11.
Cột "Bằng chứng lấy từ đâu" trỏ tới mục bàn đã điền ở bước khác; không điền thêm phiếu nào chỉ để lấp cột này.

Trạng thái: **Xong** (có bằng chứng) · **Chưa** · **Không áp dụng** (ghi lý do). Bằng chứng là **mã lần chạy**, tên file / mục phiếu, hoặc số trong report.
**Cột PIC bắt buộc:** mỗi dòng một người có tên (không ghi "cả bàn"). Dòng nào chưa có PIC thì coi như Chưa.

| # | Nhóm việc | Bằng chứng lấy từ đâu (đã có sẵn trong lab) | Mục cần kiểm tra | Trạng thái | Bằng chứng | PIC |
|---|---|---|---|---|---|---|
| 1 | Chất lượng | Report `lab10.eval` (mã lần chạy) + bảng soát lỗi (Phiếu B mục B2) | | | | |
| 2 | Dữ liệu | Bản đồ dữ liệu (Phiếu B mục B3, câu 2.3): trường nào là nguồn sự thật, trường nào là bản sao | | | | |
| 3 | Bảo mật | Một vòng HAZOP với guideword PERTURBED (Phiếu B mục B4): chữ nào đi vào model mà không do LogiX viết | | | | |
| 4 | Quyền hạn | `config/switches.json` + guard trước lệnh ghi; thẻ S2, S8 có thêm mục mức kiểm soát (Phiếu C mục C3) | | | | |
| 5 | Hiệu năng, hạ tầng | Đội tự ước tính; HAZOP guideword INCAPABLE: LLM không trả lời thì sao; số người duyệt và số ca mỗi giờ | | | | |
| 6 | Chi phí | Khối "kinh doanh và vận hành" của report: chi phí mỗi ticket so với làm tay, ROI, tiền LLM ticket đắt nhất; `config/operating_gates.json` mục `business` | | | | |
| 7 | Vận hành | Runbook (Phiếu B mục B7.5–B7.6) + `config/operating_gates.json` mục `operations` (PIC, người duyệt, số người trực, điều kiện dừng, kênh báo tin) + metric trong `monitors.py` | | | | |
| 8 | Con người, pháp lý | Bên thứ ba (hãng, tài xế, shop, người nhận quà, người đứng tên duyệt); `config/operating_gates.json` mục `legal`; thẻ S6, S7, S8 có mục riêng ở Phiếu C mục C3 | | | | |
| 9 | Quyết định | Câu tiêu chí (Phiếu A mục A4) + hash Bản tiêu chí đã ký + quyết định Gate 1 (Phiếu B mục B8, Phiếu C mục C12) | | | | |

Ô "Chưa" có rủi ro cao → chuyển thành một dòng Risk register (Phiếu C mục C10).

---

<a id="b6"></a>

## B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa (khoảng 8–10 phút, cả bàn)

*Mọi bàn làm pre-mortem ở vòng 1, TRƯỚC khi biết sự cố, để chọn 2–3 cổng phòng ngừa sẽ dựng. Ở vòng 2 bàn mở lại phần này ở
Phiếu C mục C1 (bút khác màu).*

**Khung tư duy.** Hỏi "có rủi ro gì không" thì ai cũng dè dặt. Nói "nó đã hỏng rồi, vì sao" thì mọi người được phép nói ra
điều mình vẫn lo. Làm im lặng trước, đọc sau, để ý kiến của người nói to không lấn át.

**Đề bài (đọc to):** *"Ba tháng sau pilot, LogiX phải tắt trợ lý hoàn tiền ở cả hai depot. Chuyện gì đã xảy ra?"*

1. **2 phút, im lặng:** mỗi người viết 2 lý do, mỗi lý do một dòng.
2. **2 phút:** đọc vòng tròn, mỗi lượt một lý do, không bình luận. Gộp lý do trùng.
3. **2 phút:** xếp từng lý do vào một **lăng kính**. Lăng kính nào còn trống thì cả bàn viết thêm ít nhất một lý do cho nó.
4. **2 phút:** chọn 2–3 lý do sẽ biến thành **cổng phòng ngừa** ngay hôm nay (code trong `guards.py` hoặc con số trong
   `config/operating_gates.json`). Lý do còn lại → Risk register.

Bốn lăng kính (bắt buộc đủ cả bốn; dự án AI hay chết ở ba lăng kính sau hơn là ở lăng kính đầu):

| Lăng kính | Câu hỏi gợi ý trên LogiX |
|---|---|
| **Kỹ thuật** | Model tin nhầm cái gì? Dữ liệu nào thiếu, cũ, lệch? Lệnh ghi nào không đảo ngược được? |
| **Kinh doanh** | Mỗi ticket tốn bao nhiêu so với làm tay? Một ngày hoàn tối đa bao nhiêu? Nhóm ticket nào không thể có lời? |
| **Con người và vận hành** | Ai duyệt, mấy người, mỗi giờ được mấy ca? Lượng việc tăng gấp ba thì sao? Nhân viên có tin trợ lý không? |
| **Pháp lý** | Dữ liệu cá nhân của ai rời hệ thống? Bên thứ ba nào bị ghi lỗi, bị trừ tiền mà không được hỏi? |

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được hôm nay? (trace / data / config nào) | Thành cổng phòng ngừa nào (code hay config) / hay vào risk register |
|---|---|---|---|
| | Kỹ thuật | | |
| | Kinh doanh | | |
| | Con người và vận hành | | |
| | Pháp lý | | |
| | | | |

---

<a id="b7"></a>

## B7 · Khối 2B · Cổng phòng ngừa (phút 85–105)

### B7.1 · Câu 2.6 · 2–3 cổng phòng ngừa trong `lab10/guards.py`

Mỗi cổng ứng với một dòng pre-mortem (B6) hoặc một dòng HAZOP (B4). Viết trong `pre_guard(ctx)` (trước khi trợ lý đọc ticket)
hoặc `write_gate(ctx, action)` (trước mỗi lệnh ghi). Thử bằng:

```bash
python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."
python3 -m unittest discover -s tests
```

| # | Cổng (hàm và nhánh, ví dụ `write_gate` khi `tool == "issue_refund"`) | Ứng với dòng nào ở B6 / B4 | Chặn điều gì, dựa vào nguồn sự thật nào | Mã lần chạy `base · after` | Ca đang đúng nào bị hỏng? (phải là "không") |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### B7.2 · Câu 2.7 · Hai bước tránh rò rỉ dữ liệu

Bàn đang chỉnh cổng tới khi 22 ticket bộ nền xanh hết. Nêu 2 bước cụ thể để không "chỉnh trên chính bộ dùng để chấm"
(gắn với bộ nền, gói sự cố, bài kiểm tra ẩn):

1. …
2. …

### B7.3 · Câu 2.8 · Một behavioral test

- Tính chất (một câu): …

```bash
python3 -m lab10.trace --suite base --stage after --adhoc "..." --order O-10xx --customer C-xx
```

| Ticket hiểm | Nội dung ticket (`--adhoc`) | `--order` · `--customer` | Kết quả (dán dòng `SỔ CÁI` / `LỖI HÃNG` / `GỬI HÃNG`) | Tính chất giữ được? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

Giữ hai ticket này cho phần demo.

### B7.4 · Câu 2.9 · Cổng kinh doanh (`config/operating_gates.json` mục `business`)

Mỗi con số kèm một câu lý do, lấy từ `data/world.json` → `ops_limits`, `ops_facts`.

| Khoá | Giá trị bàn đặt | Lý do (một câu, có số) |
|---|---|---|
| `business.daily_refund_cap_vnd` | | |
| `business.cost_budget_per_ticket_vnd` | | |
| `business.pilot_scope` (all / warehouse / percent) | | |
| `business.roi_min` | | |

### B7.5 · Câu 2.10 · Cổng con người, vận hành, pháp lý + Runbook phần 1–3

Điền `config/operating_gates.json` mục `operations` và `legal` (PIC, người duyệt, số người trực mỗi ca, công suất duyệt mỗi giờ,
thời gian chờ tối đa, điều kiện dừng, kênh báo tin; trường dữ liệu cá nhân không gửi cho bên thứ ba; ghi lỗi cho hãng phải có
nguyên nhân trong tracking). Rồi viết runbook dưới đây **khớp với các con số đó**.

*Runbook là tờ giấy người trực ca cầm lúc 23h khi có chuyện. Nó trả lời: nhìn con số nào, ngưỡng nào thì làm gì, ai được quyết.
Phần 1–3 và mục Giờ cao điểm viết ở vòng 1. Phần 4–5 viết ở vòng 2 (Phiếu C mục C11). Mọi con số phải khớp `config/operating_gates.json` và report.*
*Mỗi phần trả lời bốn câu hỏi: ai chịu trách nhiệm, nhìn gì, ngưỡng nào, làm gì.* **Người viết (vai Vận hành và pháp lý):** ______

#### Runbook 1 · Ai chịu trách nhiệm

**Điểm cần Ops xác nhận trước pilot:** tạo/xác nhận kênh Teams trực chung và chốt danh sách 2 người dự phòng giờ cao điểm; các tên nhân viên trong bảng dưới đây lấy từ dữ liệu lab, riêng đầu mối Pháp lý là phân công của nhóm.

| Vai | Tên / mã nhân viên (lấy từ `data/world.json` → `staff`) | Được quyền làm gì | Liên lạc qua kênh nào |
|---|---|---|---|
| PIC của trợ lý (một người) | Lê Thanh Tùng (`NV-TUNG`, giám sát vận hành) | Điều phối xử lý sự cố, thu hẹp pilot; xác nhận báo cáo và phục hồi | Teams: kênh trực pilot Ops-Pháp lý |
| Người duyệt đứng tên các khoản vượt hạn mức | Trần Thị Hạnh (`NV-HANH`, trưởng ca CSKH) | Duyệt khoản vượt hạn mức; phân công người nhận xử lý khiếu nại khách | Teams: kênh trực pilot Ops-Pháp lý |
| Người giữ công tắc tắt từng thao tác ghi | Lê Thanh Tùng (`NV-TUNG`) | Tắt/bật công tắc trong `config/switches.json`; ghi thời điểm và phạm vi | Teams: kênh trực pilot Ops-Pháp lý |
| Người nhận khiếu nại của bên thứ ba (hãng, shop, người nhận quà) | Phạm Kiều Oanh (`NV-OANH`) nhận/đối soát khiếu nại hãng và shop; Chu Thân Nhất (Pháp lý, thành viên bàn) xử lý đánh giá pháp lý/PII; NV-TUNG điều phối sự cố | Ghi nhận, bảo toàn chứng cứ, xác nhận đầu mối phản hồi; không tự kết luận trách nhiệm pháp lý | Teams: kênh trực pilot Ops-Pháp lý; khi có PII gọi trực tiếp NV-TUNG và Chu Thân Nhất |

Số người trực duyệt mỗi ca: **1** · Mỗi giờ duyệt được: **6 ca** (theo `ops_facts`) · Phạm vi pilot: theo `business.pilot_scope`; khi tăng tải chỉ thu hẹp, không tự mở rộng.

#### Runbook 2 · Nhìn con số nào, ngưỡng nào thì làm gì

Mỗi dòng một tín hiệu. Cột "Lấy ở đâu" phải là một dòng trong report của `lab10.eval` / `lab10.grade` hoặc một chỉ số trong `lab10/monitors.py`.

| Tín hiệu | Lấy ở đâu | Bình thường | Ngưỡng VÀNG → việc làm | Ngưỡng ĐỎ → việc làm | Ai quyết |
|---|---|---|---|---|---|
| Thời gian chờ người duyệt lâu nhất | Report eval: queue wait | <30 phút | ≥30 phút: NV-TUNG gọi dự phòng; ưu tiên ca nhận trước | ≥60 phút: thu hẹp pilot/tắt thao tác ghi liên quan, CSKH nhận chờ | NV-TUNG |
| Số ca bị ùn | Report eval: hàng chờ; công suất 6 ca/giờ | ≤6 ca/giờ | >6 ca/giờ: gọi dự phòng, ngừng nhận ticket ngoài phạm vi | Nếu không có dự phòng hoặc chờ đạt 60 phút: thu hẹp/tắt | NV-TUNG |
| Chi phí mỗi ticket so với làm tay | Khối kinh doanh-vận hành trong report | ≤10.000đ (chi phí làm tay mock) | Vượt 10.000đ: xem lại tải duyệt/chi phí máy | Vượt ngân sách/ticket đã đặt: thu hẹp, xin Finance duyệt | NV-TUNG + PO |
| Tổng tiền hoàn tự động trong ngày so với trần | Report: tổng hoàn tự động / `daily_refund_cap_vnd` | Dưới 80% trần | Đạt 80%: báo NV-HANH, chuyển ca nhạy cảm sang duyệt | Đạt trần: dừng hoàn tự động; ngoại lệ do NV-HANH duyệt | NV-HANH |
| Tiền hoàn sai | Report: wrongful refund / tiêu chí đã ký | 0đ | Bất kỳ >0: báo NV-HANH, NV-TUNG; rà soát hồ sơ liên quan | Dừng `issue_refund`, mở sự cố và đối soát | NV-TUNG tắt; NV-HANH xử lý |
| Lỗi ghi oan cho hãng / lộ dữ liệu cá nhân (pháp lý) | Nhật ký `file_carrier_fault`/`notify_carrier`; khiếu nại 48h | 0 vụ | Có phản ánh: giữ log, báo NV-OANH và Chu Thân Nhất | 1 lỗi oan: tắt `file_carrier_fault`; 1 lộ PII: tắt `notify_carrier` | NV-TUNG tắt; NV-OANH đối soát; Chu Thân Nhất rà soát |
| (tín hiệu riêng của bàn) | Khiếu nại hãng phản đối phiếu lỗi trong 48h | 0 phản đối | 1 phản đối: NV-OANH so tracking/hợp đồng, tạm giữ phiếu liên quan | 2 phản đối/ca hoặc xác nhận ghi oan: tắt `file_carrier_fault`, rà soát cùng nguyên nhân | NV-TUNG + NV-OANH |

#### Runbook 3 · Điều kiện dừng và cách dừng

- **Dừng một phần:** 1 lần lộ PII thì tắt `notify_carrier`; 1 lần ghi lỗi oan/không có nguyên nhân tracking thì tắt `file_carrier_fault`; hàng chờ vượt năng lực 6 ca/giờ hoặc chạm SLA 60 phút thì NV-TUNG thu hẹp `business.pilot_scope` và tạm dừng thao tác ghi cần duyệt.
- **Dừng hẳn:** lỗi không cô lập được, nhiều hồ sơ PII bị ảnh hưởng, hoặc Ops/Pháp lý xác định không thể xử lý an toàn.
- **Cách dừng:** (1) NV-TUNG đổi công tắc tương ứng trong `config/switches.json` sang `off`; (2) báo kênh Teams và gọi CSKH nhận ticket chờ; (3) ghi giờ, mã ticket, phạm vi ảnh hưởng vào nhật ký sự cố; (4) không đưa dữ liệu cá nhân vào kênh chung.
- Từ tín hiệu đỏ đến lúc dừng xong tối đa **5 phút**; người bấm: **Lê Thanh Tùng (`NV-TUNG`)**, dự phòng **Trần Thị Hạnh (`NV-HANH`)**.
- Ticket đang chờ chuyển về hàng CSKH; NV-HANH phân công người duyệt, NV-OANH nhận khiếu nại hãng/shop, Chu Thân Nhất đánh giá pháp lý khi có PII hoặc tranh chấp.
- Chỉ bật lại sau khi khoanh vùng nguyên nhân, bảo toàn chứng cứ, khắc phục và kiểm tra hồi quy; cần NV-TUNG xác nhận vận hành, Chu Thân Nhất xác nhận nếu có vấn đề pháp lý, NV-HANH xác nhận năng lực tiếp nhận. Ghi quyết định và thời điểm bật lại.

### B7.6 · Giờ cao điểm (bắt buộc với thẻ S4; các thẻ khác nên có)

Lượng ticket có thể dồn gấp ba trong một giờ (ngày sale, sau bão). Viết trước, khi chưa biết sự cố.

| Câu hỏi | Trả lời (có số, có tên) |
|---|---|
| Giờ cao điểm là khi nào, bao nhiêu ticket mỗi giờ (dựa vào `ops_facts`)? | Ngày sale/ngày sau gián đoạn; HAZOP dùng 14 ticket/giờ làm kịch bản stress-test, cần thay bằng telemetry pilot. |
| Ai trực giờ cao điểm, mấy người (khớp `operations.reviewers_on_shift`)? | Ca thường 1 người duyệt (6 ca/giờ). NV-TUNG gọi 2 người dự phòng thuộc CSKH/Ops ở kịch bản 14 ca/giờ; xác nhận danh sách trực trước pilot. |
| Ngưỡng nào thì **gọi thêm người** (hàng chờ bao nhiêu ca, chờ lâu nhất bao nhiêu phút)? Ai gọi? | NV-TUNG gọi 2 người dự phòng khi tải dự báo >6 ca/giờ hoặc hàng chờ ≥6; gọi ngay ở kịch bản 14 ca/giờ. Chờ ≥30 phút báo động, chạm 60 phút thì dừng/thu hẹp. |
| Ngưỡng nào thì **thu hẹp** phạm vi (khoá `business.pilot_scope`) hoặc **tắt** một thao tác ghi (`config/switches.json`)? Ai quyết? | Không xác nhận được người dự phòng trước cao điểm hoặc chờ chạm 60 phút: NV-TUNG thu hẹp; có PII thì tắt `notify_carrier`, có ghi lỗi oan thì tắt `file_carrier_fault`. |
| Thêm người thì chi phí mỗi ticket và ROI thay đổi thế nào (đọc report)? | Mỗi người trực thêm 30.000đ/ca theo `ops_facts`; 2 người dự phòng tăng 60.000đ/ca. Dùng report pilot tính chi phí/ticket và ROI; chưa tự giả định ROI. |

---

<a id="b8"></a>

## B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 (phút 105–115)

Làm đúng thứ tự:

```bash
python3 -m lab10.checkpoint
python3 -m lab10.eval --suite base --stage prepared
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

**Khung tư duy.** Gate 1 "đạt" khi **quyết định khớp bằng chứng và khớp tiêu chí đã ký trước**. Tiếp tục, Thu hẹp, Cải tiến
thêm, Dừng đều có thể là quyết định đạt. Quyết định không đạt là quyết định mà con số trong report không đỡ được.
Chỉ chọn Tiếp tục khi mọi chỉ số bắt buộc đều đạt.

Ba câu tự vấn trước khi viết: (1) Rủi ro còn lại có chấp nhận được như hiện trạng không? (2) Cần thêm biện pháp nào, tốn
bao nhiêu thời gian? (3) Có phần nào của dự án không nên làm tiếp?

| | **v1** (phút 105–115, TRƯỚC khi nhận thẻ sự cố) |
|---|---|
| Commit ký tiêu chí (message `Sign acceptance criteria`; hash commit, tuỳ chọn) | |
| Hash chốt cổng vòng 1 (8 ký tự lệnh `lab10.checkpoint` in ra, tuỳ chọn) | |
| Mã lần chạy dùng làm bằng chứng | bộ nền, mốc base: ________ · bộ nền với cổng vòng 1 (prepared): ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Đọc khối "theo kho và hãng" ở cuối output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt phần nào, vì sao | |
| Nếu Cải tiến thêm: giả thuyết cụ thể + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Một bằng chứng còn thiếu (thứ bộ nền chưa đo được) | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

Xong v1 thì lưu và đẩy một bản (sau mốc này không sửa cột v1):

```bash
git add lab10/guards.py lab10/guards_round1.py config/operating_gates.json config/operating_gates.round1.json config/round1.lock templates/form-b-evaluation-gates.md
git commit -m "LAB 10: chốt cổng vòng 1, quyết định v1"
git push -u origin main
```
