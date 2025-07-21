import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def garena_uid_lookup():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error": "uid parameter missing"}), 400

    url = "https://shop.garena.sg/api/auth/player_id_login"

    payload = {
        "app_id": 100067,
        "login_id": uid
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11; V2026 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.7049.111 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/json",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-ch-ua": "\"Android WebView\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?1",
        "Origin": "https://shop.garena.sg",
        "X-Requested-With": "mark.via.gp",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://shop.garena.sg/?app=100067",
        "Accept-Language": "en-MY,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-US;q=0.6",
        "Cookie": "source=mb; region=SG; mspid2=b35270728bf676f257f2a5958fc8f1d4; _fbp=fb.1.1753105810200.990604622333016770; language=en; session_key=eay3liuy6ykke8piegw3kv9q8vaaoy18; datadome=Yi2adr5Ey6zBgKPHAsJVcAvhYEt2MjKSumxYJr7V5d~aNWdGXSSnr11dlSmzAC9t65fLp7yPdyIrb8oTl9v18VOEiTXu06aD3thHDI2iwzVtdfJ5PM7GqaLXmBZYXTZO"
    }

    try:
        res = requests.post(url, headers=headers, json=payload)
        data = res.json()

        # Filtered response
        output = {
            "uid": uid,
            "nickname": data.get("nickname", ""),
            "region": data.get("region", "")
        }

        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
