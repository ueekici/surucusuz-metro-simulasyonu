# 🚇 Sürücüsüz Metro Simülasyonu – Rota Optimizasyonu

Bu proje, mevcut bir metro ağı üzerinde başlangıç ve hedef istasyonlar arasında **en hızlı** ve **en az aktarmalı** rotaları bulan bir simülasyon sunar. 

---

## 🛠️ Teknolojiler ve Kullanılan Kütüphaneler

### Python 3.10
- Algoritmaların yazımı ve gerekli modüllerin kullanımı için kullanılan programlama dili.

### heapq
- Heapq modülü öncelikli kuyruk algoritmasının uygulanmasını sağlayan bir Python kütüphanesidir. Öncelik kuyruğu gibi uygulamalarda logaritmik zaman karmaşıklıklığı sağladığı için verimliliği arttırmaktadır.
- A* algoritmasında başlangıçtan hedefe doğru en hızlı rotayı kurarken öncelik kuyruğu yapısını verimli bir şekilde uygulamak için kullanıldı.

### collections
- Collections modülü python için farklı türde kapsayıcıların kullanımını sağlayan bir kütüphanedir. Bir kapsayıcı farklı nesneleri depolamak, kapsanan nesnelere erişmek ve onların üzerinden iterasyon yapmak için kullanılan bir nesnedir.
- Ayrıca kuyruk gibi veri yapıları için ekleme ve çıkarma işlemlerin list yapısındaki zaman karmaşıklığını *O(n)* yerine *O(1)* olmasını sağlayarak algoritmaların daha verimli çalışmasını sağlar.
- BFS algoritmasında başlangıçtan hedefe doğru en az aktarmalı rotayı kurarken istasyonların kuyruk yapısına daha hızlı ve verimli şekilde eklenmesi ve çıkartılmasında hem stack hem de queue yapıları için optimize edilmiş deque kapsayıcısı ve ilgili fonksiyonları kullanıldı.
- Ve istasyonların hangi hatlara ait olduklarını depolamada kullanım kolaylığı sağladığından defaultdict kapsayıcısı kullanıldı.

---

## 📊 Algoritmaların Çalışma Mantığı

### BFS (Breadth-First Search / Genişlik Öncelikli Arama) Algoritması

- **Genişlik Öncelikli Arama (BFS)** temel bir grafik dolaşma algoritmasıdır. Temel amacı iki belirli düğüm arasındaki en kısa mesafeyi bulmaktır. İlk giren ilk çıkar mantığıyla kuyruk veri yapısı kullanır. Bir düğümle başlar, ardından ilk olarak bu düğümün tüm komşu düğümlerini dolaşır. Tüm komşu düğümler ziyaret edildikten sonra, bu komşuların komşuları dolaşılır.

Adımlar:
1. **Başlangıç:** Kaynak yani başlangıç olarak belirlenen düğümü kuyruğa ekle ve ziyaret edilmiş olarak işaretle.
2. **Keşif:** Kuyruk boş değilken:
   - Düğümü kuyruktan çıkar.
   - Komşuları kontrol et. Eğer ziyaret edilmemişse kuyruğa ekle ve geldiği noktayı kaydet.
3. **Sonlanma:** Kuyruk boş kalana kadar keşfe devam et.
4. **Yolu İnşa Et:** Eğer hedefe ulaşıldıysa kayıtlı geçişler üzerinden yol oluşturulur.

### A* Algoritması

- **A* Algoritması** başlangıç ve bitiş noktaları arasında en kısa mesafeyi bulmak için kullanılan gelişmiş bir arama algoritmasıdır. A* sezgisel algoritmalar kullanarak düğümden hedefe doğru maliyeti tahmin eder ve arama sürecini optimize eder.

Kullandığı maliyet fonksiyonları:
1. **g(n):** Başlangıçtan n düğümüne olan gerçek maliyet
2. **h(n):** n düğümünden hedefe olan tahmini maliyet

Toplam maliyet: `f(n) = g(n) + h(n)`

Adımlar:
1. Başlangıç düğümü f(n) değeriyle öncelik kuyruğuna eklenir.
2. En düşük f(n) değerine sahip düğüm kuyruğundan çıkarılır.
3. Eğer bu düğüm hedefse, algoritma sonlanır.
4. Değilse, komşulara gidilerek g, h ve f hesaplanır ve kuyruğa eklenir.
5. Kuyruk boşalana veya hedefe ulaşılana kadar devam eder.

### Neden Bu Algoritmalar?

