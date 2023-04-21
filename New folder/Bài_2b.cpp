#include <iostream>
using namespace std;

string decryptCaesar(string ciphertext, int shift) {
    string plaintext = "";
    for (int i = 0; i < ciphertext.length(); i++) {
        // Lấy ký tự hàng i, cột j trong bảng chữ cái
        char c = ciphertext[i];
        // Kiểm tra nếu là ký tự chữ cái
        if (isalpha(c)) {
            // Xác định ký tự đầu ra bằng cách dịch ngược theo shift pattern
            c = toupper(c); // Chuyển hết về chữ in hoa
            c = (((c - 65) - shift + 26) % 26) + 65; // Áp dụng shift pattern
        }
        plaintext += c; // Thêm ký tự mới vào plaintext
    }
    return plaintext;
}

int main() {
    // Nhập ciphertext từ bàn phím
    string ciphertext;
    cout << "Nhap vao ciphertext: ";
    getline(cin, ciphertext);
    // Thử giải mã với các shift pattern từ 1 đến 25 và in kết quả
    for (int i = 0; i < 26; i++) {
        cout << "Shift pattern " << i << ": " << decryptCaesar(ciphertext, i) << endl;
    }
    return 0;
}