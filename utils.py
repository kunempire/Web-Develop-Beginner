# functions to implement
def AIGC_text_detect(text):
    return 0.9999, 'Human'

def AIGC_image_detect(image_path):
    return 0.6666, 1

def picture_tampering_detect(image_path):
    return 1, './function/picture_tampering_detect/mask_results/test_img.png'

# main utils for UI design
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import base64
import cv2
import markdown2
import re

def save_base64_image(base64_data, save_path):
    try:
        image_data = base64.b64decode(base64_data)
        with open(save_path, 'wb') as f:
            f.write(image_data)
        return True
    
    except Exception as e:
        print(f"Error saving image: {e}")
        return False

def encode_image_to_base64(image_path):
    try:
        # 以二进制形式打开图片文件
        with open(image_path, "rb") as image_file:
            # 读取图片内容
            image_data = image_file.read()
            # 进行 base64 编码
            encoded_image = base64.b64encode(image_data).decode('utf-8')
            return encoded_image
    except Exception as e:
        # 处理异常，例如文件不存在等情况
        print(f"Error: {e}")
        return None

def get_tampered_part(image_path):
    label, mask_path = picture_tampering_detect(image_path)
    if mask_path != '':
        color_image = cv2.imread(image_path)
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        # 将灰度蒙版转换为二值图像
        _, binary_mask = cv2.threshold(mask, 128, 255, cv2.THRESH_BINARY)
        # 将彩色图像和二值蒙版进行按元素相乘操作
        result_image = cv2.bitwise_and(color_image, color_image, mask=binary_mask)

        # 保存输出图像
        output_path = "./function/picture_tampering_detect/temp/result_image.jpg"
        cv2.imwrite(output_path, result_image)
        return output_path

def format_image_file(image_path):
    data = encode_image_to_base64(image_path)
    _, file_extension = os.path.splitext(image_path)
    type = file_extension[1:]
    format_dic = {"type": type, "encode": 'base64', "data": data}
    return format_dic

def function_test():
    print(AIGC_text_detect('I am here to help with any questions you may have or engage in conversation on various subjects. How can I assist you today?'))
    print(AIGC_image_detect('./function/ai_picture_sample/1_ai/001987.png'))
    print(picture_tampering_detect('./function/picture_tampering_detect/sample_backup/copymove2.png'))

def parse_blog(blog_id):
    # 读取Markdown文件
    with open('./static/resource/blog'+str(blog_id)+'.md', 'r', encoding='utf-8') as file:
        md_content = file.read()
   
    html_content = markdown2.markdown(md_content) # 解析Markdown内容

    # 提取第一个一级标题作为博客名字
    pattern = re.compile(r'<h1.*?>(.*?)<\/h1>', re.DOTALL)
    match = pattern.search(html_content)
    title = match.group(1).strip()
    return title, html_content

if __name__ == '__main__':
    function_test()