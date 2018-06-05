class Solution {
    fun splitArray(nums: IntArray, m: Int): Int {
        val N = nums.size
        if (m >= N) {
            return nums.max() ?: 0
        }
        val dp = Array(m) { IntArray(N, { Int.MAX_VALUE }) }
        var index = 0
        nums.fold(0, { acc: Int, n: Int ->
            val result = acc + n
            dp[0][index] = result
            index += 1
            result
        })
        for (i in 1 until m) {
            for (j in i until N) {
                for (k in i - 1 until j) {
                    dp[i][j] = minOf(dp[i][j], maxOf(dp[i - 1][k], dp[0][j] - dp[0][k]))
                }
            }
        }
        return dp.last().last()
    }
}

fun main(args: Array<String>) {
    val solution = Solution()
    println(solution.splitArray(intArrayOf(7, 2, 5, 10, 8), 2))
}
