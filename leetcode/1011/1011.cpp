class Solution {
public:
    int shipWithinDays(vector<int>& weights, int D) {
        int right = accumulate(weights.begin(), weights.end(), 0);
        int left = max(right / D, *max_element(begin(weights),end(weights)));
        while(left < right){
            int mid = (right + left) / 2;
            if(countDays(weights, mid) > D) left = mid + 1;
            else
                right = mid;
        }
        return left;
    }
    int countDays(vector<int>& weights, int maxWeight) {
        int current = 0, days = 1;
        for(auto wei : weights) {
            current += wei;
            if(current > maxWeight) {
                days++;
                current = wei;
            }
        }
        return days;
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

int stringToInteger(string input) {
    return stoi(input);
}

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> weights = stringToIntegerVector(line);
        getline(cin, line);
        int D = stringToInteger(line);
        
        int ret = Solution().shipWithinDays(weights, D);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}