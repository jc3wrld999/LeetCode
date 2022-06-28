/**
문자열 s는 s에 동일한 빈도를 가진 두 개의 다른 문자가 없으면 good이라고 합니다.

문자열 s가 주어지면 s를 good으로 만들기 위해 삭제해야 하는 최소 문자 수를 반환합니다.

문자열에서 문자의 빈도는 문자열에 나타나는 횟수입니다. 예를 들어, 문자열 "aab"에서 'a'의 빈도는 2이고 'b'의 빈도는 1입니다.

hint 1. 문자만 삭제할 수 있으므로 빈도가 동일한 문자가 여러 개 있는 경우 하나를 제외한 모든 문자의 빈도를 줄여야 합니다.
hint 2. 증가하지 않는 빈도로 알파벳 문자를 정렬합니다.
hint 3. 알파벳 문자를 반복하고 이전에 나타나지 않은 값에 도달할 때까지 현재 문자의 빈도를 계속 줄입니다.
*/
class Solution {
  public int minDeletions(String s) {
    int[] frequency = new int[26];
    for (char c : s.toCharArray()) {
      frequency[c - 'a']++;
    }
    PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    for (int freq : frequency) {
      if (freq > 0) {
        pq.add(freq);
      }
    }
    int numOfDeletions = 0;
    while (!pq.isEmpty()) {
      int removedFreq = pq.poll();
      if (!pq.isEmpty() && pq.peek() == removedFreq) {
        numOfDeletions++;
        if (removedFreq > 1) {
          pq.add(removedFreq - 1);
        }
      }
    }
    return numOfDeletions;
  }
}