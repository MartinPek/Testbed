#include <iostream>
using namespace std;
#include <stdio.h>
#include <string.h>

char rcvd[] = "!Relay_1_1\n!line_2_2\nline_3_3";

int main() {

  char delimiter[2] = "_";
  int lineCnt = 0;
  char* line = strtok(rcvd, "\n"); 
  
  while (line != NULL) {
    lineCnt++;
    line = strtok(NULL, "\n");
  }

  cout << "v12312" << endl;
  cout << "lineCnt is: " << lineCnt << endl;
  line = rcvd;
  int lineLenght = 0;

  for (int lineNo = 0; lineNo < lineCnt; lineNo++) {
    lineLenght = strlen(line);
    cout << "line is: " << line << endl;
    cout << "lineNo is: " << lineNo << endl;
    
    char* splits = strtok(line, delimiter);
    while (splits != NULL) {
      cout << splits << endl;
      splits = strtok(NULL, delimiter);
    }
    
    line += lineLenght + 1;
    cout << "endLoop" << endl;
  }

    /*
    char* splits = strtok(line, delimiter);
    cout << splits << endl;

    line += strlen(line) + 1;
    // line = strtok(line, "\n");
    cout << line << endl;
    break;
    */
}
