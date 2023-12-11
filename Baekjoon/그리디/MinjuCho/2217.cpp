#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(void)
{
    int n;
    cin >> n;
    vector<int> ropes(n);
    for (int i=0; i<n; ++i)
    {
        cin >> ropes[i];
    }
    sort(ropes.begin(), ropes.end());

    int result = 0;
    for (int i=n; i>=0; --i)
    {
        result = max(result, (n - i) * ropes[i]);
    }
    cout << result;
}