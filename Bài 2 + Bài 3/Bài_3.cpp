#include <iostream>
#include <string>
using namespace std;

// Hàm thực hiện mã hóa ROT13
string encrypt(string message) {
    string result = "";
    // Duyệt qua các ký tự trong thông điệp
    for (int i = 0; i < message.length(); i++) {
        // Nếu ký tự là chữ cái in hoa
        if (message[i] >= 'A' && message[i] <= 'Z') {
            result += char(((message[i] - 'A') + 13) % 26 + 'A');
        }
        // Nếu ký tự là chữ cái thường
        else if (message[i] >= 'a' && message[i] <= 'z') {
            result += char(((message[i] - 'a') + 13) % 26 + 'a');
        }
        // Nếu ký tự không phải chữ cái thì giữ nguyên
        else {
            result += message[i];
        }
    }
    return result;
}

// Hàm thực hiện giải mã thông điệp đã được mã hóa bằng ROT13
string decrypt(string message) {
    // ROT13 là phép mã hóa và giải mã cùng một độ dịch, vì vậy ta chỉ cần áp dụng hàm mã hóa lại cho thông điệp cần giải mã
    return encrypt(message);
}

int main() {
    cout << "Original message: ";
    string message;
    getline(cin, message);
    string encrypted = encrypt(message);
    string decrypted = decrypt(encrypted);
    cout << "Encrypted message: " << encrypted << endl;
    cout << "Decrypted message: " << decrypted << endl;
    return 0;
}
