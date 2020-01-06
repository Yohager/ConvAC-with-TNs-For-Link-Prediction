### Katz & RageRank & SimRank

#### Katz index

定义：

$$\text{Katz}_{x,y}=\sum\limits_{l=1}^{\infty} \beta ^l |\text{walks}^{<l>}(x,y)| = \sum\limits_{l=1}^{\infty} \beta ^l [A^l]_{x,y}$$

$l$表示长度为$l$的$x,y$之间的路径。$A^l$表示网络邻接矩阵的$l$次方。$0 < \beta < 1$.



