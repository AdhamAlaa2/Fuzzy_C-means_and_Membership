 I implemented the Fuzzy C-means (FCM) Algorithm.
 Suppose I have a dataset with five data points, each with two features, I will cluster them into two groups.
 DataPoints : [[3, 5], [4, 6], [2, 8], [2, 3], [1, 4]] .
 I will use the Fuzzy C-means algorithm to cluster this data, First step is to initialize the cluster centers
 randomly. The cluster centers are as follows
 Clusters : [[2, 4], [1, 7]].
 To compute Data Points Membership I will iterate and execute Fuzzy C-mean steps until convergence
 At the end ill output the memberships of each point, also the updated centers for each
 cluster
 I will Assume that q =2 
 also ,  I will Repeat the steps but change the q value, try q from 2 to 10, and plot the objective function vs Q
 value and see the best q 
