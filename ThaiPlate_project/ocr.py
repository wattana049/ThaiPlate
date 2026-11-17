import easyocr, cv2

reader = easyocr.Reader(['th', 'en'])  # ครั้งแรกจะโหลดโมเดล
img = cv2.imread('example/03img.jpg')
results = reader.readtext(img)

for bbox, text, conf in results:
    print(text, round(conf, 2))