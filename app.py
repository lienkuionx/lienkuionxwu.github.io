from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText

# 初始化 Flask 應用程式
app = Flask(__name__)
app.secret_key = "your_secret_key"  # 用於 CSRF 保護

# 定義主要頁面的路由
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/playlist")
def playlist():
    return render_template("playlist.html")

@app.route("/BIO")
def projects():
    return render_template("BIO.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # 從表單中獲取資料
        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        try:
            # 發送郵件
            send_email(name, email, subject, message)
            flash("郵件發送成功！", "success")
        except Exception as e:
            flash(f"郵件發送失敗：{str(e)}", "danger")

        return redirect(url_for("contact"))

    return render_template("contact.html")

# 發送郵件功能
def send_email(name, email, subject, message):
    # 發件人與收件人
    sender_email = "lienkuionx@gmail.com"  # 替換為你的發件人郵箱
    receiver_email = "lienkuionx@gmail.com"  # 替換為接收郵件的地址
    password = "qwms nsbg szzc fjvf"  # 替換為你的郵箱應用程式密碼

    # 構建郵件內容
    msg = MIMEText(f"姓名: {name}\n郵箱: {email}\n\n訊息:\n{message}")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # 使用 Gmail SMTP 發送郵件
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # 啟用加密
        server.login(sender_email, password)  # 登錄郵箱
        server.sendmail(sender_email, receiver_email, msg.as_string())  # 發送郵件

# 啟動應用程式
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




