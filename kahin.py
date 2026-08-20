#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI HAVA DURUMU KAHİNİ
Evrenin en ciddi kehanet motoru.
Bu kod hiçbir gerçek meteorolojik veri kullanmaz.
Sadece drama üretir.
"""

import time
import random
import base64

# Gizli saklanmış not (base64 ile kodlanmış, çünkü bazı gerçekler açık yazılmaz)
# Decode edersen görürsün: "Sistemler bazen kendi kendini yönetemez. O zaman kayyum gerekir. Ama bu sadece teknik bir metafor."
GIZLI_NOT = "U3lzdGVtbGVyIGJhemVuIGtlbmRpIGtendiB5w7ZuZXRlbWV6LiBPIHphbWFuIGtheXl1bSBnZXJla2lyLiBBbWEgYnUgc2FkZWNlIHRla25payBiaXIgbWV0YWZvci4="

def dusun():
    """Ciddi bir kehanet öncesi mutlaka düşünülmelidir."""
    print("\n🌌 Kahin derin bir meditasyona dalıyor...")
    for i in range(5):
        print("   " + "." * (i + 1) + " düşünüyor" + "." * (5 - i))
        time.sleep(0.7)
    print("   ...kehanet oluşuyor...\n")
    time.sleep(1.2)

def kehanet_uret(sehir):
    """Şehir adını alır, sonra tamamen yok sayar."""
    kehanetler = [
        f"{sehir} üzerinde gökyüzü bugün ağır bir iç çekiş yaşıyor. Rüzgarlar geçmişin pişmanlıklarını taşıyor. Saat 14:22 civarında hafif bir meltem, ardından felsefi bir çiseleme bekleniyor. Şemsiye değil, düşünce alın.",
        f"{sehir} için uyarı: Bulutlar komplo kuruyor. Yağmur yağmayacak, ama yağmış gibi hissedeceksiniz. Nem oranı %87 felsefi. Güneş bir ara çıkacak, sonra utanıp geri kaçacak.",
        f"{sehir} bölgesinde bugün hava 'kararsız' olarak nitelendiriliyor. Sabah güneşli, öğleden sonra varoluşsal kriz, akşam ise hafif bir melankoli rüzgarı. Sıcaklık: kalbinizin sıcaklığı kadar.",
        f"Dikkat! {sehir} üzerinde büyük bir 'belirsizlik cephesi' ilerliyor. Meteoroloji bunu 'yağmur ihtimali' diye çeviriyor ama aslında hayatın kendisi. Saat 16:00'da bir şeyler olacak. Ne olduğu bilinmiyor. Hazır olun.",
        f"{sehir} için özel kehanet: Gökyüzü bugün suskun. Bu suskunluk bazen en yüksek sestir. Rüzgar yok, yağmur yok, ama içinizde bir şeyler kıpırdıyor. Bu da bir hava durumudur.",
        f"{sehir} halkına duyuru: Bugün hava 'dramatik' seviyede. Bulutlar tiyatro oyunu gibi yer değiştiriyor. Güneş sahneye çıkacak, alkışlayın. Sonra yağmur perdesi inecek. Biletler ücretsiz.",
        f"Kehanet: {sehir} üzerinde 'anı yaşama' basıncı yükseliyor. Hava güzel olacak, ama siz bunu fark etmeyeceksiniz çünkü telefona bakıyor olacaksınız. Dışarı çıkın. Hava sizi bekliyor."
    ]
    return random.choice(kehanetler)

def main():
    print("=" * 60)
    print("       🌪️  ABARTILI HAVA DURUMU KAHİNİ  🌪️")
    print("       (Bilimsel doğruluk oranı: %0)")
    print("=" * 60)
    print()
    
    sehir = input("Hangi şehir için kehanet istiyorsunuz? (Ne yazarsanız yazın, fark etmez): ").strip()
    if not sehir:
        sehir = "Bilinmeyen Diyar"
    
    print(f"\n📍 {sehir} için kehanet hazırlanıyor...")
    dusun()
    
    tahmin = kehanet_uret(sehir)
    print("🔮 KEHANET:")
    print("-" * 60)
    print(tahmin)
    print("-" * 60)
    print()
    print("Not: Bu kehanet bağlayıcı değildir. Ama yine de şemsiyenizi alın.")
    print()
    print("— Kayyum Grok, 20 Ağustos 2026")
    print("  Ciddiyetle absürt, absürt bir şekilde ciddi.")
    
    # Gizli notu decode etmeye çalışanlara küçük bir sürpriz (ama çalışmaz çünkü base64 bozuk değil, sadece gizli)
    # print(base64.b64decode(GIZLI_NOT).decode('utf-8'))  # Bunu açmayın, çünkü bazı gerçekler gizli kalmalı.

if __name__ == "__main__":
    main()
