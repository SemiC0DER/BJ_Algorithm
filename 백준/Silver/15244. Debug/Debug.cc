#include <iostream>
using namespace std;
typedef long long ll;

int N, K, Q;
ll cnt[1000001];
ll psum[1000000];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin >> N >> K;
	while (K--) {
		int x; cin >> x;
		cnt[x]++;
	}

	for (int i = 1; i <= N; i++) {
		ll& curcnt = cnt[i];
		if (curcnt) {
			for (int k = 0; k < N; k += i) psum[k] += curcnt;
		}
	}

	for (int i = 1; i < N; i++) psum[i] += psum[i - 1];

	cin >> Q;
	while (Q--) {
		int L, R; cin >> L >> R;
		ll ans;
		if (L) cout << psum[R] - psum[L - 1] << '\n';
		else cout << psum[R] << '\n';
	}
}