#include <bits/stdc++.h>
using namespace std;

#define fastio()                 \
    ios::sync_with_stdio(false); \
    cin.tie(nullptr);
#define int long long
#define all(v) v.begin(), v.end()
#define endl '\n'

string reverseByType(string s)
{
    stack<char> ch, sy;
    int n = s.size();
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        if ((s[i] >= 97) && (s[i] <= 112))
        {
            ch.push(s[i]);
            arr[i] = 1;
        }
        else
        {
            sy.push(s[i]);
            arr[i] = 0;
        }
    }

    cout << ch.size() << " ";
    cout << endl
         << sy.size() << endl;

    for (int i = 0; i < n; i++)
    {
        if (arr[i])
        {
            s[i] = ch.top();
            ch.pop();
        }
        else
        {
            s[i] = sy.top();
            sy.pop();
        }
    }

    return s;
}

int32_t main()
{
    int t;
    t = 1;
    // cin>>t;
    string s;
    cin >> s;
    string ans = reverseByType(s);
    cout << ans << endl;
}