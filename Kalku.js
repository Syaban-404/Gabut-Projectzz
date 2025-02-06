// Syaban-404 Project

function tambah(a, b) {
    tambah = a + b;

    return tambah
}
function kurang(a, b) {
    kurang = a - b;

    return kurang
}
function kali(a, b) {
    kali = a * b;

    return kali
}
function bagi(a, b) {
    bagi = a / b;

    return bagi
}

var akhir = true;

while(akhir){
    for(i = true; i === true; i++) {
var a = parseInt(prompt("Masukkan Nilai a : "));
var b = parseInt(prompt("Masukkan Nilai b : "));

pilih = prompt("Tambah / Kurang / Kali / Bagi : ");
lowCase = pilih.toLowerCase();

switch (lowCase) {
    case "tambah":
        alert("Hasil : " + tambah(a, b));
        break;
    case "kurang":
        alert("Hasil : " + kurang(a, b));
        break;
    case "kali":
        alert("Hasil : " + kali(a, b));
        break;
    case "bagi":
        if(a !== 0 && b !== 0){
        alert("Hasil : " + bagi(a, b));
        }else{
            alert("Siapa Yang Bolehin Bagi Nol Woi!");
        } break;

    default:
        alert("Error Detected!")
        break;
}

akhir = confirm('Kembali Ke Menu?');
}} alert("Thanks You For Using My Script!")
