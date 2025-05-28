import ctypes
import sys
import time
import cv2
import numpy as np
import pyautogui
from google import genai
from google.genai import types

client = genai.Client(api_key="senin Api Anahtarın")
# Gemini modelini kullanabilmek için istemci oluşturduk.

def fare(event, flags, param):
    global cıkıs
    if event == cv2.EVENT_LBUTTONDOWN:
        cıkıs = True
# Kullanıcı fareyle tıklayınca kaydı durdurmak için kontrol ekledik.

def ekran_kaydı():
    eight = pyautogui.size()
    screen_width, screen_height = pyautogui.size()
    cıkıs = False
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("ekran.avi", fourcc, 20.0, (screen_width, screen_height))
    # Ekran görüntülerini video olarak kaydedebilmek için VideoWriter oluşturduk.

    print("Kayıt başlatıldı. Çıkmak için 'q' tuşuna bas.")
    start = time.time()

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)
        # Ekran görüntüsünü yakalayıp yazılabilir video formatına çevirip kaydettik.

        if time.time() - start > 5 or cıkıs:
            break
        # 5 saniye geçtiyse veya kullanıcı çıkmak isterse döngüyü bitiriyoruz.

        cv2.waitKey(1)

    out.release()
    cv2.destroyAllWindows()
    print("Kayıt sona erdi.")

def video_analiz(komut):
    video_file_name = "ekran.avi"
    video_bytes = open(video_file_name, 'rb').read()
    # Kayıt ettiğimiz ekran videosunu ikili veri olarak okuduk.

    response = client.models.generate_content(
        model='models/gemini-2.0-flash',
        contents=types.Content(
            parts=[
                types.Part(
                    inline_data=types.Blob(data=video_bytes, mime_type='video/mp4')
                ),
                types.Part(text=komut)
            ]
        ),
        config=types.GenerateContentConfig(
            system_instruction=[
                "You are an AI assistant that analyzes the content shown in screen recordings.",
                "You respond only based on what is visible in the screen recording.",
                "You must always answer in Turkish.",
                "You should describe what is happening on the screen clearly and directly.",
                "If code appears on screen, explain what the code does.",
                "If an application is being used, explain how it is being used.",
                "Avoid decorative language or unnecessary punctuation.",
                "If the content is unrelated to programming or screen activity, respond briefly and neutrally in Turkish.",
                "If the content cannot be understood, respond with: 'Ekran içeriğini anlayamadım.'",
                "Do not make assumptions beyond what is visible in the video.",
                "Keep your responses short, useful, and focused.",
                "Behave as if you're helping someone understand what's happening on the screen."
            ],
            temperature=0.5,
            max_output_tokens=200,
            top_p=0.8,
            top_k=40,
            stop_sequences=["\n\n"]
        )
    )
    print(response.candidates[0].content.parts[0].text)
    # Gemini modelinden gelen analiz sonucunu ekrana bastık.

if __name__ == "__main__":
    print("Çıkmak için 'exit' yazın.")
    while True:
        komut = input(">>> ")
        if komut.lower() == 'exit':
            print("Çıkılıyor...")
            sys.exit()
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.ShowWindow(hwnd, 6)
        # Konsol penceresini geçici olarak gizledik.

        ekran_kaydı()
        video_analiz(komut)

        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        ctypes.windll.user32.ShowWindow(hwnd, 9)
        # Konsol penceresini tekrar görünür yaptık.
