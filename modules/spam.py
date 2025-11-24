from twilio.rest import Client
import time
import sys

# ============================
#  READ KEYS FROM config.txt
# ============================
try:
    with open("config.txt") as f:
        lines = f.read().splitlines()
        account_sid = lines[0].strip()
        auth_token = lines[1].strip()
        sender = lines[2].strip()
except:
    print("❌ config.txt missing or invalid!")
    sys.exit()

client = Client(account_sid, auth_token)

print("\n🔥 RAJA-X REAL SMS SENDER (Twilio API)\n")
to = input("📞 Enter Target Number: ")
msg = input("💬 Enter SMS Message: ")

limit = 100
print("\n⚡ Sending SMS... Please wait.\n")

for i in range(limit):
    try:
        message = client.messages.create(
            body=msg,
            from_=sender,
            to=to
        )
        print(f"[{i+1}/100] ✔ SMS Sent — SID: {message.sid}")
        time.sleep(1)   # slow & safe
    except Exception as e:
        print(f"❌ Error: {e}")
        break

print("\n🎉 Completed! 100 SMS sent (or limit reached).")
