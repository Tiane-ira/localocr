import argparse
import json

from rapidocr_onnxruntime import RapidOCR

if __name__ == '__main__':
    ocr = {}
    try:
        engine = RapidOCR()
        parser = argparse.ArgumentParser(description="A ocr tool for rapid ocr")
        parser.add_argument("-p", type=str, required=True, help="the path of the image")
        args = parser.parse_args()
        img_path = args.p
        results, elapse = engine(img_path)
        result_str = ""
        for e in results:
            if len(e) > 2:
                result_str += f"{e[1]}\n"
        ocr["result"] = result_str
    except Exception as e:
        ocr["err"] = str(e)
    print(json.dumps(ocr, ensure_ascii=False))
