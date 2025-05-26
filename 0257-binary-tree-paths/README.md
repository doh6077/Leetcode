<h2><a href="https://leetcode.com/problems/binary-tree-paths/">257. Binary Tree Paths</a></h2><h3>Easy</h3><hr><p>Given the <code>root</code> of a binary tree, return <em>all root-to-leaf paths in <strong>any order</strong></em>.</p>

<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg" style="width: 207px; height: 293px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,null,5]
<strong>Output:</strong> [&quot;1-&gt;2-&gt;5&quot;,&quot;1-&gt;3&quot;]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [&quot;1&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


<ol>
  <li>Find a leaf: A leaf is a node with no children.</li>
  <li>If either the left or right child exists:
    <ul>
      <li>Perform DFS recursively with the child as the new root.</li>
    </ul>
  </li>
  <li>If neither left nor right child exists:
    <ul>
      <li>Append the path to the answer array.</li>
    </ul>
  </li>
</ol>