- **BFS** algoritması zaman maliyetini göz ardı ederek en az aktarmalı (en az adımlı) yolu bulur.
- **A*** algoritması ise maliyet ve yönlendirme ile çalışır, bu sayede en kısa sürede ulaşımı sağlar. Sezgisel olması sayesinde geniş veri kümelerinde de verimli çalışır.

---

## 🧪 Örnek Kullanım ve Test Sonuçları
- Aşağıdaki metro ağı, **en kısa sürede ulaşım** ve **en az aktarmalı güzergah** gibi algoritmaların test edilmesi için oluşturulmuş örnek bir modeldir.
### 🗺️ Hatlar ve İstasyonlar

#### 🚨 Kırmızı Hat
- K1: Kızılay  
- K2: Ulus  
- K3: Demetevler  
- K4: OSB

#### 🔵 Mavi Hat
- M1: AŞTİ  
- M2: Kızılay *(aktarma noktası)*  
- M3: Sıhhiye  
- M4: Gar

#### 🟠 Turuncu Hat
- T1: Batıkent  
- T2: Demetevler *(aktarma noktası)*  
- T3: Gar *(aktarma noktası)*  
- T4: Keçiören

### 🔗 Bağlantılar ve Süreler (dakika)

#### 🚨 Kırmızı Hat
| Başlangıç | Bitiş | Süre |
|-----------|-------|------|
| K1        | K2    | 4 dk |
| K2        | K3    | 6 dk |
| K3        | K4    | 8 dk |

#### 🔵 Mavi Hat
| Başlangıç | Bitiş | Süre |
|-----------|-------|------|
| M1        | M2    | 5 dk |
| M2        | M3    | 3 dk |
| M3        | M4    | 4 dk |

#### 🟠 Turuncu Hat
| Başlangıç | Bitiş | Süre |
|-----------|-------|------|
| T1        | T2    | 7 dk |
| T2        | T3    | 9 dk |
| T3        | T4    | 5 dk |

#### 🔁 Hatlar Arası Aktarma Noktaları
| İstasyon 1 | İstasyon 2 | Açıklama            | Süre |
|------------|-------------|---------------------|------|
| K1         | M2          | Kızılay aktarma     | 2 dk |
| K3         | T2          | Demetevler aktarma  | 3 dk |
| M4         | T3          | Gar aktarma         | 2 dk |

### ✅ Test Senaryoları: Algoritma Sonuçlarının Doğruluğu

| # | Başlangıç → Bitiş       | Rota Türü          | Beklenen Rota ve Süre                              | Algoritmanın Bulduğu Sonuç                        | Uyuşma |
|---|--------------------------|---------------------|-----------------------------------------------------|---------------------------------------------------|--------|
| 1 | AŞTİ → OSB               | En Az Aktarmalı     | AŞTİ → Kızılay → Kızılay → Ulus → Demetevler → OSB | AŞTİ → Kızılay → Kızılay → Ulus → Demetevler → OSB | ✅     |
|   |                          | En Hızlı            | AŞTİ → Kızılay → Kızılay → Ulus → Demetevler → OSB (25 dk) | AŞTİ → Kızılay → Kızılay → Ulus → Demetevler → OSB (25 dk) | ✅     |
| 2 | Batıkent → Keçiören      | En Az Aktarmalı     | Batıkent → Demetevler → Gar → Keçiören             | Batıkent → Demetevler → Gar → Keçiören             | ✅     |
|   |                          | En Hızlı            | Batıkent → Demetevler → Gar → Keçiören (21 dk)     | Batıkent → Demetevler → Gar → Keçiören (21 dk)     | ✅     |
| 3 | Keçiören → AŞTİ          | En Az Aktarmalı     | Keçiören → Gar → Gar → Sıhhiye → Kızılay → AŞTİ    | Keçiören → Gar → Gar → Sıhhiye → Kızılay → AŞTİ    | ✅     |
|   |                          | En Hızlı            | Keçiören → Gar → Gar → Sıhhiye → Kızılay → AŞTİ (19 dk) | Keçiören → Gar → Gar → Sıhhiye → Kızılay → AŞTİ (19 dk) | ✅     |

> Tüm test senaryolarında algoritmaların bulduğu sonuçlar, beklenen rota ve sürelerle birebir örtüşmektedir.

---

## 🚀 Projeyi Geliştirme Fikirleri
- Algoritmalarının kullanımı ve metro ağlarının değiştirilip en az süren ve en az aktarmalı yolları gösteren bir arayüz geliştirilebilir.
- Algoritmaların oluşturduğu rotalar için bütün bir ağ içeren görselleştirmeler oluşturulabilir.
- Ayrıca navigasyon uygulamalarında yaygın olarak görülen en az parasal maliyete sahip rotalar da oluşturulabilir.
