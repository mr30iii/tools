import webbrowser
import time

# Apne links yahan daalo (Replace your links here)
WHATSAPP_CHANNEL_LINK = "http://whatsapp.com/channel/0029VbBTcfJCHDys1Q2ltf0n" 
MEDIAFIRE_DOWNLOAD_LINK = "https://files.catbox.moe/w9fmg4.apk"

def app_download_start_karo():
    """
    Pehle WhatsApp channel kholo, phir download link open karo.
    """
    print("--- 🔔 IMPORTANT CHECK 🔔 ---")
    print("Boss, yeh app download karne se pehle, aapko humara WhatsApp Channel FOLLOW karna padega.")
    print(f"Channel Link: {WHATSAPP_CHANNEL_LINK}")
    
    # WhatsApp channel link browser mein kholo
    webbrowser.open(WHATSAPP_CHANNEL_LINK)
    
    time.sleep(3) # Wait karo, taaki browser khul jaaye

    print("\n------------------------------")
    
    # User se pucho (Ask for confirmation)
    user_reply = input("Kya aapne channel follow kar liya hai? (Type 'DONE' ya 'HO GAYA'): ").strip().upper()

    # Check karo agar user ne 'DONE' ya 'HO GAYA' type kiya hai
    if user_reply == "DONE" or user_reply == "HO GAYA":
        print("\n✅ Bohot badhiya! Ab aapka app download shuru ho raha hai.")
        print("JUST RUN AND ENJOY THE TOOL!\n")
        
        # Mediafire link browser mein kholo
        webbrowser.open(MEDIAFIRE_DOWNLOAD_LINK)
        
    else:
        print("\n❌ Arey yaar! Aapne confirmation nahi diya. Download nahi shuru hoga.")
        print("Pehle channel follow karo, phir se script chalao.")

if __name__ == "__main__":
    app_download_start_karo()