

# Transition matrix
P = np.array([
    [0.6, 0.3, 0.1],
    [0.2, 0.5, 0.3],
    [0.3, 0.4, 0.3]
])

# Initial state vector (Study)
pi = np.array([1, 0, 0])

n = int(input("Enter number of days: "))

for i in range(n):
    pi = np.dot(pi, P)
    print(f"After day {i+1}: {pi}")