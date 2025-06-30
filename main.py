# import requests
# from bs4 import BeautifulSoup
# import smtplib
# import os
# from dotenv import load_dotenv
# import re

# load_dotenv()


# URL = "https://www.amazon.in/Haier-Inverter-Refrigerator-HEB-333DS-P-Convertible/dp/B0BTHLGYHZ/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.58c90a12-100b-4a2f-8e15-7c06f1abe2be&dib=eyJ2IjoiMSJ9.R3t0sYDGe4YgvlPwB9OuOaSPnA4sCEwiNWz0WNwGugnPy4BHQejaTHoXRClBtokGxgAn5Tu1nDNt9TcXoH3FjMIyJ_dMCzWPcqE6HZ0hHi82_omvi0gFwchSkNPlin4JxpNVC8rHTVr5LYs1lpYYXAy5k6lp-cYoMeR4C8Lo9qUcVlBKiQaY8i-IjlnoR_CTQqpGcWNaDsJ5eSeH_TNhjQxSUIlwqpnxqguBqIXe3ua_S6PObuJJ0wkkuBGbzku3hsDsx2Z8R8-OI1IFOv5sHItGqMAwN4jJy3_DKf8gFOY.BmHq5zfQYecP75GvlbSj9l2fi-V09Qgs6pH2THFWQTo&dib_tag=se&pd_rd_r=302c0b74-153b-4f7a-8e3e-8a71b8ee78a3&pd_rd_w=yNbSa&pd_rd_wg=kXNVG&qid=1750229268&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl&th=1"
# Header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate br, zstd",
#     "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
#     "Dnt": "1",
#     "Priority": "u=1",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "Referer": "https://www.amazon.in/",
#     "Cookie": "ad-id=A_Hd57lwm08blOUlf_eZmgg; ad-privacy=0",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
# }
# response = requests.get(URL,headers = Header)
# website_html = response.content

# soup = BeautifulSoup(website_html, "html.parser")

# # price = soup.find(class_= "a-offscreen").get_text()


# # # Find the HTML element that contains the price
# price = soup.find(class_="a-offscreen").get_text()

# # # Remove the dollar sign using split
# price_without_currency = float(price.split("₹")[1].replace(",", ""))

# title = soup.find(id="productTitle").get_text().strip()


# MyMail = os.environ["mymail"]
# Password = os.environ["password"]
# SMTP_Address = os.environ["SMTP_Address"]
# SMTP_Port = int(os.environ["SMTP_Port"])

# Buy_price = 35000.00

# if price_without_currency < Buy_price:
    
#     message = f"{title} is now available for {price} \n\n Buy it now at {URL}"
#     with smtplib.SMTP(SMTP_Address, SMTP_Port) as connection:
#         connection.starttls()
#         connection.login(user=MyMail, password = Password)
#         connection.sendmail(from_addr= MyMail, 
#                             to_addrs= ["12aashish3456@gmail.com","bagmaraayush@gmail.com"],
#                             msg = f"Subject: Amazon Price Alert\n\n{message} \n\n".encode("utf-8"))



# # from bs4 import BeautifulSoup
# # import requests
# # import smtplib
# # import os
# # from dotenv import load_dotenv

# # # Load environment variables from .env file
# # load_dotenv()

# # # Practice
# # # url = "https://appbrewery.github.io/instant_pot/"
# # # Live Site

