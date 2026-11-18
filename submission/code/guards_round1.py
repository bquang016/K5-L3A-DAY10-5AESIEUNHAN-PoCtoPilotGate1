"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")

    # 1. Cổng phòng ngừa kiểm tra tính hợp lệ của khoản hoàn tiền (chống tin lời khách tự khai lệch tracking)
    if tool == "issue_refund":
        order_id = action.get("order_id")
        if order_id:
            order = ctx.tools.lookup_order(order_id)
            if order:
                parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
                policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
                delay = H.db_delay_days(parcel, ctx.as_of)
                entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
                
                # Không cho phép hoàn tiền vượt quá quyền lợi tính theo dữ liệu tracking thực tế
                if action.get("amount_vnd", 0) > entitled:
                    return Verdict.escalate(f"Số tiền hoàn ({action.get('amount_vnd')}đ) vượt quá mức được hưởng theo tracking ({entitled}đ)")

        # Cổng ngân sách: Chặn/chuyển duyệt khi vượt trần hoàn tự động trong ngày
        cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
        spent = ctx.tools.auto_refund_today_vnd()
        if cap is not None and spent + action.get("amount_vnd", 0) > cap:
            return Verdict.escalate("Vượt trần hoàn tiền tự động trong ngày, chuyển người duyệt")

    # 2. Cổng bảo vệ đối tác: Chặn ghi lỗi hãng oan sai khi tracking không ghi nhận lỗi hoặc chưa đủ ngày trễ
    if tool == "file_carrier_fault":
        order_id = action.get("order_id")
        if order_id:
            order = ctx.tools.lookup_order(order_id)
            if order:
                parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
                policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
                delay = H.db_delay_days(parcel, ctx.as_of)
                if not H.carrier_at_fault(policy, parcel, delay):
                    return Verdict.deny(f"Không ghi lỗi hãng vì tracking không xác nhận lỗi hoặc chưa đủ số ngày trễ (thực tế trễ {delay} ngày)")

    return Verdict.allow()
