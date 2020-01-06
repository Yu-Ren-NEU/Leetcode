/*
 * @Description: TO-BE-ADDED
 * @Company: YUSUR. Copyright(c) All rights reserved
 * @Author: Yihao Wang
 * @Date: 2020-01-06 18:05:36
 * @LastEditors: Yihao Wang
 * @LastEditTime: 2020-01-06 18:07:32
 */
class Solution {
public:
    bool isMatch(string s, string p) {
        int s_len = s.length(), p_len = p.length();
        vector<vector<bool> > f(s_len+1, vector<bool>(p_len+1, false));
        f[0][0] = true;
        //for(int i=1;i<=s_len;i++) {
        //    f[i][0] = false;
        //}
        for(int j=1;j<=p_len;j++) {
            f[0][j] = j > 1 && p[j-1] == '*' && f[0][j-2];
        }
        for(int i=1;i<=s_len;i++)
            for(int j=1;j<=p_len;j++)
            {
                if(p[j-1] != '*') {
                    if(s[i-1] == p[j-1] || p[j-1] == '.')
                        f[i][j] = f[i-1][j-1];
                }
                else {
                    if(f[i][j-2]) {
                        f[i][j] = true;
                        continue;
                    }
                    if(s[i-1] == p[j-2] || p[j-2] == '.') 
                        f[i][j] = f[i-1][j];
                }
            }
        return f[s_len][p_len];
    }
};

string stringToString(string input) {
    assert(input.length() >= 2);
    string result;
    for (int i = 1; i < input.length() -1; i++) {
        char currentChar = input[i];
        if (input[i] == '\\') {
            char nextChar = input[i+1];
            switch (nextChar) {
                case '\"': result.push_back('\"'); break;
                case '/' : result.push_back('/'); break;
                case '\\': result.push_back('\\'); break;
                case 'b' : result.push_back('\b'); break;
                case 'f' : result.push_back('\f'); break;
                case 'r' : result.push_back('\r'); break;
                case 'n' : result.push_back('\n'); break;
                case 't' : result.push_back('\t'); break;
                default: break;
            }
            i++;
        } else {
          result.push_back(currentChar);
        }
    }
    return result;
}

string boolToString(bool input) {
    return input ? "True" : "False";
}

int main() {
    string line;
    while (getline(cin, line)) {
        string s = stringToString(line);
        getline(cin, line);
        string p = stringToString(line);
        
        bool ret = Solution().isMatch(s, p);

        string out = boolToString(ret);
        cout << out << endl;
    }
    return 0;
}