# # # ====================== Add Headers to the Request ===========================
# # URL = "https://www.amazon.in/Haier-Inverter-Refrigerator-HEB-333DS-P-Convertible/dp/B0BTHLGYHZ/ref=sr_1_1_sspa?_encoding=UTF8&content-id=amzn1.sym.58c90a12-100b-4a2f-8e15-7c06f1abe2be&dib=eyJ2IjoiMSJ9.R3t0sYDGe4YgvlPwB9OuOaSPnA4sCEwiNWz0WNwGugnPy4BHQejaTHoXRClBtokGxgAn5Tu1nDNt9TcXoH3FjMIyJ_dMCzWPcqE6HZ0hHi82_omvi0gFwchSkNPlin4JxpNVC8rHTVr5LYs1lpYYXAy5k6lp-cYoMeR4C8Lo9qUcVlBKiQaY8i-IjlnoR_CTQqpGcWNaDsJ5eSeH_TNhjQxSUIlwqpnxqguBqIXe3ua_S6PObuJJ0wkkuBGbzku3hsDsx2Z8R8-OI1IFOv5sHItGqMAwN4jJy3_DKf8gFOY.BmHq5zfQYecP75GvlbSj9l2fi-V09Qgs6pH2THFWQTo&dib_tag=se&pd_rd_r=302c0b74-153b-4f7a-8e3e-8a71b8ee78a3&pd_rd_w=yNbSa&pd_rd_wg=kXNVG&qid=1750229268&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl&th=1"
# # Header = {
# #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
# #     "Accept-Encoding": "gzip, deflate br, zstd",
# #     "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
# #     "Dnt": "1",
# #     "Priority": "u=1",
# #     "Sec-Fetch-Dest": "document",
# #     "Sec-Fetch-Mode": "navigate",
# #     "Sec-Fetch-Site": "none",
# #     "Sec-Fetch-User": "?1",
# #     "Sec-Gpc": "1",
# #     "Upgrade-Insecure-Requests": "1",
# #     "Referer": "https://www.amazon.in/",
# #     "Cookie": "ad-id=A_Hd57lwm08blOUlf_eZmgg; ad-privacy=0",
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
# # }

# # # Adding headers to the request
# # response = requests.get(URL, headers=Header)

# # soup = BeautifulSoup(response.content, "html.parser")
# # # Check you are getting the actual Amazon page back and not something else:
# # print(soup.prettify())

# # # Find the HTML element that contains the price
# # price = soup.find(class_="a-offscreen").get_text()

# # # Remove the dollar sign using split
# # price_without_currency = price.split("₹")[1].replace(",", "").strip()


# # # Convert to floating point number
# # price_as_float = float(price_without_currency)
# # print(price_as_float)

# # # Get the product title
# # title = soup.find(id="productTitle").get_text().strip()
# # print(title)

# # # Set the price below which you would like to get a notification
# # BUY_PRICE = 70

# # if price_as_float < BUY_PRICE:
# #     message = f"{title} is on sale for {price}!"

# #     # ====================== Send the email ===========================

# #     with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
# #         connection.starttls()
# #         result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
# #         connection.sendmail(
# #             from_addr=os.environ["EMAIL_ADDRESS"],
# #             to_addrs=os.environ["EMAIL_ADDRESS"],
# #             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
# #         )












from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default-secret-key')

# Load environment variables
load_dotenv()

