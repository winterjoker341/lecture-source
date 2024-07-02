use std::io;
use std::cmp;

fn input_vec(vec: &mut Vec<i64>, len: usize) {
	let mut buf = String::new();
	io::stdin().read_line(&mut buf).unwrap();
	let mut tokens = buf.split_whitespace();
	let mut next = || tokens.next().unwrap();
	for _ in 0..len {
		vec.push(next().parse().unwrap());
	}
	buf.clear();
}

fn main() {
	let mut buf = String::new();
	io::stdin().read_line(&mut buf).unwrap();
	let n: usize = buf.trim().parse().unwrap();
	buf.clear();
	let mut	dist: Vec<i64> = Vec::new();
	input_vec(&mut dist, n-1);
	let mut	cost: Vec<i64> = Vec::new();
	input_vec(&mut cost, n);
	let mut mn: i64 = cost[0];
	let mut ans: i64 = 0;
	for i in 1..n {
		ans += mn*dist[i-1];
		mn = cmp::min(mn, cost[i]);
	}
	println!("{}", ans);
}
