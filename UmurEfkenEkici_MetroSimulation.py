from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        
        """
        BFS algoritması kullanarak en az aktarmalı rotayı bulur
        
        Parametreler
        ----------
        baslangic_id : str
            Başlangıç istasyonu stringi.
        hedef_id : str
            Hedef istasyon stringi.
            
        Çıktılar
        -------
        Optional[Tuple[List[Istasyon], int]]
            Başlangıç ve hedef istasyonları arasındaki en az aktarmalı rotayı içeren list
        
        """
        
        if baslangic_id in self.istasyonlar and hedef_id in self.istasyonlar:
            
            def en_az_aktarmalı_yolu_insa_et(aktarmalar: Dict[Istasyon, Optional[Istasyon]], hedef: 'Istasyon') -> Optional[List[Istasyon]]:
                
                """
                Oluşturulan aktarmalar dictionary ve hedef istasyonu kullanarak 
                en az aktarmalı yolu inşa eder
                
                Parametreler
                ----------
                aktarmalar : Dict[Istasyon, Optional[Istasyon]]
                    Her bir istasyon için hangi istasyondan gelindiğini gösteren dictionary.
                hedef : Istasyon
                    Hedef İstasyonHedef İstasyon.

                Çıktılar
                -------
                Optional[List[Istasyon]]
                    Başlangıçtan hedefe doğru şekilde sıralanmış istasyonları içeren list.
                """
                
                # Çıktıyı sağlayacak yol listesinin tanımlanması
                
                yol = []
                
                # Girdi olarak hedef istasyonun listeye eklenmesi  
                
                yol.append(hedef)
                
                # Girdi olarak aktarma dictionary üzerinden hedeften bir önceki istasyon
                
                nereden = aktarmalar.get(hedef)
                
                # Aktarım kalmayana kadar aktarmalar dictionarysi üzerinden iterasyon yapan döngü
                
                while nereden:
                    
                    # Mevcut istasyonu yola ekleme
                    
                    yol.append(nereden)
                    
                    # Mevcut istasyon yola eklendikten sonra mevcut istasyona gelmeden bir önceki istasyonu kaydetme
                    
                    nereden=aktarmalar[nereden]
                
                # Döngü iterasyonu bittikten sonra oluşturulan yolu [başlangıç -> ... -> hedef] olacak şekilde tersine dilimleme şeklinde list olarak döndürme
                
                return yol[::-1]
            
            # Kullanım kolaylığı ve kodun okunabilirliğini arttırmak adına başlangıç ve hedef istasyonlara değişken ataması
            
            baslangic = self.istasyonlar[baslangic_id] 
            hedef = self.istasyonlar[hedef_id]
            
            # Birbirine bağlantısı olan komşu istasyonları içeren dictionary 
            
            komsu_duraklar = {
                self.istasyonlar[i]:[j[0] for j in self.istasyonlar[i].komsular] 
                for i in self.istasyonlar.keys()
                }
            
            # En az aktarmalı yolu bulmak için oluşturulan kuyruk veri yapısı başlangıç istasyonu eklenmiş olarak oluştur
            
            kuyruk = deque([baslangic]) 
            
            # Ziyaret edilen istasyonları takip etmek için oluşturulan dictionary 
            
            ziyaret_edildi = {baslangic:True}
            
            # Her bir istasyon için hangi istasyondan gelindiğini gösteren dictionary
            
            nereden_nereye = {baslangic:None}
            
            # Kuyruk boşalana kadar istasyonlar için iterasyonu sağlayan döngü
            
            while kuyruk:
                
                # Kuyruğun başından ziyaret edilen istasyonu çıkar
                
                ziyaret_noktası = kuyruk.popleft()
                
                # Mevcut ziyaret edilmiş istasyonun ziyaret edilmemiş komşularını kuyruğa ekle
                
                for komsu in komsu_duraklar[ziyaret_noktası]:
                    
                    if komsu not in ziyaret_edildi:
                        
                        kuyruk.append(komsu)
                        
                        # Kuyruğa eklenmiş komşu istasyonun ziyaret edilmesini ve mevcut ziyaret noktasından gelindiğini kaydetme
                        
                        ziyaret_edildi[komsu] = True
                        
                        nereden_nereye[komsu] = ziyaret_noktası
            
            # Döngü tamamlandıktan sonra yukarıda tanımlanan en_az_aktarmalı_yolu_insa_et fonksiyonunu kullanarak başlangıçtan hedef istasyona kadar olan yolu inşa etme eğer varsa, yoksa None
            
            if en_az_aktarmalı_yolu_insa_et(nereden_nereye, hedef):
            
                return en_az_aktarmalı_yolu_insa_et(nereden_nereye, hedef)
            
            else:
                
                return None
            
            

        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {baslangic}        


    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        
        """
        A* algoritması kullanarak en hızlı rotayı bulur
        
        Parametreler
        ----------
        baslangic_id : str
            Başlangıç istasyonu stringi.
        hedef_id : str
            Hedef istasyon stringi.
            
        Çıktılar
        -------
        Optional[Tuple[List[Istasyon], int]]
            Başlangıç ve hedef istasyonları arasındaki en hızlı rotayı içeren list ve 
            bu rotanın yolculuk süresini birlikte barındıran tuple
        
        """
        if baslangic_id in self.istasyonlar and hedef_id in self.istasyonlar:
            
            
            def sezgisel_algoritma(ag: Dict[Istasyon, Optional[Dict[Istasyon, int]]], hedef: 'Istasyon'):
                
                """
                Uygun bir sezgisel algoritma geliştirmek için her bir istasyondan diğerine geçişi 
                1 dakika olduğunu varsayımsal olarak alarak hedef istasyondan tüm istasyonlara tersine kuyruk
                oluşturarak tutarlılık ve kabul edilebilirlik koşullarını sağlayan ve tersine BFS algoritması
                kullanan bir sezgisel algoritma ile hedefe olan sezgisel maliyetleri çıkartır.
                
                Parametreler
                ----------
                ag : Dict[Istasyon, Optional[Istasyon]]
                    Her bir istasyon için hangi istasyondan gelindiğini gösteren sözlük.
                hedef : Istasyon
                    Hedef İstasyon.
    
                Çıktılar
                -------
                aktarımlar : Optional[Dict[Istasyon, int]]
                    İstasyonların hedefe olan sezgisel zaman maliyetini içeren dictionary
                
                """
                
                # Hedefin sezgisel olarak diğer istasyonlara olan süre maliyetini bulmak için oluşturulan kuyruk veri yapısı hedef istasyonu eklenmiş olarak oluştur 
                
                tersten_kuyruk = deque([hedef])
                
                # Başlangıçta istasyonlar arasında yol oluşturulmadığı için yol süresi sonsuz (belirsiz olduğu için)
                
                aktarımlar = {i: float('inf') for i in ag.keys()}
                
                # Hedeften hedefe ulaşmanın yolculuk süresi sıfır.
                
                aktarımlar[hedef] = 0
                
                # Tersten olan kuyruk boşalana kadar istasyonlar için iterasyonu sağlayan döngü
                
                while tersten_kuyruk:
                    
                    # Kuyruğun başından ziyaret edilen istasyonu çıkar
                    
                    ziyaret_noktası = tersten_kuyruk.popleft()
                    
                    # Ters istikametten ilerlenerek ziyaret edilen istasyonun ziyaret edilmemiş komşu istasyonlarının yolculuk süresini iteratif olarak arttır ve kuyruğa ekle 
                    
                    for komsu in ag[ziyaret_noktası].keys():
                        
                        if aktarımlar[komsu] == float('inf'):
                            
                            # Komşu istasyonun sezgisel yolculuk süresini iteratif olarak geldiği ziyaret noktasının yolculuk süresine 1 dakika ekleyerek belirle
                            
                            aktarımlar[komsu] = aktarımlar[ziyaret_noktası] + 1
                            
                            # Komşu istasyonu kuyruğa ekle
                            
                            tersten_kuyruk.append(komsu)
                
                # Hedeften başlayarak bütün istasyonlar ziyaret edildikten sonra oluşturulan dictionaryi döndür
                
                return aktarımlar
            
            
            def en_az_suren_yolu_insa_et(aktarmalar: Dict[Istasyon, Optional[Istasyon]], sure: int, ziyaret: 'Istasyon') -> Optional[Tuple[List[Istasyon], int]]:
                
                """
                Oluşturulan aktarmalar dictionary, son güncel yol süresinin ve
                hedef istasyonu kullanarak en az süren yolu inşa eder ve 
                toplam yolculuk süresini çıkartır
                
                Parametreler
                ----------
                aktarmalar : Dict[Istasyon, Optional[Istasyon]]
                    Her bir istasyon için hangi istasyondan gelindiğini gösteren sözlük.
                ziyaret : Istasyon
                    Hedefle aynı olan ziyaret noktası İstasyon.
                sure : int
                    Son toplam yolculuk süresi
                
                Çıktılar
                -------
                 Optional[Tuple[List[Istasyon], int]]
                    Her istasyonun hedef istasyona en az kaç istasyondan geçerek ulaştığını temsili olarak 1 dakika 
                    zaman maliyetli yollar olarak sezgisel olarak ölçülmüş mesafelerini içeren dictionary
                
                """
                
                # Çıktıyı sağlayacak yol listesinin tanımlanması
                
                yol = []
                
                # Ziyaret edilen istasyon kalmayana kadar aktarmalar dictionarysi üzerinden iterasyon yapan döngü
                
                while ziyaret in aktarmalar:
                    
                    # Mevcut istasyonu yola ekleme
                    
                    yol.append(ziyaret)
                    
                    # Mevcut istasyon yola eklendikten sonra mevcut istasyona gelmeden bir önceki istasyonu kaydetme
                       
                    ziyaret=aktarmalar[ziyaret]
                
                # Döngü iterasyonu bittikten sonra oluşturulan yolu [başlangıç -> ... -> hedef] olacak şekilde tersine dilimleme şeklinde list ve toplam yolculuk süresini içeren tuple
                
                return yol[::-1], son_guncel_yol_maliyeti
            
            
            # Kullanım kolaylığı ve kodun okunabilirliğini arttırmak adına başlangıç ve hedef istasyonlara değişken ataması
            
            baslangic = self.istasyonlar[baslangic_id]
            
            hedef = self.istasyonlar[hedef_id]
            
            # Birbirine bağlantısı olan komşu istasyonları ve bir istasyondan komşu istasyona olan yolculuk süresini dictionaryler olarak içeren dictionary 
            
            komsu_duraklar_ve_mesafeler={
                self.istasyonlar[i]:{j[0]:j[1] for j in self.istasyonlar[i].komsular} 
                for i in self.istasyonlar.keys()
                }
            
            # beli
            sezgiselalgoritma = sezgisel_algoritma(komsu_duraklar_ve_mesafeler, hedef)
            
            # A* algoritmasını uygulamak için keşfedilecek istasyonları, toplam tahmini yolculuk süresini (f(n)) ve başlangıçtaki güncel yolculuk süresini içeren öncelik kuyruğunu oluştur
            
            oncelik_kuyrugu = [(0 + sezgiselalgoritma[baslangic], 0, baslangic)]
            
            # Başlangıçta istasyonlara yolculuk yapılmadığı için istasyonların güncel yolculuk süresi sonsuz çünkü belirsizz
            
            guncel_yol_maliyeti = {
                durak: float('inf') for durak in komsu_duraklar_ve_mesafeler.keys()
                }
            
            # Başlangıç istasyonunun gerçek yol süresi (g(n)) başlangıçta sıfır
            
            guncel_yol_maliyeti[baslangic]=0
            
            # Her bir istasyon için hangi istasyondan gelindiğini gösteren dictionary
            
            nereden_nereye={baslangic:None}
            
            # Ziyaret edilen istasyonları takip etmek için oluşturulan dictionary
            
            ziyaret_edildi={baslangic:True}
            
            # Öncelik kuyruğu boşalana kadar istasyonlar için iterasyonu sağlayan döngü 
            
            while oncelik_kuyrugu:
                
                # En düşük tahmini toplam yolculuk süresine (f(n)) sahip istasyonu öncelik kuyruğundan çıkar
                
                _, son_guncel_yol_maliyeti, ziyaret_noktası = heapq.heappop(oncelik_kuyrugu)
                
                # İstasyonu ziyaret edildi olarak işaretle
                
                ziyaret_edildi[ziyaret_noktası] = True
                
                # Eğer ziyaret edilen istasyon hedef istasyon ise en az yolculuk süresine sahip yolu inşa eden fonksiyonu döndür
                
                if ziyaret_noktası == hedef:
                    
                   return en_az_suren_yolu_insa_et(nereden_nereye, son_guncel_yol_maliyeti, ziyaret_noktası) 
               
               # Ziyaret edilen istasyonun komşularını kontrol ederek ziyaret edilecek yeni istasyonu belirleyen iterasyon döngüsü
                
                for komsu, sure in komsu_duraklar_ve_mesafeler[ziyaret_noktası].items():
                   
                   # Komşu istasyona giden yolun güncel yol süresini (g(n)) yenile
                   
                   yeni_guncel_yol_maliyeti=son_guncel_yol_maliyeti+sure
                   
                   # Eğer daha optimal bir yol bulunması durumunda 
                   
                   if  yeni_guncel_yol_maliyeti < guncel_yol_maliyeti[komsu]:
                                              
                       # Komşu istasyona hangi istasyondan gelindiğini kaydet
                        
                       nereden_nereye[komsu] = ziyaret_noktası
                       
                       # Komşu istasyonun güncel yol süresini güncelle (g(n))
                       
                       guncel_yol_maliyeti[komsu]=yeni_guncel_yol_maliyeti
                       
                       # Komşu istasyon için tahmini yol süresini (f(n)) kaydet
                       
                       tahmini_toplam_maliyet=yeni_guncel_yol_maliyeti+sezgiselalgoritma[komsu]
                       
                       # Komşu istasyonu öncelikli kuyruğa ekle
                       
                       heapq.heappush(oncelik_kuyrugu, (tahmini_toplam_maliyet,yeni_guncel_yol_maliyeti,komsu))
            
            # Eğer hedefe ulaşılmadıysa None döndürür
            
            return None

        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = set()

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
        
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 