# Bot for Dawn Extension [1.7]

## ⚙️ Config (config > settings.yaml):

```
FOR REGISTRATION MODULE:
Accounts: data > register.txt | Format:
- email:password

FOR FARM, EXPORT AND TASKS MODULES:
Accounts: data > farm.txt | Format:
- email:password

Proxies: data > proxies.txt | Format:
- type://user:pass@ip:port (http/socks5)
- type://user:pass:ip:port (http/socks5)
- type://ip:port:user:pass (http/socks5)
- type://ip:port@user:pass (http/socks5)
```


| Name              | Description                                           |
|-------------------|-------------------------------------------------------|
| threads           | Number of accounts that will work simultaneously      |
| keepalive_interval             | delay between keepalive requests in seconds           |
| imap_settings             | imap servers for your mails                           |
| captcha_service             | service for solving captcha (2captcha or anticaptcha) |
| two_captcha_api_key             | 2captcha api key                                      |
| anti_captcha_api_key             | anti-captcha api key                                  |



## 🚀 | How to start:
1. **Install python >= 3.11:**
```bash
https://www.python.org/downloads/
```
2. **Clone the repository:**
```bash
git clone this repo
```
3. **Create and activate a virtual environment:**
```bash
python -m venv venv
cd venv/Scripts
activate
cd ../..
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```
4. **Run the bot:**
```bash
python run.py
```