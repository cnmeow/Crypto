#include <iostream>
using namespace std;

string encryptCaesar(string plaintext, int shift) {
    string ciphertext = "";
    for (int i = 0; i < plaintext.length(); i++) {
        // Lấy ký tự hàng i, cột j trong bảng chữ cái
        char c = plaintext[i];
        // Kiểm tra nếu là ký tự chữ cái
        if (isalpha(c)) {
            // Xác định ký tự đầu ra bằng cách dịch theo shift pattern
            c = toupper(c); // Chuyển hết về chữ in hoa
            c = (((c - 65) + shift) % 26) + 65; // Áp dụng shift pattern
        }
        ciphertext += c; // Thêm ký tự mới vào ciphertext
    }
    return ciphertext;
}

int main() {
    // Nhập plaintext và shift pattern từ bàn phím
    string plaintext;
    int shift;
    cout << "Nhap vao plaintext: ";
    getline(cin, plaintext);
    cout << "Nhap vao shift pattern: ";
    cin >> shift;
    // Mã hóa Caesar và in kết quả ra màn hình
    string ciphertext = encryptCaesar(plaintext, shift);
    cout << "Ciphertext la: " << ciphertext;
    return 0;
}
