#Okul Yönetim Sistemi
Bu proje, bir okul yönetim sistemi için geliştirilmiş bir Python uygulamasıdır. Öğrenci ve öğretmen kayıtlarını yönetmek, sınıf-ders ilişkilerini görüntülemek gibi temel işlevleri içerir.

-Özellikler
Öğrenci kayıt, güncelleme, silme ve listeleme
Öğretmen kayıt işlemleri
Sınıflara göre ders ve öğretmen bilgilerini görüntüleme
Kullanıcı dostu konsol arayüzü

-Kullanım
connection.py dosyasında veritabanı bağlantı bilgilerini güncelleyin:

connection = mysql.connector.connect(
    host = "localhost",
    user = "kullanici_adi",
    password = "sifreniz",
    database = "veritabani_adi"
)


Yeni bir branch oluşturun (git checkout -b yeni-ozellik)
Değişikliklerinizi commit edin (git commit -am 'Yeni özellik eklendi')
Branch'i pushlayın (git push origin yeni-ozellik)
Pull Request oluşturun

Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.

Not
Bu proje belirli bir veritabanı yapısına göre geliştirilmiştir. Kendi veritabanınızı kullanacaksanız:

Tablo isimlerini ve alanları projedekiyle aynı yapın

Veya ilgili Python dosyalarındaki SQL sorgularını ve model sınıflarını kendi yapınıza uygun şekilde değiştirin

Veritabanı bağlantı bilgilerini connection.py dosyasında düzenlemeyi unutmayın.
