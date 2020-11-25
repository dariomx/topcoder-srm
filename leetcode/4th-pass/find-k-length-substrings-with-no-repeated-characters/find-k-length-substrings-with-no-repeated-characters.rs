use std::collections::HashMap;
use std::convert::TryFrom;
use std::str;

impl Solution {
    pub fn num_k_len_substr_no_repeats(s: String, k: i32) -> i32 {
        let s = s.as_bytes();
        let k = usize::try_from(k).unwrap();
        let mut cnt = HashMap::new();
        let mut start: usize = 0;
        let mut ans: i32 = 0;
        for end in 0..s.len() {
            let mut win_size = end - start + 1;
            if win_size > k {
                let y = s[start];
                cnt.insert(y, cnt[&y] - 1);
                if cnt[&y] == 0 {
                    cnt.remove(&y);
                }
                start += 1;
                win_size -= 1;
            }
            let x = s[end];
            if cnt.contains_key(&x) {
                cnt.insert(x, cnt[&x] + 1);
            } else {
                cnt.insert(x, 1);
            }
            if win_size == k && cnt.len() == k {
                ans += 1;
            }
        }
        return ans;
    }
}