# Leetcode解题分类
---

* 算法思想
    * 二分查找
        1. [No.33](https://leetcode.com/problems/search-in-rotated-sorted-array)
        2. [No.34](https://leetcode.com/problems/search-for-a-range) 分别二分查找范围的start和end
        3. [No.81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii) 去掉重复的元素，然后就和No.33一样了
        4. [No.153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array)
        5. [No.162](https://leetcode.com/problems/find-peak-element) 对index做二分
        6. [No.287](https://leetcode.com/problems/find-the-duplicate-number/description) n+1个数，范围为a~(n-a+1)，在a~(n-a+1)范围内做二分
        7. [No.378](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)
        8. [No.522](https://leetcode.com/problems/longest-uncommon-subsequence-ii) 利用二分查找来判断是否是子序列
        9. [No.524](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting) 同[No.522](https://leetcode.com/problems/longest-uncommon-subsequence-ii)
        10. [No.540](https://leetcode.com/problems/single-element-in-a-sorted-array)
        11. [No.658](https://leetcode.com/problems/find-k-closest-elements)
        12. [No.729](https://leetcode.com/problems/my-calendar-i) 因为是在线算法，所以不适合使用排序
        13. [No.731](https://leetcode.com/problems/my-calendar-ii) 同No.729，或者使用括号匹配的类似算法
        14. [No.792](https://leetcode.com/problems/number-of-matching-subsequences) 利用二分查找来判断是否是子序列
        15. [No.826](https://leetcode.com/problems/most-profit-assigning-work)
    * 贪心思想
        1. [No.11](https://leetcode.com/problems/container-with-most-water) 遍历容器的两条垂直边，每次移动较小的那一边
        2. [No.659](https://leetcode.com/problems/split-array-into-consecutive-subsequences)
        3. [No.781](https://leetcode.com/problems/rabbits-in-forest) 注意几点：1)一只兔子回答n，则代表和它同色的兔子共有n+1只(包括这只兔子) 2)我们要把相同回答的兔子归成同一颜色，但总数不超过n+1(n为这些兔子的回答)
        4. [No.822](https://leetcode.com/problems/card-flipping-game) 如果一张牌的正反面都为n，则n不可能为结果
    * 2-pointer
        * 滑动窗口
            1. [No.3](https://leetcode.com/problems/longest-substring-without-repeating-characters) 用flag存储窗口内元素出现的次数
            2. [No.11](https://leetcode.com/problems/container-with-most-water) 遍历容器的两条垂直边，每次移动较小的那一边
            3. [No.209](https://leetcode.com/problems/minimum-size-subarray-sum)
            4. [No.413](https://leetcode.com/problems/arithmetic-slices)
            5. [No.424](https://leetcode.com/problems/longest-repeating-character-replacement)
            6. [No.467](https://leetcode.com/problems/unique-substrings-in-wraparound-string)
            7. [No.495](https://leetcode.com/problems/teemo-attacking)
            8. [No.567](https://leetcode.com/problems/permutation-in-string) 滑动计数
            9. [No.678](https://leetcode.com/problems/valid-parenthesis-string) 用一个cnt可以判断不含“*”的括号表达式是否合法，在含有“*”的表达式，用lo和hi表示cnt的取值范围，最后看0是否在取值范围内
            10. [No.713](https://leetcode.com/problems/subarray-product-less-than-k) 向前推进右边界，移动左边界去适配右边界
            11. [No.769](https://leetcode.com/problems/max-chunks-to-make-sorted) 如果`min(arr[i,j+1])=i and max(arr[i,j+1])=j`则可以分块
            12. [No.795](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum)
            13. [No.825](https://leetcode.com/problems/friends-of-appropriate-ages)
        * 多数求和
            1. [No.15](https://leetcode.com/problems/3sum) 排序，遍历最大值，其余两值用2-pointer
            2. [No.16](https://leetcode.com/problems/3sum-closest) 和No.15一样
            3. [No.18](https://leetcode.com/problems/4sum) 排序，遍历最大值和最小值，其余两值用2-pointer
            4. [No.611](https://leetcode.com/problems/valid-triangle-number) 同[No.15](https://leetcode.com/problems/3sum)
    * 排序
        * 快速排序
            1. [No.179](https://leetcode.com/problems/largest-number) cmp(x, y)=-1 if str(x)+str(y)>str(y)+str(x) else 1
            2. [No.274](https://leetcode.com/problems/h-index)
            3. [No.275](https://leetcode.com/problems/h-index-ii) 同[No.274](https://leetcode.com/problems/h-index)
            4. [No.435](https://leetcode.com/problems/non-overlapping-intervals) 按end排序
            5. [No.436](https://leetcode.com/problems/find-right-interval) 同[No.435](https://leetcode.com/problems/non-overlapping-intervals)
            6. [No.452](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons) 同[No.435](https://leetcode.com/problems/non-overlapping-intervals)
            7. [No.539](https://leetcode.com/problems/minimum-time-difference)
            8. [No.593](https://leetcode.com/problems/valid-square) 排序之后各点关系就确定了
            9. [No.763](https://leetcode.com/problems/partition-labels) 记录每个字符第一次出现和最后一次出现的位置，按第一次出现的位置排序，类似于求overlapping interval。
        * 堆排序
            1. [No.215](https://leetcode.com/problems/kth-largest-element-in-an-array) 堆的大小为215，计算最大值用最小堆
            2. [No.347](https://leetcode.com/problems/top-k-frequent-elements)
            3. [No.373](https://leetcode.com/problems/find-k-pairs-with-smallest-sums)
            4. [No.692](https://leetcode.com/problems/top-k-frequent-words)
        * 桶排序
            1. [No.220](https://leetcode.com/problems/contains-duplicate-iii) 差不大于t，则桶的大小为t，和相邻的桶内元素比较即可
        * 计数排序
            1. [No.75](https://leetcode.com/problems/sort-colors)
            2. [No.791](https://leetcode.com/problems/custom-sort-string)
    * 搜索
        * BFS
            1. [No.102](https://leetcode.com/problems/binary-tree-level-order-traversal) 层次遍历
            2. [No.103](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal) 同[No.102](https://leetcode.com/problems/binary-tree-level-order-traversal)
            3. [No.116](https://leetcode.com/problems/populating-next-right-pointers-in-each-node) 层次遍历
            4. [No.117](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii) 同[No.116](https://leetcode.com/problems/populating-next-right-pointers-in-each-node)
            5. [No.127](https://leetcode.com/problems/word-ladder) 按要求通过一系列转换从一个值变为另外一个值，可以将转换关系理解为图中的相连节点。
            6. [No.130](https://leetcode.com/problems/surrounded-regions)
            7. [No.133](https://leetcode.com/problems/clone-graph) 利用map存储新节点与对应源节点的映射，复制点与点之间的关系
            8. [No.199](https://leetcode.com/problems/binary-tree-right-side-view)
            9. [No.200](https://leetcode.com/problems/number-of-islands) 计算有多少连通分量
            10. [No.211](https://leetcode.com/problems/add-and-search-word-data-structure-design)
            11. [No.222](https://leetcode.com/problems/count-complete-tree-nodes)
            12. [No.310](https://leetcode.com/problems/minimum-height-trees) 计算最长路径。从任一点a出发，找到离a最远的点b，再从b出发，找到离b最远的点c，搜索过程中记录下路径p。结果为p最中间的一个或两个点。
            13. [No.331](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree)
            14. [No.399](https://leetcode.com/problems/evaluate-division) 转换为图来做，先计算一个点到其他各个点的值，即分子相同，分母不同，在用除法计算出结果。
            15. [No.417](https://leetcode.com/problems/pacific-atlantic-water-flow)
            16. [No.433](https://leetcode.com/problems/minimum-genetic-mutation)
            17. [No.449](https://leetcode.com/problems/serialize-and-deserialize-bst)
            18. [No.513](https://leetcode.com/problems/find-bottom-left-tree-value)
            19. [No.515](https://leetcode.com/problems/find-largest-value-in-each-tree-row)
            20. [No.547](https://leetcode.com/problems/friend-circles)
            21. [No.623](https://leetcode.com/problems/add-one-row-to-tree)
            22. [No.655](https://leetcode.com/problems/print-binary-tree)
            23. [No.662](https://leetcode.com/problems/maximum-width-of-binary-tree) 使用数组存储完全二叉树中父节点与子节点的序号关系
            24. [No.752](https://leetcode.com/problems/open-the-lock)
            25. [No.787](https://leetcode.com/problems/cheapest-flights-within-k-stops)
            26. [No.797](https://leetcode.com/problems/all-paths-from-source-to-target)
            27. [No.808](https://leetcode.com/problems/soup-servings)
        * DFS
            1. [No.79](https://leetcode.com/problems/word-search)
            2. [No.94](https://leetcode.com/problems/binary-tree-inorder-traversal)
            3. [No.114](https://leetcode.com/problems/flatten-binary-tree-to-linked-list) 前序遍历
            4. [No.113](https://leetcode.com/problems/path-sum-ii)
            5. [No.199](https://leetcode.com/problems/binary-tree-right-side-view)
            6. [No.230](https://leetcode.com/problems/kth-smallest-element-in-a-bst)
            7. [No.236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree) LCA问题
            8. [No.310](https://leetcode.com/problems/minimum-height-trees) 计算最长路径。从任一点a出发，找到离a最远的点b，再从b出发，找到离b最远的点c，搜索过程中记录下b到c的路径p。结果为p最中间的一个或两个点。
            9. [No.331](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree)
            10. [No.332](https://leetcode.com/problems/reconstruct-itinerary)
            11. [No.473](https://leetcode.com/problems/matchsticks-to-square)
            12. [No.494](https://leetcode.com/problems/target-sum)
            13. [No.508](https://leetcode.com/problems/most-frequent-subtree-sum)
            14. [No.638](https://leetcode.com/problems/shopping-offers)
            15. [No.698](https://leetcode.com/problems/partition-to-k-equal-sum-subsets)
            16. [No.814](https://leetcode.com/problems/binary-tree-pruning)
        * Backtracking
            1. [No.91](https://leetcode.com/problems/decode-ways)
            2. [No.93](https://leetcode.com/problems/restore-ip-addresses)
            3. [No.95](https://leetcode.com/problems/unique-binary-search-trees-ii) 遍历当前树的根节点，分别生成左子树和右子树
            4. [No.96](https://leetcode.com/problems/unique-binary-search-trees) 同[No.95](https://leetcode.com/problems/unique-binary-search-trees-ii)
            5. [No.98](https://leetcode.com/problems/validate-binary-search-tree) 分别校验左右子树，然后校验左子树的最大值和右子树的最小值
            6. [No.241](https://leetcode.com/problems/different-ways-to-add-parentheses)
            7. [No.386](https://leetcode.com/problems/lexicographical-numbers)
            8. [No.416](https://leetcode.com/problems/partition-equal-subset-sum)
            9. [No.526](https://leetcode.com/problems/beautiful-arrangement)
            10. [No.553](https://leetcode.com/problems/optimal-division)
            11. [No.738](https://leetcode.com/problems/monotone-increasing-digits)
            12. [No.756](https://leetcode.com/problems/pyramid-transition-matrix)
    * 分治
        1. [No.95](https://leetcode.com/problems/unique-binary-search-trees-ii) 遍历当前树的根节点，分别生成左子树和右子树
        2. [No.96](https://leetcode.com/problems/unique-binary-search-trees) 同[No.95](https://leetcode.com/problems/unique-binary-search-trees-ii)
        3. [No.98](https://leetcode.com/problems/validate-binary-search-tree) 分别校验左右子树，然后校验左子树的最大值和右子树的最小值
        4. [No.105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) 已知前序中序构造树
        5. [No.106](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal) 已知中序后序构造树
        6. [No.109](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree) 每次都平分左右子树
        7. [No.131](https://leetcode.com/problems/palindrome-partitioning)
        8. [No.148](https://leetcode.com/problems/sort-list) 归并排序
        9. [No.654](https://leetcode.com/problems/maximum-binary-tree)
    * DP
        * 图DP
            * 路径数
                1. [No.62](https://leetcode.com/problems/unique-paths)
                2. [No.63](https://leetcode.com/problems/unique-paths-ii)
            * 路径和
                1. [No.64](https://leetcode.com/problems/minimum-path-sum)
                2. [No.120](https://leetcode.com/problems/triangle) 金字塔形结构，从底向上，逐层规约
        * 最长递增子序列(子串)
            1. [No.300](https://leetcode.com/problems/longest-increasing-subsequence)
            2. [No.646](https://leetcode.com/problems/maximum-length-of-pair-chain)
            3. [No.673](https://leetcode.com/problems/number-of-longest-increasing-subsequence)
        * 最长公共子序列(子串)
            1. [No.583](https://leetcode.com/problems/delete-operation-for-two-strings) 转换为最长公共子序列来做。
            2. [No.718](https://leetcode.com/problems/maximum-length-of-repeated-subarray) 最长公共子串 DP[i][j]代表s1[:i],s2[:j]以s[i-1]和s[j-1]结尾的公共子串长度，`DP[i][j]=D[i-1][j-1]+1 if s[i-1]==s[j-1] else 0`
        * 最近公共祖先
            1. [No.236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree)
        * 0-1背包
            1. [No.416](https://leetcode.com/problems/partition-equal-subset-sum)
            2. [No.474](https://leetcode.com/problems/ones-and-zeroes) 两个维度上的0-1背包
        * 完全背包
            1. [No.322](https://leetcode.com/problems/coin-change)
            2. [No.518](https://leetcode.com/problems/coin-change-2)
            3. [No.638](https://leetcode.com/problems/shopping-offers)
        * 树形DP
            1. [No.337](https://leetcode.com/problems/house-robber-iii)
        * 字符串编辑
            1. [No.583](https://leetcode.com/problems/delete-operation-for-two-strings) DP[i][j]代表word1[:i]和word2[:j]的最小删除次数，`DP[i][j]=DP[i - 1][j - 1] if word1[i-1]==word2[j-1] else min(1+DP[i-1][j], 1+DP[i][j-1], 2+DP[i-1][j-1])`
            2. [No.712](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings) 类似于[No.583](https://leetcode.com/problems/delete-operation-for-two-strings)
        * 回文子序列(子串)
	        1. [No.5](https://leetcode.com/problems/longest-palindromic-substring)
	        2. [No.516](https://leetcode.com/problems/longest-palindromic-subsequence)
        * 整数分割
        * 字符串(数组)分割
            1. [No.139](https://leetcode.com/problems/word-break)
            2. [No.813](https://leetcode.com/problems/largest-sum-of-averages) DP[i][j]表示A[:j+1]分成i份后的最大平均和，`DP[i][j]=max(DP[i-1][k]+sum(A[k+1:j+1])/(j- k) for k in range(i-1, j))`
        * 状态机
            1. [No.309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) 关键是初始值
            2. [No.714](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) 类似于[No.309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown)
        * 线性DP
            1. [No.343](https://leetcode.com/problems/integer-break) DP[i]代表n = i时的结果
            2. [No.368](https://leetcode.com/problems/largest-divisible-subset) DP[i]代表以nums[i]结尾的序列，`DP[i]=max([(*DP[j], nums[i]) for j in range(i-1, -1, -1) if nums[i]%nums[j]==0], key=lambda x: len(x), default=(nums,)))`
            3. [No.376](https://leetcode.com/problems/wiggle-subsequence) 要做两次DP，波动方向有两种
            4. [No.377](https://leetcode.com/problems/combination-sum-iv)
            5. [No.397](https://leetcode.com/problems/integer-replacement) 用递归自顶向下比较快
            6. [No.486](https://leetcode.com/problems/predict-the-winner) DP[i][j]表示一名玩家在先手情况能从nums[i:j+1]数组中取得最大分数
            7. [No.740](https://leetcode.com/problems/delete-and-earn) 先计数，在对每个值做DP
            8. [No.790](https://leetcode.com/problems/domino-and-tromino-tiling) `DP[n]=DP[n-1]+DP[n-2]+2*(DP[n-3]+...+DP[0])=2*DP[n-1]+DP[n-3]`
            9. [No.801](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing) `DP[n]=(a,b) (a:如果此处不交换需要的次数，b:如果此处交换需要的次数)`
            10. [No.823](https://leetcode.com/problems/binary-trees-with-factors) `DP[n]=sum(DP[i]*DP[j]) (i in A and j in A and i*j==n)`
        * 其他
		    1. [No.152](https://leetcode.com/problems/maximum-product-subarray)
		    2. [No.213](https://leetcode.com/problems/house-robber-ii)
		    3. [No.221](https://leetcode.com/problems/maximal-square) DP数组中的DP[i][j]代表了以（i，j）为右下角的square的边长。所以当matrix[i][j]==1时，`DP[i][j]=min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1])`,因为这三者中有一个为0时，matrix[i][j]并不能使某个square扩大。而这三者大于0，只能是其中最小值所在的square扩大。
		    4. [No.264](https://leetcode.com/problems/ugly-number-ii) 丑数
		    5. [No.279](https://leetcode.com/problems/perfect-squares) 满足条件的组合
            6. [No.313](https://leetcode.com/problems/super-ugly-number) 泛化丑数
            7. [No.322](https://leetcode.com/problems/coin-change)
            8. [No.375](https://leetcode.com/problems/guess-number-higher-or-lower-ii) DP[i][j]表示i...j的最优结果，有`DP[i][j]=min(k+max(DP[i][k-1],DP[k+1][j] for k in range(i,j+1))) if j>i else 0`
            9. [No.395](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters) 如果出现次数最少的字符出现次数大于k则字符串符合条件，否则递归地以该字符分割字符串去做判断
            10. [No.542](https://leetcode.com/problems/01-matrix) 二维矩阵DP，先从左上角向右下角做DP，再反向做一次
            11. [No.576](https://leetcode.com/problems/out-of-boundary-paths) 同时朝各个方向做BFS，每次都刷新矩阵
            12. [No.688](https://leetcode.com/problems/knight-probability-in-chessboard) 同[No.576](https://leetcode.com/problems/out-of-boundary-paths)
            13. [No.764](https://leetcode.com/problems/largest-plus-sign)
            14. [No.799](https://leetcode.com/problems/champagne-tower)
    * 数学
        * 素数
        * 多数投票
            1. [No.229](https://leetcode.com/problems/majority-element-ii) 典型投票问题
        * 相遇问题
        * 排列组合
            1. [No.17](https://leetcode.com/problems/letter-combinations-of-a-phone-number) 生成组合
            2. [No.22](https://leetcode.com/problems/generate-parentheses) 生成排列
            3. [No.31](https://leetcode.com/problems/next-permutation) 计算排列组合中的下一个
            4. [No.39](https://leetcode.com/problems/combination-sum) 生成组合求和
            5. [No.40](https://leetcode.com/problems/combination-sum-ii) 同[No.39](https://leetcode.com/problems/combination-sum)
            6. [No.46](https://leetcode.com/problems/permutations) 排列
            7. [No.47](https://leetcode.com/problems/permutations-ii) 排列
            8. [No.60](https://leetcode.com/problems/permutation-sequence) 计算排列组合中的任意一个。以n为第一位数排列组合有(n-1)！种，且第一位越大则这个排列越大，以此类推。类似于动态进制。
            9. [No.62](https://leetcode.com/problems/unique-paths) 可以理解为变形的排列组合问题，所有Right和Down排列之后去除相对顺序错误的那些组合。
            10. [No.77](https://leetcode.com/problems/combinations) 组合
            11. [No.78](https://leetcode.com/problems/subsets) 同[No.77](https://leetcode.com/problems/combinations)
            12. [No.90](https://leetcode.com/problems/subsets-ii) 同[No.78](https://leetcode.com/problems/subsets)
            13. [No.216](https://leetcode.com/problems/combination-sum-iii) 组合
            14. [No.357](https://leetcode.com/problems/count-numbers-with-unique-digits) 不同的数即为首位不为0的组合数
            15. [No.556](https://leetcode.com/problems/next-greater-element-iii) 同[No.31](https://leetcode.com/problems/next-permutation)
        * 其他
            1. [No.29](https://leetcode.com/problems/divide-two-integers) 用减法模拟除法，用快速幂的方式加快速度
            2. [No.50](https://leetcode.com/problems/powx-n) 快速幂
            3. [No.166](https://leetcode.com/problems/fraction-to-recurring-decimal) 模拟手工除法计算
            4. [No.319](https://leetcode.com/problems/bulb-switcher) 开关灯问题
            5. [No.365](https://leetcode.com/problems/water-and-jug-problem) 泊松分酒
            6. [No.372](https://leetcode.com/problems/super-pow) 快速幂
            7. [No.390](https://leetcode.com/problems/elimination-game) 每次删数只关注第一个数字的变化即可
            8. [No.396](https://leetcode.com/problems/rotate-function) F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]，F(k+1) = Sum(Bk) - n * Bk[n-1]
            9. [No.423](https://leetcode.com/problems/reconstruct-original-digits-from-english) 解方程
            10. [No.462](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii) 把所有数字都变成**中位数**
            11. [No.554](https://leetcode.com/problems/brick-wall) 对每个wall做accumulate，统计出现频数
            12. [No.640](https://leetcode.com/problems/solve-the-equation) 模拟解方程
            13. [No.670](https://leetcode.com/problems/maximum-swap) 总高位向地位遍历，如果某一位数字的低位有比它打的数，则这一位数字需要交互位置，要与低位中最大的且最低位的数字交换即可
            14. [No.672](https://leetcode.com/problems/bulb-switcher-ii) 不太懂
    * 其他算法
        * 巧用hashmap
            1. [No.454](https://leetcode.com/problems/4sum-ii)
            2. [No.523](https://leetcode.com/problems/continuous-subarray-sum) 若sum(0...i)%k=n，有j>i，sum(0...j)%k=n，则可知sum(i+1...j)是k的倍数。此题中需要j>i+1。
            3. [No.525](https://leetcode.com/problems/contiguous-array) 类似于523，若sum(0...i)=[x1, y1] (x1是0的个数，y1是1的个数)，若有j>i，sum(0...j)=[x2, y2]，且y2-x2=y1-x2，则可知sum(i+1...j)=[x, y]，其中x=y
            4. [No.560](https://leetcode.com/problems/subarray-sum-equals-k) 若sum(0...i)=n，有j>i，sum(0...j)-k=n，则可知sum(i+1...j)=k。
        * Manacher算法
            1. [No.5](https://leetcode.com/problems/longest-palindromic-substring)
* 数据结构
    * 字符串
        * 普通字符串操作
            1. [No.8](https://leetcode.com/problems/string-to-integer-atoi)
            2. [No.13](https://leetcode.com/problems/roman-to-integer)
            3. [No.49](https://leetcode.com/problems/group-anagrams)
            4. [No.89](https://leetcode.com/problems/gray-code) G(n)=['0'+G(n-1), '1'+reversed(G(n-1))]
            5. [No.151](https://leetcode.com/problems/reverse-words-in-a-string)
            6. [No.165](https://leetcode.com/problems/compare-version-numbers)
            7. [No.187](https://leetcode.com/problems/repeated-dna-sequences) 长度固定，用hashmap找重复即可
            8. [No.299](https://leetcode.com/problems/bulls-and-cows)
            9. [No.306](https://leetcode.com/problems/additive-number)
            10. [No.318](https://leetcode.com/problems/maximum-product-of-word-lengths)
            11. [No.809](https://leetcode.com/problems/expressive-words)
            12. [No.816](https://leetcode.com/problems/ambiguous-coordinates)
        * 字符串模拟大数运算
            1. [No.43](https://leetcode.com/problems/multiply-strings) 按四位进行分块，加快运行速度
    * 链表
        * 快慢指针
            1. [No.19](https://leetcode.com/problems/remove-nth-node-from-end-of-list)
            2. [No.142](https://leetcode.com/problems/linked-list-cycle-ii) 一个指针一次走两步，一个一次走一步。
        * 普通链表操作
            1. No.2：链表操作模拟加法
            2. [No.24](https://leetcode.com/problems/swap-nodes-in-pairs)
            3. [No.61](https://leetcode.com/problems/rotate-list)
            4. [No.92](https://leetcode.com/problems/reverse-linked-list-ii)
            5. [No.138](https://leetcode.com/problems/copy-list-with-random-pointer)
            6. [No.147](https://leetcode.com/problems/insertion-sort-list) 插入排序
            7. [No.148](https://leetcode.com/problems/sort-list) 归并排序
            8. [No.328](https://leetcode.com/problems/odd-even-linked-list)
            9. [No.725](https://leetcode.com/problems/split-linked-list-in-parts) 计算一下平均长度即可
    * 位操作
        1. [No.137](https://leetcode.com/problems/single-number-ii) 只有一个数字出现n次，其余数字均出现m次，m>n。用多个二进制位表示一个二进制位出现的次数，计算出推导式即可。
        2. [No.201](https://leetcode.com/problems/bitwise-and-of-numbers-range) 除了m和n高位相同的部分，其余都为0
        3. [No.260](https://leetcode.com/problems/single-number-iii) 两个数出现奇数次，其余都为偶数次。逐个异或获得m，找到m中最右的1，其余位置0，获得n。将n再次与所有数以此做与，按结果是否为0分成两组做异或，即得结果。
        4. [No.338](https://leetcode.com/problems/counting-bits) 二进制技巧
        5. [No.477](https://leetcode.com/problems/total-hamming-distance) 每一位的总hamming距离为`1的个数 * 0的个数`
    * 栈
        1. [No.71](https://leetcode.com/problems/simplify-path)
        2. [No.143](https://leetcode.com/problems/reorder-list)
        3. [No.150](https://leetcode.com/problems/evaluate-reverse-polish-notation) 逆波兰式
        4. [No.173](https://leetcode.com/problems/binary-search-tree-iterator)
        5. [No.227](https://leetcode.com/problems/basic-calculator-ii)
        6. [No.341](https://leetcode.com/problems/flatten-nested-list-iterator)
        7. [No.385](https://leetcode.com/problems/mini-parser)
        8. [No.388](https://leetcode.com/problems/longest-absolute-file-path)
        9. [No.394](https://leetcode.com/problems/decode-string)
        10. [No.402](https://leetcode.com/problems/remove-k-digits) 最后的结果是个递增(>=)序列
        11. [No.445](https://leetcode.com/problems/add-two-numbers-ii)
        12. [No.456](https://leetcode.com/problems/132-pattern)
        13. [No.503](https://leetcode.com/problems/next-greater-element-ii) `next greater element`类型的题目，`小技巧：数组可以循环，可以循环两倍的数组长度`
        14. [No.636](https://leetcode.com/problems/exclusive-time-of-functions)
        15. [No.735](https://leetcode.com/problems/asteroid-collision)
        16. [No.739](https://leetcode.com/problems/daily-temperatures) `next greater element`类型的题目
    * 队列
        * 优先队列
            1. [No.621](https://leetcode.com/problems/task-scheduler) 排队系列
            2. [No.767](https://leetcode.com/problems/reorganize-string) 排队系列
    * 数组和矩阵
        * 普通数组和矩阵操作
            1. [No.6](https://leetcode.com/problems/zigzag-conversion)
            2. [No.36](https://leetcode.com/problems/valid-sudoku) 分别校验行，列和块
            3. [No.48](https://leetcode.com/problems/rotate-image) 先将每列逆置，然后沿对角线做对称
            4. [No.54](https://leetcode.com/problems/spiral-matrix)
            5. [No.55](https://leetcode.com/problems/jump-game)
            6. [No.56](https://leetcode.com/problems/merge-intervals) 按start排序
            7. [No.59](https://leetcode.com/problems/spiral-matrix-ii)
            8. [No.73](https://leetcode.com/problems/set-matrix-zeroes)
            9. [No.74](https://leetcode.com/problems/search-a-2d-matrix) 从左下角或者右上角开始，类似于BST
            10. [No.80](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii)
            11. [No.82](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii)
            12. [No.134](https://leetcode.com/problems/gas-station) 关键点在于如果车从i出发最远能到达j，那么从i到j出发都最远只能到达j，因为从i出发到达i+1至j中的任意一点时油量都>=0
            13. [No.228](https://leetcode.com/problems/summary-ranges)
            14. [No.238](https://leetcode.com/problems/product-of-array-except-self)
            15. [No.240](https://leetcode.com/problems/search-a-2d-matrix-ii) 同[No.74](https://leetcode.com/problems/search-a-2d-matrix)
            16. [No.304](https://leetcode.com/problems/range-sum-query-2d-immutable) 对每行做累和求差计算出范围的和
            17. [No.307](https://leetcode.com/problems/range-sum-query-mutable) 累和求差计算出范围的和
            18. [No.324](https://leetcode.com/problems/wiggle-sort-ii)
            19. [No.334](https://leetcode.com/problems/increasing-triplet-subsequence)
            20. [No.406](https://leetcode.com/problems/queue-reconstruction-by-height) 先按k排个序
            21. [No.419](https://leetcode.com/problems/battleships-in-a-board) 寻找每艘船唯一的特征点，如果一个点是1，且它的上方和左边都不是1，则这是一个特征点
            22. [No.442](https://leetcode.com/problems/find-all-duplicates-in-an-array) 1. 将n放到nums[n-1]，如果nums[n-1]已经等于n了，那n出现了两次。 2. 用nums[n-1]的正负记录n是否出现过。
            23. [No.457](https://leetcode.com/problems/circular-array-loop)
            24. [No.481](https://leetcode.com/problems/magical-string)
            25. [No.491](https://leetcode.com/problems/increasing-subsequences)
            26. [No.498](https://leetcode.com/problems/diagonal-traverse)
            27. [No.529](https://leetcode.com/problems/minesweeper)
            28. [No.807](https://leetcode.com/problems/max-increase-to-keep-city-skyline) 每栋建筑的最大高度是它所在行最大值与所在列最大值中的较小者。
    * 树
        * Trie树
            1. [No.208](https://leetcode.com/problems/implement-trie-prefix-tree)
            2. [No.211](https://leetcode.com/problems/add-and-search-word-data-structure-design)
            3. [No.421](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array)
            4. [No.648](https://leetcode.com/problems/replace-words)
            5. [No.677](https://leetcode.com/problems/map-sum-pairs)
            6. [No.820](https://leetcode.com/problems/short-encoding-of-words)
        * 前中后序遍历
            1. [No.114](https://leetcode.com/problems/flatten-binary-tree-to-linked-list) 前序遍历
            2. [No.144](https://leetcode.com/problems/binary-tree-preorder-traversal) 先序遍历
            3. [No.230](https://leetcode.com/problems/kth-smallest-element-in-a-bst) 中序排列
            4. [No.652](https://leetcode.com/problems/find-duplicate-subtrees) 要对左右子树分组
        * 摘叶算法
            1. [No.310](https://leetcode.com/problems/minimum-height-trees)
        * 其他
            1. [No.450](https://leetcode.com/problems/delete-node-in-a-bst) 删除BST的节点
            2. [No.779](https://leetcode.com/problems/k-th-symbol-in-grammar) 树形排列，利用子节点和父节点的index的关系，递归
    * 图
        * 并查集
            1. [No.200](https://leetcode.com/problems/number-of-islands) 计算有多少连通分量
            2. [No.547](https://leetcode.com/problems/friend-circles)
            3. [No.684](https://leetcode.com/problems/redundant-connection)
            4. [No.721](https://leetcode.com/problems/accounts-merge) 有相同的email代表两个账号属于同一个人(即两个账号节点之间有)
        * 涂色算法
            1. [No.785](https://leetcode.com/problems/is-graph-bipartite) 将相邻的点涂成不同的颜色，当涂色发生冲突时则不可分割
        * 拓扑排序
            1. [No.207](https://leetcode.com/problems/course-schedule) 前驱问题，典型的拓扑排序类问题
            2. [No.210](https://leetcode.com/problems/course-schedule-ii) 同[No.207](https://leetcode.com/problems/course-schedule)
            3. [No.802](https://leetcode.com/problems/find-eventual-safe-states) 寻找不在环内的元素
        * 单源最短路径
            1. [No.743](https://leetcode.com/problems/network-delay-time) dijkstra算法
