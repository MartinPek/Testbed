#include <iostream>
#include <cstring>

using namespace std;
// strcat
char testString[32] = "";

int main() {
    strcat(testString, "!Relay_3_3");
    cout << testString << endl;
    strcat(testString, "!Relay_6_9");
    cout << testString << endl;
}