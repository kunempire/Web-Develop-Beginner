from flask import Flask, request, render_template, jsonify, send_file

from utils import *

app = Flask(__name__)

app.template_folder = 'templates'

# home page
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_file('./static/resource/'+filename, as_attachment=True)

# text-distinguish page
@app.route('/function/text-distinguish', methods=['GET', 'POST'])
def text_distinguish():
    input_text = "Text here..."
    if request.method == 'POST':
        input_text = request.form['InputText']
        probability, label = AIGC_text_detect(input_text)
        probability = round(probability, 4)
        return render_template('text-distinguish.html', input_text=input_text, label=label, probability=probability)
    if request.method == 'GET':
        return render_template('text-distinguish.html', input_text=input_text)

# image-distinguish page
@app.route('/function/image-distinguish')
def image_distinguish():
    return render_template('image-distinguish.html')

@app.route('/function/image-distinguish/distinguish-image', methods=['POST'])
def distinguish_image():
    data = request.get_json()
    image_data = data.get('imageData')

    if 'data' in image_data:
        image_base64 = image_data['data']
        save_path = './function/AIGC_image_detect/temp/uploaded_image.' + image_data['type']
        if save_base64_image(image_base64, save_path):
            print(f"Image saved successfully: {save_path}")
            probability, label = AIGC_image_detect(save_path)
            probability = round(probability, 4)
            label = 'AIGC' if label == 1 else 'Human'
            return jsonify({"probability": probability, "label": label})
        else:
            return jsonify({"status": "error", "message": "Failed to save image"})
        
    else:
        return jsonify({"status": "error", "message": "Missing image data in the request"})

# tampering-detect page
@app.route('/function/tampering-detect')
def tampering_detect():
    return render_template('tampering-detect.html')

@app.route('/function/tampering-detect/detect-tampering', methods=['POST'])
def detect_tampering():
    data = request.get_json()
    image_data = data.get('imageData')

    if 'data' in image_data:
        image_base64 = image_data['data']
        save_path = './function/picture_tampering_detect/temp/uploaded_image.' + image_data['type']
        if save_base64_image(image_base64, save_path):
            print(f"Image saved successfully: {save_path}")
            result_path = get_tampered_part(save_path)
            if result_path != None:
                result_image = format_image_file(result_path)
                return jsonify(result_image)
            else:
                return jsonify({"status": "success", "message": "No detection", "code" : 2})
        else:
            return jsonify({"status": "error", "message": "Failed to save image", "code" : -2})
        
    else:
        return jsonify({"status": "error", "message": "Missing image data in the request", "code" : -1})

# about page
@app.route('/about')
def page4():
    return render_template('about.html')

# blog page
@app.route('/blog/<blog_id>')
def blog_page(blog_id):
    title, html_content = parse_blog(blog_id)

    return render_template('blog-single.html', title=title, blog_content=html_content)



if __name__ == '__main__':

    # function_test()

    # 0.0.0.0 表示允许来自任何 IP 地址的访问，否则只能本地访问
    app.run(debug=True, host='0.0.0.0', port=7890)
    