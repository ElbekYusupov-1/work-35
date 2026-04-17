#28-masal
#def isPrime(N) {
 #   if N <= 1 return false;
  #  for (let i = 2; i <= Math.sqrt(N); i++) {
  #      if (N % i === 0) return false;
  #  }
  #  return true;
#}
#// Test
#console.log(isPrime(7)); // true
#console.log(isPrime(8)); // false

#29-misol
function digitCount(K) {
    if (K === 0) return 1;
    return Math.abs(K).toString().length;
}

#30-misol
function digitN(K, N) {
    let str = Math.abs(K).toString();

    if (N > str.length) return -1;

    return Number(str[N - 1]);
}
#31-misol
function isPalindrom(N) {
    let str = Math.abs(N).toString();
    let rev = str.split('').reverse().join('');
    return str === rev;
}

#32-misol
function degToRad(D) {
    return D * Math.PI / 180;
}

#33-misol
function radToDeg(R) {
    return R * 180 / Math.PI;
}
#34-misol
function fact(N) {
    let res = 1;
    for (let i = 1; i <= N; i++) {
        res *= i;
    }
    return res;
}
