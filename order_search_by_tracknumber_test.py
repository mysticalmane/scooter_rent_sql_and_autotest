# Александр Костин, 15-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request

# test 1
def test_finding_order_by_track_is_possible():
    response = sender_stand_request.get_order_by_tracknumber()
    assert response.status_code == 200

