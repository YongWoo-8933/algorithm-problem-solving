"""
백준 14562 태권왕 (실버 1)

1. 평범한 BFS풀이 진행
"""

fun main() = with(System.`in`.bufferedReader()) {
    repeat(readLine().toInt()) {
        val (S, T) = readLine().split(" ").map{ it.toInt() }
        val q = ArrayDeque<IntArray>(listOf(intArrayOf(0, S, T)))
        while(q.isNotEmpty()) {
            val (cnt, s, t) = q.removeFirstOrNull()!!
            if(s==t) {
                println(cnt)
                break
            }
            // 두배발차기
            if(s*2<=t+3) q.addLast(intArrayOf(cnt+1, s*2, t+3))
            // 1점 발차기
            q.addLast(intArrayOf(cnt+1, s+1, t))
        }
    }
}