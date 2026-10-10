"""

void primes_up_to(int k){
	if(k<=0) return 0;
	vector<bool> sieve;
	for(int i=0;i<=k;i++){
		sieve.push_back(true);
	}
	sieve[0] = sieve[1] = false;

	for(int i=2;i<=sqrt(k);i++){
		if(sieve[i]){
			for(int j=i*i;j<=k;j+=i){
				sieve[j] = false;
			}
		}
	}

	vector<int> r;
	for(int i=2;i<=k;i++){
		if(sieve[i]){
			r.push_back(i);
		}
	}

	for(int i=0;i<r.size();i++) cout<<r[i]<<" ";
}

"""

def primes_up_to(k: int) -> list[int]:
	if k<=0 : return []
	sieve = []
	for i in range(k+1):
		sieve.append(True);
	sieve[0] = sieve[1] = False

	for i in range(2, int(k**0.5)+1):
		if sieve[i]:
			for j in range(i*i, k+1, i):
				sieve[j] = False

	r = []
	for i in range(2, k+1):
		if sieve[i]:
			r.append(i)

	return r
