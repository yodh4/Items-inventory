**1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya**

Terdapap beberapa selector pada CSS di antaranya adalah *Element Selector*, *ID Selector*, dan *Class Selector*. 
1. Element Selector

    Element selector digunakan untuk mengubah properti semua elemen yang memiliki tag HTML yang sama. Element selector dapat kita gunakan saat kita memiliki suatu elemen yang konsisten di website kita sehingga properti yang kita atur akan ter-*apply* ke semua elemen dengan tag yang sama.
2. ID Selector
    
    ID selector digunakan dengan memberi ID pada suatu tag yang berfungsi sebagai selectornya. ID ini bersifat unik dalam satu halaman web. ID Selector dapat kita gunakan jika kita memilki elemen dengan tag yang sama namun kita ingin membedakan properti dari tiap tag tersebut.

3. Class Selector

    Class selector digunakan dengan mengelompokan suatu elemen ke dalam class yang sama. Class selector dapat kita gunakan jika kita ingin mengatur suatu properti ke suatu kelompok yang dibungkus oleh suatu class. Hal ini berfungsi jika halaman kita sudah mulai kompleks dan terdiri dari beberapa elemen yang saling berkaitan.
    

**2. Jelaskan HTML5 Tag yang kamu ketahui**

Terdapat banyak sekali Tag yang tersedia di HTML begitu pula dengan attribut untuk masing-masing tag tersebut. Beberapa diantaranya adalah:

1. `<!DOCTYPE html>` untuk mendeklarasikan *type* dokumen
2. `<p>` untuk membuat paragraf
3. `<title>` untuk judul web
4. `<b>` untuk membuat teks menjadi *bold*
5. `<i>` untuk membuat teks menjadi *italic*

Untuk attribut pada HTML terbagi menjadi beberapa jenis di antaranya adalah:
1. Attribut Global
Attribut global adalah attribut yang bisa ditambahkan pada semua elemen HTML, beberapa contoh attribut global adalah `class`, `hidden`, `id`, `style`, `title`.
2. Attribut Event
Attribut event adalah attribut yang digunakan untuk menentukan aksi yang akan dilakukan saat terjadi sesuatu pada elemen, beberapa contoh attribut event adalah `onafterprint`, `onload`, `onresize`, `onpagehide`, `onpageshow`
3. Attribut Khusus
Attribut khusus adalah attribut yang hanya bisa dipakai pada elemen tertentu dan terkadang tidak bisa digunakan pada elemen yang lain, beberapa contoh attribut khusus adalah `src`, `href`, `action`, `autoplay`

**3. Jelaskan perbedaan antara *margin* dan *padding***

Padding dan margin adalah dua hal yang cukup mirip, margin adalah ruang di luar batas luar elemen HTML sedangkan padding adalah batas dalam elemen HTML dengan kontennya sendiri. Margin biasanya digunakan untuk jarak antara suatu elemen dengan elemen lain di luarnya sedangkan padding biasanya digunakan untuk mengatur jarak antara suatu elemen dengan konten dari elemen tersebut. Kita bisa mengatur suatu margin dan padding dengan cara seperti berikut `margin-top: 10px` dan `padding: 20px`

**4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?**

Terdapat beberapa perbedaan antara framework CSS Tailwind dan Bootstrap seperti:
1. Tailwind membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya sedangkan Bootstrap menggunakan tampilan yang sudah jadi dan dapat langsung digunakan
2. Tailwind memiliki ukuran file yang lebih kecil dibanding Bootstrap karena hanya memuat kelas-kelas utilitas yang ada.
3. Tailwind dapat memberikan fleksibilitas lebih terhadap proyek kita sedangkan Bootstrap biasa memberikan tampilan yang lebih konsisten karena menggunakan komponen yang telah didefinisikan
4. Tailwind memiliki *learning curve* yang lebih tinggi dibandingkan dengan Bootstrap karena harus paham bagaimana cara menggabungkan kelas-kelas utilitas yang tersedia sedangkan Bootstrap lebih ramah untuk pemula karena dapat mulai dengan komponen yang telah didefinisikan.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**

1. Mengubah halaman login menggunakan template yang tersedia di internet dan menyesuaikan nama atributnya sesuai fungsi `login_user` yang ada di `views.py`.
2. Mengubah halaman *register* dengan mengganti form yang digunakan dengan form yang ada pada dokumentasi di Bootstrap kemudian memodifikasi tampilannya dan menyesuaikan attribut elemen sesuai dengan Django `UserCrationForm`.
3. Mengubah tampilan `main` menggunakan `Card` untuk setiap item yang disimpan di invetory
4. Mengubah tampilan `add new product` 
