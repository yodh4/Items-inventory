**1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming**

Perbedaan *asynchronous programming* dan *synchronous programming* terletak pada proses pengeksekusian program. Jika pada *synchronous programming*, kode akan dieksekusi satu demi satu dari paling atas hingga akhir, hal ini akan menyebabkan program berhenti untuk sementara waktu jika suatu instruksi membutuhkan waktu yang cukup lama untuk diproses. Berbeda dengan *synchronous programming*, *asynchronous programming* memungkinkan kita untuk memproses suatu instruksi tanpa harus menunggu instruksi yang sudah diproses terlebih dahulu selesai. Hal ini dapat membuat program tetap terus berjalan saat terdapat instruksi yang sedang diproses namun belum selesai dieksekusi.

**2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini**

*Event driven programming* adalah sebuah paradigma pemrograman di mana alur dari sebuah program dapat berubah sesuai *event* yang muncul saat program sedang berjalan. *Event* ini dapat muncul berdasarkan input dari pengguna seperti memencet sebuah button, mensubmit sebuah form, dll. Salah satu contoh penerapan *event driven programming* pada tugas ini adalah saat *button* dengan `id` `button_add` pada modal dipencet,*button* ini akan memanggil *function* `addProduct()`.

**3. Jelaskan penerapan asynchronous programming pada AJAX**

Penerapan *asynchronous programming* pada AJAX dilakukan dengan menggunakan `FetchAPI` atau `XMLHttpRequest`. Jika kita menggunakan `FetchAPI`, maka pertama-tama kita harus membuat objek `fetch()` dan mengirimkan `URL` yang akan diminta sebagai argumen. Setelah itu objek `Fetch` akan mengembalikan `Promise` yang memungkinkan kita untuk menangani respon tersebut secara asinkron menggunakan `.then()` untuk menentukan apa yang harus dilakukan saat respon diterima.

**4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan**

Terdapat beberapa perbedaan antara `FetchAPI` dan `JQuery`, `FetchAPI` adalah API bawaan JavaScript modern sementara `JQuery` adalah sebuah library ekseternal JavaScript. Selain itu, `FetchAPI` memiliki sintaks yang lebih modern dengan memanfaatkan `fetch()` dan menggunakan `promise` untuk mengelola respon, sementara itu, `JQuery` memiliki sintaks yang lebih ringkas daripada `FetchAPI` dengan menggunakan metode seperti `&.ajax()`.

Menurut saya, `FetchAPI` dan `JQuery` memiliki kelebihannya sendiri-sendiri dan dapat kita gunakan tergantung keperluan kita. Namun, saya akan memilih menggunakan `FetchAPI` karena pengelolaan asinkron yang lebih terstruktur sehingga lebih mudah dibaca.

**5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**

1. Membuat fungsi `get_product_json` dan menambahkan routing untuk fungsi tersebut
2. Membuat fungsi `create_ajax` dan menambahkan routing untuk fungsi tersebut
3. Membuat struktur `cards` untuk setiap menampilkan item dengan menggunakan`<div class="d-flex grid gap-4 flex-wrap" id="product_cards"></div>`
4. Membuat fungsi asinkron `getProducts()` pada `main.html`
5. Membuat fungsi asinkron `refreshProducts()` pada `main.html`
6. Membuat modal sebagai form untuk menambahkan item
7. Menambahkan button baru untuk menampilkan modal
8. Membuat fungsi `addProduct()` untuk menambahkan item ke database
9. Menambahkan fungi `onClick` pada button `Add Product` pada modal untuk mengeksekusi fungsi `addProduct()`


link aplikasi: 