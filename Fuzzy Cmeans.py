import numpy as np
import matplotlib.pyplot as plt

def distance(x,y):
    return np.sqrt(np.sum(pow((x-y),2)))

# Distance Calculation

def CalculateDistance(data_points, cluster_centers):
    dp = len(data_points)
    cc = len(cluster_centers)
    d = np.zeros((dp, cc))
    for i in range(dp):
        for j in range(cc):
            d[i][j] = distance(data_points[i], cluster_centers[j])
    return d

# Membership calculation

def CalculateMembership(distances, q):
    ds0 = distances.shape[0]
    ds1 = distances.shape[1]
    rnk = np.zeros((ds0, ds1))
    for i in range(ds0):
        for j in range(ds1):
            lower = 0
            for l in range(ds1):
                lower += pow((distances[i][j] / distances[i][l]), 2/(q-1))
            rnk[i][j] = 1 / lower
    return rnk
# Updating cluster mean

def UpdateClusterMean(memberships, data_points, q):
    dps = data_points.shape[0]
    ms = memberships.shape[1]
    new_centers = np.zeros((ms, data_points.shape[1]))
    for j in range(ms):
        upper = 0
        lower = 0
        for i in range(dps):
            upper += pow(memberships[i][j], q) * data_points[i]
            lower += pow(memberships[i][j], q) 
        new_centers[j] = upper / lower
    return new_centers

def CalculateObjectiveFunc(data_points, memberships, cluster_centers, q, lamda):
    dps = data_points.shape[0]
    ms = memberships.shape[1]
    obj_func = 0
    for i in range(dps):
        for j in range(ms):
            obj_func += pow(memberships[i][j], q) * pow(distance(data_points[i], cluster_centers[j]), 2)
    obj_func *= lamda
    return obj_func

def ReachConvergence(data_points, memberships, cluster_centers, q, lamda):
    converged = False
    while not converged:
        old_obj_func = CalculateObjectiveFunc(data_points, memberships, cluster_centers, q, lamda)
        distances = CalculateDistance(data_points, cluster_centers)
        memberships = CalculateMembership(distances, q)
        cluster_centers = UpdateClusterMean(memberships, data_points, q)
        new_obj_func = CalculateObjectiveFunc(data_points, memberships, cluster_centers, q, lamda)
        if abs(old_obj_func - new_obj_func) < 0.01:
            converged = True
    return memberships, cluster_centers

data_points = np.array([[3, 5], [4, 6], [2, 8], [2, 3], [1, 4]])
cluster_centers = np.array([[2, 4], [1, 7]])
q = 2
lamda = 1

distances = CalculateDistance(data_points, cluster_centers)
memberships = CalculateMembership(distances, q)
cluster_centers = UpdateClusterMean(memberships, data_points, q)

final_memberships, final_cluster_centers = ReachConvergence(data_points, memberships, cluster_centers, q, lamda)

print(cluster_centers)
print("Final Memberships:")
print(final_memberships)
print("Final Cluster Centers:")
print(final_cluster_centers)




# What is the best and mot suitable q ?

q_values = range(2,11)
objective_function_values = []

for q in q_values:
    membership, cluster_centers = ReachConvergence(data_points,memberships, cluster_centers, q, lamda)
    objective_function_values.append(CalculateObjectiveFunc(data_points, membership, cluster_centers, q, lamda))

plt.plot(q_values, objective_function_values)
plt.xlabel('Q')
plt.ylabel('Objective Function')
plt.show()


# The best q is = 4


