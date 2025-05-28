# Ekran Kaydı ve Video Analiz Aracı

Bu Python projesi, ekran kaydı alıp Google Gemini AI modeli ile kaydedilen videoyu analiz eden bir uygulamadır. 

## Özellikler
- 5 saniyelik ekran kaydı yapar.
- Kaydı `.avi` formatında kaydeder.
- Google Gemini AI modeli ile ekran kaydındaki içeriği Türkçe analiz eder.
- Konsol pencere görünürlüğünü otomatik yönetir.
- Kullanıcı `exit` komutuyla çıkabilir.

## Gereksinimler
- Python 3.7 ve üzeri
- OpenCV (cv2)
- numpy
- pyautogui
- google-genai (Google Gemini API istemcisi)

## Kullanım
1. API anahtarınızı `client = genai.Client(api_key="API_ANAHTARINIZ")` satırına ekleyin.
2. Terminalden programı çalıştırın:
    ```bash
    python ekran_kaydi_analiz.py
    ```
3. Komut istemine istediğiniz analiz komutunu yazın.
4. `exit` yazarak programdan çıkabilirsiniz.

## Notlar
- Kontrol+Ü kısayol tuşları ile o an olduğunuz pencerede aktif olarak çalışır.
- Kayda başlamak için program konsol penceresini gizler.
- Ekran kaydı fare tıklaması veya 5 saniye sonunda otomatik durur.
- Google Gemini API bağlantısı için geçerli bir API anahtarına ihtiyacınız vardır.
