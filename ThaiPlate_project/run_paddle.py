import cv2, glob
import easyocr
from paddleocr import PaddleOCR

easy = easyocr.Reader(['th', 'en'])
paddle = PaddleOCR(
    lang='th',
    enable_mkldnn=False,                 # ปิด oneDNN แก้ error นี้
    use_doc_orientation_classify=False,  # ป้ายครอปแล้ว ไม่ต้องหมุนเอกสาร
    use_doc_unwarping=False,             # ไม่ต้องดัดภาพเอกสาร
    use_textline_orientation=False,
)

def paddle_read(path):
    if hasattr(paddle, 'predict'):           # PaddleOCR 3.x
        res = paddle.predict(path)
        return " ".join(res[0]['rec_texts'])
    res = paddle.ocr(path)                   # PaddleOCR 2.x
    return " ".join(line[1][0] for line in (res[0] or []))

for p in sorted(glob.glob('example/*.jpg')):   # เปลี่ยนตรงนี้
    e = " ".join(t for _, t, _ in easy.readtext(cv2.imread(p)))
    print(p, '| easyocr:', e, '| paddle:', paddle_read(p))