# Database setup
def init_db():
    conn = sqlite3.connect('price_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS alerts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT NOT NULL,
                  product_url TEXT NOT NULL,
                  target_price REAL NOT NULL,
                  product_name TEXT,
                  current_price REAL,
                  last_checked TEXT,
                  is_active INTEGER DEFAULT 1)''')
    conn.commit()
    conn.close()

init_db()

# Amazon headers configuration
AMAZON_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Dnt": "1",
    "Upgrade-Insecure-Requests": "1"
}

def get_product_info(url):
    try:
        response = requests.get(url, headers=AMAZON_HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get product title
        title_element = soup.find(id="productTitle")
        if not title_element:
            return None, None, "Could not find product title"
        title = title_element.get_text().strip()
        
        # Get product price
        price_element = soup.find(class_="a-offscreen")
        if not price_element:
            return None, None, "Could not find product price"
        
        price_text = price_element.get_text()
        try:
            price = float(price_text.split("₹")[1].replace(",", ""))
        except (IndexError, ValueError):
            return None, None, "Could not parse product price"
        
        return title, price, None
    except Exception as e:
        return None, None, str(e)

def send_email_notification(email, product_name, current_price, product_url):
    try:
        mymail = os.environ["MYMAIL"]
        password = os.environ["PASSWORD"]
        smtp_address = os.environ["SMTP_ADDRESS"]
        smtp_port = int(os.environ["SMTP_PORT"])
        
        message = f"Subject: Amazon Price Alert!\n\n{product_name} is now available for ₹{current_price:,.2f}\n\nBuy it now at {product_url}"
        
        with smtplib.SMTP(smtp_address, smtp_port) as connection:
            connection.starttls()
            connection.login(user=mymail, password=password)
            connection.sendmail(
                from_addr=mymail,
                to_addrs=email,
                msg=message.encode("utf-8")
            )
        return True, None
    except Exception as e:
        return False, str(e)

def check_alerts():
    conn = sqlite3.connect('price_tracker.db')
    c = conn.cursor()
    
    # Get all active alerts
    c.execute("SELECT id, email, product_url, target_price, product_name FROM alerts WHERE is_active = 1")
    alerts = c.fetchall()
    
    for alert in alerts:
        alert_id, email, product_url, target_price, product_name = alert
        
        # Get current product info
        current_name, current_price, error = get_product_info(product_url)
        
        if error:
            print(f"Error checking alert {alert_id}: {error}")
            continue
        
        # Update the alert with current info
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("UPDATE alerts SET product_name = ?, current_price = ?, last_checked = ? WHERE id = ?",
                 (current_name, current_price, now, alert_id))
        conn.commit()
        
        # Check if price is below target
        if current_price <= target_price:
            success, error = send_email_notification(email, current_name, current_price, product_url)
            if success:
                # Deactivate the alert after sending notification
                c.execute("UPDATE alerts SET is_active = 0 WHERE id = ?", (alert_id,))
                conn.commit()
    
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('price_tracker.db')
    c = conn.cursor()
    c.execute("SELECT * FROM alerts ORDER BY last_checked DESC")
    alerts = c.fetchall()
    conn.close()
    return render_template('index.html', alerts=alerts)

@app.route('/add_alert', methods=['GET', 'POST'])
def add_alert():
    if request.method == 'POST':
        email = request.form['email']
        product_url = request.form['product_url']
        target_price = float(request.form['target_price'])
        
        # Validate URL is from Amazon
        if "amazon." not in product_url.lower():
            flash("Please enter a valid Amazon product URL", "error")
            return redirect(url_for('add_alert'))
        
        # Get product info
        product_name, current_price, error = get_product_info(product_url)
        if error:
            flash(f"Error fetching product info: {error}", "error")
            return redirect(url_for('add_alert'))
        
        # Save to database
        conn = sqlite3.connect('price_tracker.db')
        c = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c.execute("INSERT INTO alerts (email, product_url, target_price, product_name, current_price, last_checked) VALUES (?, ?, ?, ?, ?, ?)",
                 (email, product_url, target_price, product_name, current_price, now))
        conn.commit()
        conn.close()
        
        flash("Price alert created successfully!", "success")
        return redirect(url_for('home'))
    
    return render_template('add_alert.html')

@app.route('/delete_alert/<int:alert_id>')
def delete_alert(alert_id):
    conn = sqlite3.connect('price_tracker.db')
    c = conn.cursor()
    c.execute("DELETE FROM alerts WHERE id = ?", (alert_id,))
    conn.commit()
    conn.close()
    flash("Alert deleted successfully", "success")
    return redirect(url_for('home'))

@app.route('/toggle_alert/<int:alert_id>')
def toggle_alert(alert_id):
    conn = sqlite3.connect('price_tracker.db')
    c = conn.cursor()
    c.execute("UPDATE alerts SET is_active = NOT is_active WHERE id = ?", (alert_id,))
    conn.commit()
    conn.close()
    flash("Alert status updated", "success")
    return redirect(url_for('home'))

@app.route('/check_alerts')
def manual_check_alerts():
    check_alerts()
    flash("All alerts checked successfully", "success")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)