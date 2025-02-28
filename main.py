from flask import Flask, request, jsonify

app = Flask(__name__)

# الصفحة الرئيسية لاختبار تشغيل API
@app.route("/")
def home():
    return "🚀 API شغالة بنجاح! استخدم /generate_zafa لإنشاء الزفات."

# مسار توليد الزفة
@app.route("/generate_zafa", methods=["POST"])
def generate_zafa():
    data = request.json
    bride_name = data.get("bride_name", "العروسة")
    groom_name = data.get("groom_name", "العريس")
    music_style = data.get("style", "khaleeji")
    singer = data.get("singer", "nour_al_rifai")
    text_type = data.get("text_type", "default")

    # توليد نص الزفة بناءً على الاختيار
    if text_type == "modern":
        zafa_text = f"ليلة العمر تجمع {bride_name} و {groom_name} في أجمل الأوقات."
    elif text_type == "classic":
        zafa_text = f"بالحب والفرح، نزف أجمل التهاني لـ {bride_name} و {groom_name}."
    elif text_type == "ai_generated":
        zafa_text = f"زفة خاصة: ليلة رائعة ومميزة لـ {bride_name} و {groom_name}."
    else:
        zafa_text = f"مبروك للعروس {bride_name} والعريس {groom_name}، ليلة سعيدة!"

    response = {
        "message": "تم إنشاء الزفة!",
        "text": zafa_text,
        "download_url": f"https://yourstorage.com/zafat/{bride_name}_{groom_name}.mp3"
    }

    return jsonify(response)

# تشغيل Flask على المنفذ 10000 (لـ Render)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
